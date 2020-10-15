from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField("core.User", on_delete = models.PROTECT)

    full_name = models.CharField(max_length = 512)
    mobile = models.CharField(max_length = 12)
    dob = models.DateField()

    intro = models.CharField(max_length = 512, blank = True, null = True)
    about = models.TextField(blank = True, null = True)
    profile_pic = models.ImageField(blank = True, null = True)

    roll_number = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

Employment_Type_Choices = (
    ("Full-time", "Full-time"),
    ("Part-time", "Part-time"),
    ("Self-Employed", "Self-Employed"),
    ("Freelance", "Freelance"),
    ("Internship", "Internship"),
    ("Trainee", "Trainee"),
)

class WorkExperience(models.Model):
    student = models.ForeignKey("student.Student", on_delete = models.CASCADE)
    title = models.CharField(max_length = 512)
    type = models.CharField(max_length = 15, choices = Employment_Type_Choices)
    company = models.CharField(max_length = 512)
    location = models.CharField(max_length = 512, blank = True, null = True)
    currently_working = models.BooleanField(default = True)
    start_date = models.DateField()
    end_date = models.DateField( blank = True, null = True)
    description = models.TextField()
    link = models.CharField(max_length = 512, blank = True, null = True)
    file = models.FileField(blank = True, null = True)

    date = models.DateField(auto_now_add = True)

class StudentSkill(models.Model):
    student = models.ForeignKey("student.Student", on_delete = models.CASCADE)
    skill = models.ForeignKey("core.Skill", on_delete = models.CASCADE)

class StudentLanguage(models.Model):
    student = models.ForeignKey("student.Student", on_delete = models.CASCADE)
    language = models.ForeignKey("core.Language", on_delete = models.CASCADE)

class StudentSkillEndorsement(models.Model):
    skill = models.ForeignKey("student.StudentSkill", on_delete = models.CASCADE)
    endorsed_by = models.ForeignKey("student.Student", on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)

class StudentRecommendation(models.Model):
    given_by = models.ForeignKey("student.Student", on_delete = models.CASCADE, related_name = "given_by")
    given_to = models.ForeignKey("student.Student", on_delete = models.CASCADE, related_name = "given_to")
    description = models.CharField(max_length = 500)
    date = models.DateField()
    relation = models.CharField(max_length = 256)

class StudentCourseEnrollment(models.Model):
    course_enrollment = models.ForeignKey("core.CourseEnrollment", on_delete = models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete = models.CASCADE)
    date = models.DateField()


class StudentAttendance(models.Model):
    student_course_enrollment = models.ForeignKey("student.StudentCourseEnrollment", on_delete = models.CASCADE)
    date = models.DateField()
    attendance = models.BooleanField(default = True)



