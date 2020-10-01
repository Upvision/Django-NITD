from django.contrib import admin
from core import models
# Register your models here.


admin.site.register(models.User)
admin.site.register(models.DegreeLevel)
admin.site.register(models.Department)
admin.site.register(models.Semester)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.AcademicYear)
admin.site.register(models.Enrollment)
admin.site.register(models.CourseEnrollment)
admin.site.register(models.TimeTable)
admin.site.register(models.Skill)
admin.site.register(models.Language)