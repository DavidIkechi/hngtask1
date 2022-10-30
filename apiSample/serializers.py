from rest_framework import serializers
from .models import *

class HNGUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HNGUser
        fields = ['bio', 'age', 'backend', 'slackUsername']