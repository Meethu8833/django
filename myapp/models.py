from django.db import models

# Create your models here.
class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    address=models.TextField()
    date_of_birth=models.DateField()
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class user_product(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_phone=models.CharField(max_length=10)
    def __str__(self):
        return self.user_name
class product_for_user(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    users=models.ForeignKey(user_product,on_delete=models.CASCADE)

class Publisher(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name    
class Book_publisher(models.Model):
    title=models.CharField(max_length=100)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=10,unique=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)


class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.CharField(max_length=100,unique=True)
    date=models.DateField()
    def __str__(self):
        return self.course_name
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    

class Organizer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    def __str__(self):
        return self.name
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=255)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
