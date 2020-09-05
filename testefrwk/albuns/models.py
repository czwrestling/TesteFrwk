from django.db import models

# Create your models here.
class AlbunsPost(models.Model):

    titulo = models.CharField(max_length=50,null=True)
    descricao = models.CharField(max_length=255,null=True)
    #arquivo = models.FileField(upload_to='documentos/')
    def _str_(self):
            return self.titulo