from django.db import models
from django.utils import timezone

# Create your models here.
class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    maintence_id = models.AutoField(primary_key=True)
    vehicle_reg_no = models.CharField(max_length= 10)
    maintenance_type = models.CharField(max_length= 20)
    description = models.CharField(max_length= 50)
    maintenance_date = models.DateTimeField(auto_now_add=True)
    next_due_date = models.DateTimeField()
    technician= models.CharField(max_length=20, default='Unknown technician')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return f'{self.maintenance_type} for {self.vehicle_reg_no} by {self.technician}'
