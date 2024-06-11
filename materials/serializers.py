from rest_framework import serializers
from materials.models import Course, Lesson
from materials.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['owner']

    def validate_description(self, value):
        validate_youtube_link(value)
        return value


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['owner']

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def validate_description(self, value):
        validate_youtube_link(value)
        return value

