from django.db import models

class Participation(models.Model):
    fcs = models.CharField(max_length=200, null=False)
    institution_name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=70, null=False, blank=True, unique=True)

    def __str__(self):
        return self.fcs