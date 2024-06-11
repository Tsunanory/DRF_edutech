from rest_framework import serializers
from materials.models import Course, Lesson
from materials.validators import YoutubeLinkValidator


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            YoutubeLinkValidator(field='link'),
            YoutubeLinkValidator(field='description'),
        ]


class CourseCreateSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            YoutubeLinkValidator(field='description')
        ]

    def get_lesson_count(self, obj):
        return obj.lessons.count()
