from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]
    first_name = models.CharField(max_length=200, verbose_name="Nombre")
    last_name = models.CharField(max_length=200, verbose_name="Apellido")
    email_id = models.EmailField(max_length=100,blank=True, verbose_name="Email")
    phone_number = models.CharField(max_length=10,verbose_name="Teléfono", blank=True)
    address = models.TextField(verbose_name="dirección")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name="Género", blank=True)
    dab =models.DateField(verbose_name="Nacimiento")
    joining_date = models.DateField(verbose_name="inscripción")
    jobs = models.ManyToManyField('Job',verbose_name="Trabajos" ,blank=True)
    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Empleados"

class Job(models.Model):
    name = models.CharField(max_length=240, verbose_name="Nombre del trabajo")
    class Meta:
        verbose_name="Trabajo"
        verbose_name_plural = "Trabajos"

    def __str__(self):
        return self.name