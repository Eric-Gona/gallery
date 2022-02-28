from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
  name = models.CharField(max_length =100)

  def save_location(self):
    self.save()

  def deleting_location(self):
      self.delete()

  def updating_location(self, update):
    self.name = update
    self.save()

  @classmethod
  def getting_location(cls, id):
    location_id = Location.objects.get(pk = id)
    return location_id

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length =100)

  def save_category(self):
    self.save()

  def deleting_category(self):
    self.delete()

  def updating_category(self, update):
    self.name = update
    self.save()

  @classmethod
  def find_category(cls, id):
    category_id = Category.objects.get(pk = id)
    return category_id

  def __str__(self):
    return self.name

class Image(models.Model):
  name = models.CharField(max_length=60)
  description = models.TextField()
  image = CloudinaryField('image')
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)

  def save_image(self):
    self.save()

  @classmethod
  def get_location(cls,location):
    images = Image.objects.filter(location__name__icontains=location)
    return location

  def delete_image(self):
    self.delete()

  @classmethod
  def get_images(cls):
    images = cls.objects.all()
    return images

  @classmethod
  def get_image_id(cls,id):
    image_id = cls.objects.filter(id= id).all()
    return image_id

  @classmethod
  def search_images(cls,category):
      images = Image.objects.filter(category__name__icontains=category)
      return images

  @classmethod
  def update_image(cls, id ,name,description , location, category):
    update = cls.objects.filter(id = id).update(name = name,description = description,location = location,category = category)
    return update


  def __str__(self):
    return self.name
