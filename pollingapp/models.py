from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    class Meta:
        db_table = 'Question'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = 'Choice'

        


