from django.urls import path

from config.yasg import schema_view
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.stripe_views import StripeCreateProductView, StripeCreatePriceView, StripeCreateCheckoutSessionView
from materials.views import ManageSubscriptionView, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, CourseListView, CourseViewSet, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('manage-subscription/', ManageSubscriptionView.as_view(), name='manage-subscription'),
    path('courses/', CourseListView.as_view(), name='course-list'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('create-product/', StripeCreateProductView.as_view(), name='create-product'),
    path('create-price/', StripeCreatePriceView.as_view(), name='create-price'),
    path('create-checkout-session/', StripeCreateCheckoutSessionView.as_view(),
                       name='create-checkout-session'),
] + router.urls
