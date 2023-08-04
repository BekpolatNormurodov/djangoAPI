from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
        {'name':'Dennis', 'age':28},
        {'name':'Jhon', 'age':20},
        {'name':'Danna', 'age':23},
        {'name':'Jhosa', 'age':25},
    ]
    return Response(person)