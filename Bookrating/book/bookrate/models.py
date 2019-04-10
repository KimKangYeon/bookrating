from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,)
    review = models.TextField()
    price = models.FloatField(default=1,)
    SCORES = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    score = models.CharField(max_length=5, choices=SCORES, default = ""
        )
   
    def __str__(self):
        return self.title