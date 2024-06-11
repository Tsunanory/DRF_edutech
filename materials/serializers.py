from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import YoutubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            YoutubeLinkValidator(field='link'),
            YoutubeLinkValidator(field='description'),
        ]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            YoutubeLinkValidator(field='description')
        ]

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request', None)
        if request:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False