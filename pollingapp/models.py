from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self) -> str:
        return self.question_text
    
    class Meta:
        db_table = 'Question'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
    class Meta:
        db_table = 'Choice'




