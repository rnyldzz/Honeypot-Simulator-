import socket
import threading
import datetime

log_file = "honeypot_logs.txt"

services = {
    21:"FTP",
    22:"SSH",
    23:"Telnet"
}

def handle_connection(client_socket, client_adress, port):
    """ Glen bağlantıları yönetir ve loglar."""
    service_name= services.get(port, "Bilinmeyen Hizmet")
    
    if port == 21: # FTP
        client_socket.send(b"220 (vsFTPd 3.0.3)\r\n")
    elif port == 22: # SSH
        client_socket.send(b"SSH-2.0-OpenSSH_7.4p1 Debian-10\r\n")
    elif port == 23: # Telnet
        client_socket.send(b"\r\nLogin: ")
    
    log_entry = f"[{datetime.datetime.now()}] - IP: {client_address[0]}, Port: {port} ({service_name}) - Bağlantı Kuruldu.\n"
    
    try:
        # Saldırganın gönderdiği verileri oku
        data = client_socket.recv(1024)
        if data:
            decoded_data = data.decode("utf-8", errors="ignore").strip()
            log_entry += f"[{datetime.datetime.now()}] - IP: {client_address[0]} - Alınan Veri: {decoded_data}\n"
    except Exception as e:
        log_entry += f"[{datetime.datetime.now()}] - Hata: {e}\n"
    finally:
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        client_socket.close()

def start_honeypot():
    """Honeypot sunucusunu başlatır."""
    for port in services:
        server_thread = threading.Thread(target=listen_on_port, args=(port,))
        server_thread.start()
    print("Honeypot simülasyonu başlatıldı. Saldırılar bekleniyor...")

def listen_on_port(port):
    """Belirli bir portu dinler."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(5)
        print(f"Port {port} dinleniyor...")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[{datetime.datetime.now()}] - IP: {client_address[0]} adresinden port {port} bağlantısı geldi.")
            client_handler = threading.Thread(target=handle_connection, args=(client_socket, client_address, port))
            client_handler.start()
    except Exception as e:
        print(f"Port {port} hatası: {e}")
        server_socket.close()

if __name__ == "__main__":
    start_honeypot()
