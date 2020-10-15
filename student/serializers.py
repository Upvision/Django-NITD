
from student import models
from rest_framework import routers, serializers, viewsets


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    work_experience = serializers.SerializerMethodField(read_only=True)
    student_skills = serializers.SerializerMethodField(read_only=True)
    student_languages = serializers.SerializerMethodField(read_only=True)
    student_recommendations_given = serializers.SerializerMethodField(read_only=True)
    student_recommendations = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Student
        fields = "__all__"

    def get_work_experience(self, obj):
        work_experience = models.WorkExperience.objects.filter(student = obj)
        data = WorkExperienceSerializer(work_experience, many=True).data
        return data

    def get_student_skills(self, obj):
        student_skills = models.StudentSkill.objects.filter(student = obj)
        data = StudentSkillSerializer(student_skills, many=True).data
        return data

    def get_student_languages(self, obj):
        student_languages = models.StudentLanguage.objects.filter(student = obj)
        data = StudentLanguageSerializer(student_languages, many=True).data
        return data

    def get_student_recommendations_given(self, obj):
        student_recommendations_given = models.StudentRecommendation.objects.filter(given_by = obj)
        data = StudentRecommendation(student_recommendations_given, many=True).data
        return data

    def get_student_recommendations(self, obj):
        student_recommendations = models.StudentRecommendation.objects.filter(given_to = obj)
        data = StudentRecommendation(student_recommendations, many=True).data
        return data


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = "__all__"


class StudentSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = "__all__"



class StudentLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = "__all__"


class StudentSkillEndorsementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = "__all__"


class StudentRecommendation(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = "__all__"

