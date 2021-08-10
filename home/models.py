from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
CHOICE = (('', 'Select'), ('Worker', 'Worker'), ('Manager', 'Manager'), ('Accountant', 'Accountant'),
          ('Salesperson', 'Salesperson'))


class Slider(models.Model):
    photo = models.ImageField(upload_to='media')


class Status(models.Model):
    status = models.TextField()


class Slideshow(models.Model):
    photo = models.ImageField(upload_to='media')


class Category(models.Model):
    sno = models.CharField(max_length=1000)
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiry = models.CharField(max_length=300)
    ingredient = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.EmailField()
    otp = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name


class Otp(models.Model):
    otp = models.CharField(max_length=10)


class Rating(models.Model):
    name = models.CharField(max_length=300)
    rating = models.CharField(max_length=300)
    review = models.TextField()

    def __str__(self):
        return self.name


class Aboutus(models.Model):
    photo = models.ImageField(upload_to='media')


class Distributor(models.Model):
    store_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)

    def __str__(self):
        return self.store_name


class Manager(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Accountant(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Salesperson(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    query = models.TextField()

    def __str__(self):
        return self.name


class Career(models.Model):
    type = models.CharField(max_length=300, choices=CHOICE)
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    date = models.DateField()
    cv = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class CareerStatus(models.Model):
    status = models.CharField(max_length=300)
