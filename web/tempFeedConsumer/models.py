from django.db import models

# Create your models here.

#User = get_user_model()

class Reading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temp = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.timestamp} : {self.temp}"
