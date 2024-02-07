from django.db import models


class Sweatshirt(models.Model):
    size = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    price = models.IntegerField()
    description = models.TextField(blank=True,  null=True)
    photo = models.ImageField(upload_to='sweatshirt/')
    number = models.IntegerField(blank=True, null=True)


    class Meta:
        db_table = 'sweatshirt'

    def __str__(self):
        return f'{self.size}'


class Photo(models.Model):
    sweatshirt = models.ForeignKey(Sweatshirt, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='sweatshirt/')

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return f'{self.sweatshirt.size}'

