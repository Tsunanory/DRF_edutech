from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson, Subscription

User = get_user_model()


class LessonTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(email='user@example.com', password='password')
        self.owner = User.objects.create_user(email='owner@example.com', password='password')

        self.course = Course.objects.create(name='Test Course', owner=self.owner)

        self.lesson = Lesson.objects.create(name='Test Lesson', course=self.course, owner=self.owner, link='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.owner)
        data = {
            'name': 'New Lesson',
            'course': self.course.id,
            'link': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        }
        response = self.client.post('/lesson/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lessons(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/lesson/{self.lesson.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.lesson.name)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.owner)
        data = {
            'name': 'Updated Lesson',
            'course': self.course.id,
            'link': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        }
        response = self.client.put(f'/lesson/update/{self.lesson.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, 'Updated Lesson')

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(f'/lesson/delete/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())


class SubscriptionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(email='user@example.com', password='password')
        self.owner = User.objects.create_user(email='owner@example.com', password='password')

        self.course = Course.objects.create(name='Test Course', owner=self.owner)

    def test_manage_subscription_add(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'course_id': self.course.id
        }
        response = self.client.post('/manage-subscription/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_manage_subscription_remove(self):
        self.client.force_authenticate(user=self.user)
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            'course_id': self.course.id
        }
        response = self.client.post('/manage-subscription/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
