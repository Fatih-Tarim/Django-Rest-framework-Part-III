from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profil')
    bio = models.CharField(max_length=300, blank=True, null=True)
    sehir = models.CharField(max_length=120, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to='profil_fotograflari/%Y/%m/')

    def __str__(self):
        return self.user.username
    
    def save(self, *args,**kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.foto.path)
    
    class Meta:
        verbose_name_plural = "Profiller"
     
class ProfilDurum(models.Model):
    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    durum_mesaji = models.CharField(max_length=240)
    yaratilma_zamani = models.DateTimeField(auto_now_add=True) #auto_now_add -> zaman bir kere alınır ve değişmez
    guncellenme_tarihi = models.DateTimeField(auto_now=False, null=True) #auto_now -> her güncellendiğinde anlık saati alır ve kayıt eder

    def __str__(self):
        return str(self.user_profil)      
    
    class Meta:
        verbose_name_plural = "Profil Mesajları"
