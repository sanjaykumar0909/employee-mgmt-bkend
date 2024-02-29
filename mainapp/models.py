from django.db import models
class Employees(models.Model):
    emp_id= models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50)
    department= models.CharField(max_length=15)
    dob= models.DateField()
    gender=models.CharField()
    designation= models.CharField(max_length=20)
    salary= models.IntegerField()
    join_date= models.DateField()

