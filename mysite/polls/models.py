import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #객체의 표현을 보기쉽게 하기 위해 추가한 함수
    def __str__(self):
        return self.question_text

    #최근에 발행됐는지 확인해주는 함수
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text