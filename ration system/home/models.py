from django.db import models


# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=20, default="1234567891")
    status = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    UID = models.CharField(max_length=100)
    RCN = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ShopKeeper(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    shop_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    rice_purched = models.IntegerField()
    rice_alloted = models.IntegerField()

    dal_purched = models.IntegerField()
    dal_alloted = models.IntegerField()

    sugar_purched =models.IntegerField()
    sugar_alloted = models.IntegerField()

    wheat_purched = models.IntegerField()
    wheat_alloted = models.IntegerField()

    def __str__(self):
        return self.username

class History(models.Model):
    date = models.DateTimeField(auto_now = True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    rice = models.CharField(max_length=100)
    dal = models.CharField(max_length=100)
    sugar = models.CharField(max_length=100)
    wheat = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.client.name


class Feedback(models.Model):
    # client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    client = models.CharField(max_length=100, default=123)
    mobie_no = models.CharField(max_length=20, default="8446601001")
    email = models.EmailField()
    comment = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.client

