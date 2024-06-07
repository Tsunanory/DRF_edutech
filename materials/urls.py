from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter
from materials.views import LessonListCreateAPIView, CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, \
    LessonRetrieveUpdateDestroyAPIView
from users.views import PaymentListAPIView, CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonListCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListCreateAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/update/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls
