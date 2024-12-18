import datetime
from django.db import models
from django.utils import timezone

<<<<<<< HEAD
#Createyourmodelshere.
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
=======
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
<<<<<<< HEAD
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
=======
        return self.pub_date >= timezone.now()
    datetime.timedelta(days=1)
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
<<<<<<< HEAD
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
=======
    question = models.ForeignKey(Question,
on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
