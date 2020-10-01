from django.contrib import admin
from student import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.WorkExperience)
admin.site.register(models.StudentSkill)
admin.site.register(models.StudentLanguage)
admin.site.register(models.StudentSkillEndorsement)
admin.site.register(models.StudentRecommendation)
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.StudentAttendance)