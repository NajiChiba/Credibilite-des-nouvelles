import re
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .models import New
from .serializers import NewsSerializer 
from django.http import HttpResponse
from .data_treatement.training import TrainingModels
from .data_treatement.analysentiment import analysentiment
from django.utils.encoding import smart_str, smart_bytes


def predict(news):
    pass

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def check_news(request):
    try:
        if request.method == 'POST':
            news_data = json.loads(request.body)
            article= news_data['content']

        result = TrainingModels.predict('article')
        #print('------------- result  ---> '+str(result))
        
        if result == 1:
            return HttpResponse("fake")

        if result == 0:
            return HttpResponse("real")

    except Exception as ex:
        print(ex)
        return HttpResponse('nothing')


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def check_sentiment(request):
    try:
        if request.method == 'POST':
            news_data = json.loads(request.body)
            article= news_data['content']

        result = analysentiment(article)
        print('------------- Sentiment  ---> '+str(result))
        
        if result < 0:
            return HttpResponse("-")

        if result >= 0:
            return HttpResponse("+")

    except Exception as ex:
        print(ex)
        return HttpResponse('nothing')