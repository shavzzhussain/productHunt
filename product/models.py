from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    vote_count = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product/')
    icon = models.ImageField(upload_to='product/')
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def  __str__(self):
        return self.title
    def short(self):
        return self.body[:100]
    def cool_date(self):
        return self.date.strftime('%m/%B/%Y')




