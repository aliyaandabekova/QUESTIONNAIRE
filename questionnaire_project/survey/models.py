from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField()
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=(
        ('active','active'),
        ('passive','passive')
    ))
    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    type_of_question = models.CharField(max_length=100,choices=(
        ('answer with text','answer with text'),
        ('select one option','select one option'),
        ('select several options','select several options')
    ))
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    def __str__(self):
        return self.answer_text

