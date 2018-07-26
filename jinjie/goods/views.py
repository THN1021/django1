# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from goods.models import Product, Tag
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from goods.serializer import GoodsSerializer
import json
from rest_framework.views import APIView


class Acquire(APIView):
    def get(self, request):
        get = request.GET
        show = {}
        if get.get('id'):
            a = get.get('id')
            # show = {}
            # show['idd']=a
            temp = Product.objects.get(id=a)
            show['id'] = temp.id
            show['name'] = temp.name
            show['price'] = temp.price
            show['type_id'] = temp.type_id
            show['weight'] = temp.weight
            show['stock'] = temp.stock
            temp1 = temp.tags.all()
            b = []
            for i in temp1:
                b.append(i.name)
            show['tags'] = b
        else:
            tid = get.get('type_id')
            cpp = int(get.get('count_pp'))
            page = get.get('page')
            # for i in range(page):
            b = []
            temp = Product.objects.filter(type_id=tid)
            print temp[0]
            for j in range(cpp):
                temp1 = temp[j]
                show1 = {}
                show1['id'] = temp1.id
                show1['name'] = temp1.name
                show1['price'] = temp1.price
                show1['type_id'] = temp1.type_id
                show1['weight'] = temp1.weight
                show1['stock'] = temp1.stock
                temp2 = temp1.tags.all()
                c = []
                for i in temp2:
                    c.append(i.name)
                show1['tags'] = c
                b.append(show1)
            show['products'] = b
        return JsonResponse(show)

    def post(self, request):
        post = JSONParser().parse(request)
        weight = post["weight"]
        name = post['name']
        price = post['price']
        type_id = post['type_id']
        stock = post['stock']
        tags = post['tags']
        p = Product.objects.create(name=name, price=price, type_id=type_id, weight=weight, stock=stock)
        p.tags.set(tags)
        show = {}
        show['id'] = p.id
        return JsonResponse(show)

    def put(self, request):
        get = request.GET
        show = {}
        id = get.get("id")
        put = JSONParser().parse(request)
        try:
            temp = Product.objects.get(id=id)
            temp.name = put['name']
            temp.weight = put['weight']
            temp.price = put['price']
            temp.type_id = put['type_id']
            temp.stock = put['stock']
            temp.tags.set(put['tags'])
            temp.save()
            show['result'] = 200
        except:
            show['result'] = 404
        return JsonResponse(show)

    def delete(self,request):
        get = request.GET
        show = {}
        id = get.get("id")
        try:
            temp = Product.objects.get(id=id)
            temp.delete()
            show['result'] = 200
        except:
            show['result'] = 404
        return JsonResponse(show)
