from rest_framework.serializers import ModelSerializer
from goods import models


class GoodsSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'type_id', 'weight', 'stock', 'tags',)
