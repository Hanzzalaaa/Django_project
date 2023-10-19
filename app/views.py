from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.




class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer






class Search(APIView):
    def get(self,request):
        search_term = request.GET.get('search')
        data_lst = []
        if search_term:
            result = Customer.objects.filter(
                Q(name__icontains=search_term) | Q(pk__icontains=search_term) |
                Q(post_code=search_term) | Q(phone_number__icontains=search_term)
            )

            if result:
                for i in result:
                    data = {
                        'id':i.pk,
                        'name':i.name,
                        'post_code':i.post_code,
                        'phone_number':i.phone_number,
                    }
                    data_lst.append(data)
            else:
                Response({
                    'message':'No customer found'
                })
        else:
            Response(Customer.objects.all())

        return Response(data_lst)
