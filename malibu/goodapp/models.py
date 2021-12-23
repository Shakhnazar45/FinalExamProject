from django.db import models



class User(models.Model):

    name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    PhoneNumber = models.PositiveIntegerField()
    email = models.CharField(max_length=20)


class Market(models.Model):
        CATEGORIES = (
            ('Champagne', 'Champagne'),('Cognac', 'Cognac'),('Pink Wine', 'Pink Wine'),('Red Wine', 'Red Wine'),('Rum', 'Rum'),('White Wine', 'White Wine'),
            ('Sparkling Wine', 'Sparkling Wine'),
        )
        name = models.CharField(max_length=200)
        price = models.PositiveIntegerField()
        url = models.ImageField(null = True,blank = True)
        category = models.CharField(max_length=200, choices = CATEGORIES)

class Cart (models.Model):
         prodcount = models.CharField(max_length=200)
         all_price = models.PositiveIntegerField()
         user = models.ForeignKey(User,on_delete=models.CASCADE)
         market = models.ForeignKey(Market,  on_delete=models.CASCADE)
