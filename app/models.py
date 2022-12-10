from django.db import models

class Historial(models.Model):
    id_img = models.IntegerField()
    status = models.BooleanField(default=False)
    step = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    end_time = models.DateTimeField(auto_now=True)
    #duration = models.TimeField()

    class Meta:
        managed = False
        db_table = 'historial'


class LogError(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name="Error Ocurred")
    step = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'log_error'
