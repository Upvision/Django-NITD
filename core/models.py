from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default = True)
    profile_pic = models.ImageField(null=True)

class DegreeLevel(models.Model):
    name = models.CharField(max_length = 200)


class Department(models.Model):
    name = models.CharField(max_length = 200)


class Semester(models.Model):
    number = models.PositiveSmallIntegerField()

class CourseCategory(models.Model):
    name = models.CharField(max_length = 200)


class Course(models.Model):
    department = models.ForeignKey("core.Department", on_delete = models.PROTECT)
    degree = models.ForeignKey("core.DegreeLevel", on_delete = models.PROTECT)

    semester = models.ForeignKey("core.Semester", on_delete = models.PROTECT)
    category = models.ForeignKey("core.CourseCategory", on_delete = models.PROTECT)
    title = models.CharField(max_length = 200)
    credits = models.PositiveSmallIntegerField()
    code = models.CharField(max_length = 6)

class AcademicYear(models.Model):
    start = models.DateField()
    end = models.DateField()

class Enrollment(models.Model):
    semester = models.ForeignKey('core.Semester', on_delete = models.PROTECT)
    academic_year = models.ForeignKey('core.AcademicYear', on_delete = models.PROTECT)

class CourseEnrollment(models.Model):
    enrollment = models.ForeignKey("core.Enrollment", on_delete=models.CASCADE)
    course = models.ForeignKey("core.Course", on_delete=models.CASCADE)

Weekdays_choices = (
    ("Su","Sunday"),
    ("Mo","Monday"),
    ("Tu","Tuesday"),
    ("We","Wednesday"),
    ("Th","Tursday"),
    ("Fr","Friday"),
    ("Sa","Saturday"),
)
class TimeTable(models.Model):
    course_enrollment = models.ForeignKey("core.CourseEnrollment", on_delete = models.CASCADE)
    weekday = models.CharField(max_length = 2, choices = Weekdays_choices)
    start = models.TimeField()
    end = models.TimeField()


class Skill(models.Model):
    name = models.CharField(max_length = 512)

class Language(models.Model):
    name = models.CharField(max_length = 512)





