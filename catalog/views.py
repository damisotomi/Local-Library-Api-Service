from .models import Book, BookInstance,Author, Genre,Language,Review
from .serializers import BookSerializer,AuthorSerializer,GenreSerializer,LanguageSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset= Book.objects.select_related('author','language').prefetch_related('genre','related_name').all()
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['author','genre','language']
    search_fields=['title','summary']
    ordering_fields=['title']


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.related_name.count()>0:
            return Response({"error":"This book cannot be deleted. It is referenced by one or more copies"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorViewSet(ModelViewSet):
    queryset= Author.objects.all()
    serializer_class=AuthorSerializer

class GenreViewSet(ModelViewSet):
    queryset= Genre.objects.all()
    serializer_class=GenreSerializer

class LanguageViewSet(ModelViewSet):
    queryset= Language.objects.all()
    serializer_class=LanguageSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])
    
