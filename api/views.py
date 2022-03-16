from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets, mixins
from reversion.views import RevisionMixin

from .serializers import UserSerializer, DocumentsSerializer
from .models import Document


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class DocumentsView(viewsets.ModelViewSet):
    try:
        queryset = Document.objects.all()
        serializer_class = DocumentsSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    except Exception as e:
        print(e)


class DocumentDetailView(viewsets.ModelViewSet):
    try:
        queryset = Document.history.filter()
        serializer_class = DocumentsSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    except Exception as e:
        print(e)




