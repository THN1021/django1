# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from goods.models import Product, Tag
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from rest_framework.views import APIView


class Acquire(APIView):
    def get(self, request):
        show = {}
        show['id'] = Product.id
        show['name'] = Product.name
        show['price'] = Product.price
        show['type_id'] = Product.type_id
        show['weight'] = Product.weight
        show['stock'] = Product.stock
        show['tags'] = Product.tags
        return JsonResponse(show)
