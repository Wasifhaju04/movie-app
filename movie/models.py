from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
    movie_id=models.AutoField
    name=models.CharField(max_length=50)
    director_name=models.CharField(max_length=50)
    budget=models.BigIntegerField()
    box_office=models.BigIntegerField()
    imdb_ratings=models.FloatField()
    release_date=models.DateField(default=timezone.now)
    verdict=models.CharField(max_length=50)
    poster=models.ImageField(upload_to="movie\images",default=" ")
    rent_price=models.FloatField(default=100.00)
    genre=models.CharField(max_length=50,default="Drama")

    def __str__(self):
        return self.name
    
class Blog (models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="blog/images" )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return self.title + " | " + str(self.author)
    
        
    

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50,default="")
    name =  models.CharField(max_length=50)
    desc =  models.CharField(max_length=500)
    phone = models.IntegerField()
    screenshot = models.ImageField(upload_to="contact\images",default="https://via.placeholder.com/500x500.png?text=Default")
    pub_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
    

class order(models.Model):
    jsonCart=models.CharField(max_length=200)
    email = models.CharField(max_length=50,default=" ")
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    address =  models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state =  models.CharField(max_length=50)
    isSameBillingAddress=models.BooleanField()
    
    def __str__(self):
        return self.email


        