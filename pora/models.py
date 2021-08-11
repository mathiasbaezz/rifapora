from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils import timezone

# Create your models here.
class Codigo(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField( blank=True)


    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Vendedor(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    venta = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.nombre
