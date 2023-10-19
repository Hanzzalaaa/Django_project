from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"



class TransactionSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()
    class Meta:
        model = Transaction
        fields = "__all__"
