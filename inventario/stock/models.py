from django.db import models
from django.utils import timezone

class inventarioManager(models.Manager):
    def productos_disponibles(self):
        """
        Devuelve todos los productos cuya cantidad sea mayor a 0.
        """
        return self.filter(cantidad__gt=0)

    def productos_por_categoria(self, categoria):
        """
        Devuelve todos los productos en una categoría específica.
        """
        return self.filter(categoria=categoria)

    def productos_cercanos_a_expiracion(self, dias=7):
        """
        Devuelve todos los productos que expiran dentro de los próximos 'dias' días.
        """
        fecha_limite = timezone.now().date() + timezone.timedelta(days=dias)
        return self.filter(fecha_expiracion__lte=fecha_limite)

class inventario(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha_expiracion = models.DateField(null=True, blank=True)
    fecha_entrada = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(null=True, blank=True)

    objects = inventarioManager()

    class Meta:

        ordering = ['-fecha_entrada']

        indexes = [
            models.Index(fields=['nombre_producto']),
            models.Index(fields=['fecha_entrada']),
        ]

    def __str__(self):
        return f'{self.nombre_producto} - Cantidad: {self.cantidad}'