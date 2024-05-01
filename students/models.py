from django.db import models




class Cars(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.make} {self.model} {self.price}"

