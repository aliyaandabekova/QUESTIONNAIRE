from rest_framework import serializers
from .models import *

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5)
