from . import models
from rest_framework import serializers
from django.db.models import F


class SimpleGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Genre
        fields=['id','name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Book
        fields=['id','title','author','summary','isbn','genre','language','total_copies','available_copies','onLoan_copies']

    # author=serializers.StringRelatedField()
    # genre=serializers.SerializerMethodField('genre_name')
    # genre=SimpleGenreSerializer()
    # language=serializers.StringRelatedField()
    total_copies=serializers.SerializerMethodField('copies_count')
    available_copies=serializers.SerializerMethodField('available_copies_count')
    onLoan_copies=serializers.SerializerMethodField('onloan_copies_count')

    def available_copies_count(self,book:models.Book):
        return models.BookInstance.objects.filter(book_id=book.id,status='a').count()

    def onloan_copies_count(self,book:models.Book):
        return models.BookInstance.objects.filter(book_id=book.id,status='o').count()

    def copies_count(self,book:models.Book):
        return book.related_name.count()

    def genre_name(self,book:models.Book):
        return ','.join(genre.name for genre in book.genre.all())


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['id','first_name','last_name','date_of_birth','date_of_death','number_of_books']

    number_of_books=serializers.SerializerMethodField('books_count')


    def books_count(self,author:models.Author):
        return author.related_name.count()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Genre
        fields=['id','name','number_of_books']

    number_of_books=serializers.SerializerMethodField('book_count')

    def book_count(self,genre:models.Genre):
        return genre.book_set.count()


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Language
        fields=['id','name','number_of_books']

    number_of_books=serializers.SerializerMethodField('book_count')

    def book_count(self,language:models.Language):
        return language.language.count()
        # return models.Book.objects.filter(language_id=language.id).count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Review
        fields=['id','name','description']

    def create(self, validated_data):
        book_id=self.context['book_id']
        return models.Review.objects.create(book_id=book_id,**validated_data)