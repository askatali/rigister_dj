from django.db import models


class Frame(models.Model):
    code = models.CharField(max_length=80)
    vendor_code = models.CharField(max_length=80)
    width = models.CharField(max_length=80)
    height = models.CharField(max_length=80)
    aliquet = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='frame/')

    class Meta:
        db_table = 'frame'

    def __str__(self):
        return f'{self.code}'


class Image(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='frame/')

    class Meta:
        db_table = 'image'

    def __str__(self):
        return f'{self.frame.code}'
