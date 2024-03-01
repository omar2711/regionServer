from django.db import models

class Computer(models.Model):
    department_name = models.CharField(max_length=100)
    disk_total = models.BigIntegerField()
    disk_used = models.BigIntegerField()
    disk_free = models.BigIntegerField()
    main_process_id = models.IntegerField()
    memory_ram = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    last_update = models.DateTimeField()

    def __str__(self):
        return self.department_name