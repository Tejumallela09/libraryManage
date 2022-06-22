from django.db import models

# Create your models here.
class College_clubs(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
class Books(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Courses(models.Model):
    name=models.CharField(max_length=128)
    dept_name=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    def __unicode__(self):
        return self.name,self.dept_name


class Student(models.Model):
    stu_id = models.CharField( max_length=12,primary_key=True)
    name = models.CharField(max_length=128)
    mobile=models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128 )
    clubs = models.ManyToManyField(College_clubs)
    # books = models.OneToOneField(Books,on_delete=models.SET_NULL,null=True)
    dept_name=models.OneToOneField(Department,on_delete=models.SET_NULL,null=True)
    course=models.ManyToManyField(Courses)
    def __unicode__(self):
        return self.name
    # fees=models.CharField(max_length=20)
class Instructor(models.Model):
    emp_id = models.CharField( max_length=12,primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=128 )
    salary = models.CharField(max_length=28)
    dept_name = models.ManyToManyField(Department)
    course = models.ManyToManyField(Courses)
    def __unicode__(self):
        return self.name
class Books_borrowed(models.Model):
    st_id = models.OneToOneField(Student,on_delete=models.CASCADE)
    books = models.ForeignKey(Books,on_delete=models.SET_NULL,null=True,related_name='borrowedbooks')
    def __unicode__(self):
        return self.books

