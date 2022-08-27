from .models import Book, BookInstance,Author, Genre,Language
from .serializers import BookSerializer,AuthorSerializer,GenreSerializer,LanguageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class Book(ModelViewSet):
    queryset= Book.objects.select_related('author','language').prefetch_related('genre','related_name').all()
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=['author','genre','language']
    search_fields=['title','summary']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.related_name.count()>0:
            return Response({"error":"This book cannot be deleted. It is referenced by one or more copies"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

class Author(ModelViewSet):
    queryset= Author.objects.all()
    serializer_class=AuthorSerializer

class Genre(ModelViewSet):
    queryset= Genre.objects.all()
    serializer_class=GenreSerializer

class Language(ModelViewSet):
    queryset= Language.objects.all()
    serializer_class=LanguageSerializer

