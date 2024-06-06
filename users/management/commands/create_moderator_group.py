from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from materials.models import Lesson, Course  # Adjust the import according to your models


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Moderators')

        lesson_content_type = ContentType.objects.get_for_model(Lesson)
        course_content_type = ContentType.objects.get_for_model(Course)

        permissions = Permission.objects.filter(content_type__in=[lesson_content_type, course_content_type],
                                                codename__in=['view_lesson', 'change_lesson', 'view_course',
                                                              'change_course'])

        group.permissions.set(permissions)