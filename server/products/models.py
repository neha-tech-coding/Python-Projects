from django.db import models

# DB
# class---> Database Table Name
# attributes---> Columns
# instance/object --- row

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=50,null=False)  #max length
    description=models.TextField(null=True) #empty pass
    price=models.FloatField(default=99)
    updatedAt=models.DateTimeField(auto_now=True)
    createdAt=models.DateTimeField(auto_created=True)
    id=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.title


