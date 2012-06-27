from django.db import models

# Create your models here.
class Student(models.Model):
    studentID = models.IntegerField()    
    last_name = models.TextField()
    first_name = models.TextField()
    middle_initial = models.TextField()    
    year = models.IntegerField()
    sex = models.TextField()
    course = models.TextField()
    section = models.TextField()
    
    class Meta:
        db_table = 'student'

    def __unicode__(self):
        return unicode(self.studentID)

class Event(models.Model):
    name = models.TextField()
    date = models.DateField()

    class Meta:
        db_table = 'event'

    def __unicode__(self):
        return unicode(self.name)

class Attend(models.Model):
    time = models.DateTimeField()
    student = models.ForeignKey(Student)
    event = models.ForeignKey(Event)

    class Meta:
        db_table = 'attend'    
