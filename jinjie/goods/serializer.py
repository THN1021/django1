from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from goods import models as goods_models
from django.db import models


class GoodsSerializer(ModelSerializer):
    class Meta:
        model = goods_models.Product
        fields = ('id', 'name', 'price', 'type_id', 'weight', 'stock', 'tags',)

class PostSerializer(serializers.Serializer):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    type_id = models.IntegerField()
    weight = models.FloatField()
    stock = models.BooleanField()
    tags = models.ManyToManyField('Tag')
