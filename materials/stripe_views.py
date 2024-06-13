import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from materials.models import Course

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCreateProductView(APIView):
    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        if not course_id:
            return Response({"error": "course_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = stripe.Product.create(
                name=course.name,
                description=course.description,
                images=[request.build_absolute_uri(course.preview.url)] if course.preview else None,
            )
            return Response({"product_id": product.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class StripeCreatePriceView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        unit_amount = request.data.get('unit_amount')  # In cents

        try:
            price = stripe.Price.create(
                product=product_id,
                unit_amount=unit_amount,
                currency='usd',
            )
            return Response({"price_id": price.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class StripeCreateCheckoutSessionView(APIView):
    def post(self, request, *args, **kwargs):
        price_id = request.data.get('price_id')
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri('/cancel/'),
            )
            return Response({"session_id": checkout_session.id, "checkout_url": checkout_session.url}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)