from rest_framework.viewsets import ViewSet
from .permissions import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate,login


class Homepage(ViewSet):
    def list(self,request):
        return Response('Welcome to our site!')
class LoginView(ViewSet):
    def create(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return Response(f'Welcome to our site, {username}!')
        return Response(serializer.errors)

class SurveyView(ViewSet):
    permission_classes = [AdminPermission]
    serializer_class = SurveySerializer

    def list(self,request):
        surveys = Survey.objects.all()
        serializer = self.serializer_class(surveys,many=True)
        return Response(serializer.data,status=200)
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors)
    def retrieve(self,request,survey_id):
        survey = Survey.objects.get(id=survey_id)
        serializer = self.serializer_class(survey)
        return Response(serializer.data,status=200)
    def update(self,request,survey_id):
        survey = Survey.objects.get(id=survey_id)
        serializer = self.serializer_class(survey,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=202)
        return Response(serializer.errors)
    def destroy(self,request,survey_id):
        survey = Survey.objects.get(id=survey_id)
        survey.delete()
        return Response(status=204)


class QuestionView(ViewSet):
    permission_classes = [AdminPermission]
    serializer_class = QuestionSerializer

    def list(self,request):
        questions = Question.objects.all()
        serializer = self.serializer_class(questions,many=True)
        return Response(serializer.data,status=200)
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def retrieve(self,request,question_id):
        question = Question.objects.get(id=question_id)
        serializer = self.serializer_class(question)
        return Response(serializer.data,status=200)
    def update(self,request,question_id):
        question = Question.objects.get(id=question_id)
        serializer = self.serializer_class(question,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=202)
        return Response(serializer.errors)
    def destroy(self,request,question_id):
        question = Question.objects.get(id=question_id)
        question.delete()
        return Response(status=204)

"""
Получение списка активных опросов
"""
class SurveyViewForUser(ViewSet):
    permission_classes = [UserPermission]
    serializer_class = SurveySerializer
    def list(self,request):
        surveys = Survey.objects.filter(status='active')
        serializer = self.serializer_class(surveys,many=True)
        return Response(serializer.data,status=200)


class AnswerView(ViewSet):
    serializer_class = AnswerSerializer
    def list(self,request,survey_id):
        questions = Question.objects.filter(survey=survey_id)
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data,status=200)
    def create(self,request,survey_id):
        questions = Question.objects.filter(survey=survey_id)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
class AnswersView(ViewSet):
    serializer_class = AnswerSerializer
    def list(self,request,user_id):
        answers = Answer.objects.filter(user__id=user_id)
        serializer = self.serializer_class(answers,many=True)
        return Response(serializer.data,status=200)
