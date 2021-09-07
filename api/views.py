#from django.http import response
#from django.shortcuts import render
#from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Raw, Ingredient
from . import serializers
import mysql.connector
import json
from common import db

#TODO: Complete MySQL Tests, JWT MiddleWare

print("CREATING")
dbi = db.DB()                    

# Create your views here.
""" class getIngridients(generics.ListCreateAPIView):
    queryset = Ingridient.objects.all()
    serializer_class = IngridientSerializer """

@api_view(['GET'])
def listIngridients(request):    
    #ingridients = Ingredient.objects.raw("SELECT * FROM product ORDER BY id LIMIT 1")    
    #serializer = serializers.Ingredient(ingridients, many = True)
    [rows, cols] = dbi.execute("""
        SELECT
            p.id,
            p.cost,
            JSON_ARRAYAGG(JSON_OBJECT(
                'id', i.id,
                'name', i.name,
                'unit', i.uom,
                'rate', i.rate
            )) as ingredients
        FROM product p
        INNER JOIN map_ingredient_product m ON m.product_id=p.id
        INNER JOIN ingredient i ON i.id=m.ingredient_id
        GROUP BY p.id
    """, True)
    dbi.execute("INSERT INTO product(name, cost) VALUES('XYZ3', 10)", False)
    #Bind
    return Response({"statusCode": 1, "data": rows })

#cursor.close()
#cnx.close()