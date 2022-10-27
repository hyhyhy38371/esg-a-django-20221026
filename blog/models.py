from pydoc import describe
from django.db import models
from django.core.validators import MaxValueValidator

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
        ]
    )
    def get_absolute_url(self):
        #TODO: 향후에는 장고의 URL REVERSE 기능을 사용하세용!
        return f"/blog/restaurants/{self.pk}/"
    
    def __str__(self):
        return f'[{self.pk}]{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        #TODO: 향후에는 장고의 URL REVERSE 기능을 사용하세용!
        return f"/blog/{self.pk}/"
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'