from django.db import models

# Create your models here.
class Customer(models.Model):
    name =  models.CharField(max_length=56,null=True,blank=True)
    post_code =  models.CharField(max_length=56,null=True,blank=True)
    phone_number =  models.CharField(max_length=56,null=True,blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    i_customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='trans_customer')
    date = models.DateTimeField(auto_created=True)
    category =  models.CharField(max_length=56,null=True,blank=True)

    def __str__(self):
        return f"transtion id {self.pk} and customer id {self.i_customer}"