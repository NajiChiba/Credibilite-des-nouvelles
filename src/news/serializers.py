from rest_framework import serializers
from .models import New

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'body', 'fake')