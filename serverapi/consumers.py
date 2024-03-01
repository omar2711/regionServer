from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import Computer

class ComputerInfoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # Convertir el texto recibido a JSON
        data = json.loads(text_data)

        # Extraer los datos
        department_name = data['department_name']
        disk_total = data['disk_total']
        disk_used = data['disk_used']
        disk_free = data['disk_free']
        main_process_id = data['main_process_id']
        memory_ram = data['memory_ram']
        ip_address = data['ip_address']
        last_update = data['last_update']

        # Guardar los datos en la base de datos
        await self.save_computer_info(department_name, disk_total, disk_used, disk_free, main_process_id, memory_ram, ip_address, last_update)

        # Opcional: enviar confirmación al cliente
        await self.send(text_data=json.dumps({"status": "Datos recibidos y guardados."}))

    @sync_to_async
    def save_computer_info(self, department_name, disk_total, disk_used, disk_free, main_process_id, memory_ram, ip_address, last_update):
        # Crear y guardar un nuevo objeto Computer en la base de datos
        Computer.objects.create(
            department_name=department_name,
            disk_total=disk_total,
            disk_used=disk_used,
            disk_free=disk_free,
            main_process_id=main_process_id,
            memory_ram=memory_ram,
            ip_address=ip_address,
            last_update=last_update
        )
