from django.shortcuts import render
from .models import Customer, Tournament, Player, Round, Match
from rest_framework import generics
from .serializers import (
    CustomerSerializer,
    TournamentSerializer,
    PlayerSerializer,
    RoundSerializer,
    MatchSerializer,
)


class CustomerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = (Customer.objects.all(),)
    serializer_class = CustomerSerializer


class CustomerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TournamentCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new tournament
    queryset = (Tournament.objects.all(),)
    serializer_class = CustomerSerializer


class TournamentList(generics.ListAPIView):
    # API endpoint that allows tournament to be viewed.
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
