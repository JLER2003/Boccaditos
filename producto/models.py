from django.db import models

#Tabla categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

#Tabla producto relacionada con categoria
class Producto(models.Model):
    # ID_Producto = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.nombre + '- by' + self.categoria
    
    def __str__(self):
        return self.nombre + ' - by ' + str(self.categoria)


#Tabla Cliente
class Cliente(models.Model):
    # ID_Cliente = models.AutoField(primary_key=True)
    Nombre = models.TextField(blank=True)

    def __str__(self):
        return self.Nombre

#Tabla Venta relacionada con producto y cliente
class Venta(models.Model):
    # ID_Venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha   = models.DateField()
    
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.producto.categoria} - {self.cliente.Nombre}"


