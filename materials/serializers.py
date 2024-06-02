from rest_framework import serializers
from materials.models import Course


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lessons.count()

