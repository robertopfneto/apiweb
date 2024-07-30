from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=50, null=False)
  
    class Meta:
        db_table = 'profession'
        

class Person(models.Model):
    name = models.CharField(max_length=15, null=False)
    age = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11, null=False)
    data_nascimento = models.CharField(max_length=10)

    fk_profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True)
   
    class Meta:
        db_table = 'person'
        