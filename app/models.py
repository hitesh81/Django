from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default=459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.email


class Service_provider(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    contact = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    country_id = models.CharField(max_length=200)
    state_id = models.CharField(max_length=200)
    city_id = models.CharField(max_length=200)
    service = models.CharField(max_length=200, default="test")
    sub = models.CharField(max_length=200, default="test")
    profile_img = models.FileField(upload_to='', null=True, blank=True, default="set.jpg")

    def __str__(self):
        return self.name


class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    contact = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    city_id = models.CharField(max_length=200)
    country_id = models.CharField(max_length=200)
    state_id = models.CharField(max_length=200)


class Service_detail(models.Model):
    Service_name = models.CharField(max_length=200)
    Service_img = models.FileField(upload_to='', null=True, blank=True, default="set.jpg")
    def __str__(self):
        return self.Service_name


class Sub_service(models.Model):
    Service_id = models.ForeignKey(Service_detail, on_delete=models.CASCADE)
    SubService_name = models.CharField(max_length=50)

    def __str__(self):
        return self.SubService_name


class AllInfo(models.Model):
    Service_id = models.ForeignKey(Service_detail, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Sub_service, on_delete=models.CASCADE)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Service_id = models.ForeignKey(Service_detail, on_delete=models.CASCADE)
    Sub_id = models.ForeignKey(Sub_service, on_delete=models.CASCADE)
    service_provider_assign = models.ForeignKey(Service_provider, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    Orderdate = models.DateField(auto_now_add=True)
    ordertime = models.TimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    pincode = models.CharField(max_length=50)

    status = models.CharField(max_length=200, default="Pending")

    def __str__(self):
        return self.Orderdate


class feedback(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    review = models.TextField(max_length=200)

    def __str__(self):
        return self.rating













