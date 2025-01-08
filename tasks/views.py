# from django.shortcuts import render
from .serializers import JavobgarSerializer
# from rest_framework import viewsets, permissions
from .models import Javobgar
# from rest_framework.permissions import AllowAny
# class JavobgarViewset(viewsets.ModelViewSet):
#     queryset = Javobgar.objects.all()
#     serializer_class = JavobgarSerializers
#     permission_classes = [AllowAny]
# # Create your views here.

from rest_framework import mixins
from rest_framework import generics

class JavobgarList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Javobgar.objects.all()
    serializer_class = JavobgarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class JavobgarDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Javobgar.objects.all()
    serializer_class = JavobgarSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)