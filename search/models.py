from django.db import models

class Question(models.Model):
    question_stem = models.CharField(max_length=400)
    answer = models.ImageField()
    ori_path = models.CharField(max_length=200)