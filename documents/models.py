from django.db import models

# Create your models here.
class Documents(models.Model):
	file_upload=models.FileField(upload_to='dms/files')