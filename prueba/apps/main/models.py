from django.db import models

# Create your models here.
class Documento(models.Model):
    codigo = models.CharField(max_length=12, db_column='prov_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200)   
    
    class Meta:
        db_table = 'vca_proveedor'


class Proveedor(models.Model):
    codigo = models.CharField(max_length=12, db_column='prov_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200)   
    
    class Meta:
        db_table = 'vca_proveedor'


class Cliente(models.Model):
    codigo = models.CharField(max_length=12, db_column='clie_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200)   
    
    class Meta:
        db_table = 'vca_cliente'
        
        
class Almacen(models.Model):
    codigo = models.CharField(max_length=12, db_column='alma_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200)   
    
    class Meta:
        db_table = 'vca_alma'
        
        
class Unidad(models.Model):
    codigo = models.CharField(max_length=12, db_column='unid_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200, db_column='unid_nomb')

    class Meta:
        db_table = 'vca_unid'
        
class Item(models.Model):
    codigo = models.CharField(max_length=12, db_column='item_codi', primary_key=True ,blank=True)
    nombre = models.CharField(max_length=200)
    vca_itemalma = models.ManyToManyField(Almacen,through='ItemAlma')
    unidades = models.ForeignKey(Unidad,db_column='unid_codi')
    
    class Meta:
        db_table = 'vca_item'
    
class ItemAlma(models.Model):
    item = models.ForeignKey(Item,db_column='item_codi' ,blank=True)
    alma = models.ForeignKey(Almacen, db_column='alma_codi' ,blank=True)    
    stock = models.DecimalField( max_digits=18, decimal_places=2)
    
    class Meta:
        db_table = 'vca_itemalma'

class Setting(models.Model):
    
    def image_path(self,filename):
        ruta = "setting/%s/%s" % (self.setting_name,str(filename))
        return ruta
    
    setting_name = models.CharField(max_length=200)
    my_name = models.CharField(max_length=200)
    my_job = models.CharField(max_length=200)
    my_descriptions = models.TextField(max_length=200)
    my_foto = models.ImageField(upload_to=image_path)
    background = models.ImageField(upload_to=image_path)    
    status = models.BooleanField(default=False)
    
    
    def __unicodi__(self):
        return self.setting_name
    
    class Meta:
        verbose_name = "configuracion del a Web"
        verbose_name_plural = "configuraciones del a Web"


