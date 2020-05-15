from django.db import models

from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is 150 KB")

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)

class NavyEmployee(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField( max_length=254, unique=True)
	details = models.CharField(max_length=500)
	Photo = models.ImageField(upload_to='resources/%Y/%m/%d/', null=True, blank=True, validators=[validate_image])
	created = models.DateTimeField('date published')
# Create your models here.
