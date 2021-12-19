from django.db import models

class Computer(models.Model):
    name_comp = models.CharField(max_length=255, verbose_name="Название Компьютера")
    hard_disk_number = models.IntegerField(verbose_name="Количество жестких дисков")
    general_storage = models.IntegerField(verbose_name="Общее количество ГБ ROM")

class OS(models.Model):
    name_os = models.CharField(max_length=150, verbose_name="Название Операционной системы")
    storage_os = models.IntegerField(verbose_name="Количество занимаемой ОС памяти")
    start_numbers = models.IntegerField(verbose_name="Количество запусков ОС")
    Comp_OS = models.ForeignKey(Computer, on_delete=models.CASCADE, null=True)