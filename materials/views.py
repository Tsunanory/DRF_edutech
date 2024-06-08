from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.permissions import NotModerator, IsOwnerOrModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), NotModerator()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsOwner()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsOwnerOrModerator()]
        return [IsAuthenticated(), IsOwnerOrModerator()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, NotModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrModerator]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrModerator]
        return [permission() for permission in self.permission_classes]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

