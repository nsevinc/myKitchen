from django.db import models

# Create your models here.
class malzemeler(models.Model):
    malzemeid = models.CharField(max_length=50)
    malzeme_text = models.CharField(max_length=200)
    miktar = models.IntegerField(default=0)
    def __str__(self):
        return self.malzeme_text