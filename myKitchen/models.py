from django.db import models
    
class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    stext = models.CharField(max_length=200)
    createdat = models.DateTimeField()
    
    def __str__(self):
        return self.name
#    def __unicode__(self):
#        return u"%s" % self.name    
      
class Quantity_Units(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    stext = models.CharField(max_length=200,null=True)
    createdat = models.DateTimeField()

    def __str__(self):
        return self.name

class Qunits_Conversions(models.Model):
    id = models.AutoField(primary_key=True)
  #  source_qunit = models.ForeignKey(Quantity_Units, on_delete=models.CASCADE)
    target_qunit = models.ForeignKey(Quantity_Units, on_delete=models.CASCADE)
    faktor = models.FloatField(default=1)
    
class Material_Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    stext = models.CharField(max_length=200,null=True)
    createdat = models.DateTimeField()    

    def __str__(self):
        return self.name    
    
class materials(models.Model):
    id = models.AutoField(primary_key=True)
    stext = models.CharField(max_length=200)
    qunit = models.ForeignKey(Quantity_Units, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    material_group = models.ForeignKey(Material_Groups, on_delete=models.CASCADE)
    minstock = models.IntegerField(default=0) #minimum stok miktarı
    endday = models.IntegerField(default=0) #alındıktan sonra tüketilmesi gereken gün sayısı
    openendday = models.IntegerField(default=0) #ürün paketi açıldıktan sonra tüketilmesi gereken gün sayısı
    createdat = models.DateTimeField()

    def __str__(self):
        return self.name
    
