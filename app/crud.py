from django.utils import timezone
from .models import *

def create_historial(id_img, step):
    Historial(id_img = id_img, step = step).save()

def finish_historial(id_img, step):
    Historial.objects.filter(id_img = id_img, step = step).update(end_time = timezone.now(), status=True)

def add_log(step, message):
    LogError(step = step, description = message).save() 