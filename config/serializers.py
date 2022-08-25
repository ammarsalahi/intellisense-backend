from os import defpath
from .models import Roadmap, Util, FAQ
from rest_framework import serializers


class RoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = '__all__'
        depth = 1


class UtilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Util
        fields = '__all__'
        depth = 1


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        depth = 1


