from django.core.management.base import BaseCommand
import socket
import threading
from serverapi.models import Computer
import json

class Command(BaseCommand):
    help = 'Starts a TCP socket server'

    def handle(self, *args, **kwargs):
        host = '192.168.13.62'  # Escucha en localhost
        port = 69  # Puerto arbitrario para escucha de sockets
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            self.stdout.write(f"Listening on {host}:{port}")

            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        try:
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break  # Conexión cerrada por el cliente
                    data_dict = json.loads(data.decode('utf-8'))
                    # Aquí procesas los datos recibidos
                    self.save_computer_info(data_dict)
                    conn.sendall(b"Datos recibidos")
        except Exception as e:
            print(f"Error handling connection from {addr}: {e}")

    def save_computer_info(self, data):
        Computer.objects.create(
            department_name=data['department_name'],
            disk_total=data['disk_total'],
            disk_used=data['disk_used'],
            disk_free=data['disk_free'],
            main_process_id=data['main_process_id'],
            memory_ram=data['memory_ram'],
            ip_address=data['ip_address'],
            last_update=data['last_update']
        )
