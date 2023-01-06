import uuid
from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    """This model stores info about the different genre categories that are availa
    ble for all books eg science fiction, drama etc"""
    name=models.CharField(max_length=255,help_text="Enter a book genre(e.g, Science Fiction)")

    def __str__(self):
        """string for representing the Model Object(in admin site)"""
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=255, help_text='Enter the books natural language eg English, French etc')

    def __str__(self):
        '''String for representing the model object in the admin site'''
        return self.name


class Book(models.Model):
    '''This model stores info about the books available in the library. Not a specific copy of a book'''
    title=models.CharField(max_length=255)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True,related_name="related_name")
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    summary=models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn= models.CharField('ISBN',max_length=13,unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre,help_text='Select a Genre for this book')
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language=models.ForeignKey(Language, on_delete=models.SET_NULL, null=True,related_name='language')
    # Foreign Key used because book can only have one language, but a langauge can be used to write many books

    def display_genre(self):
        '''Create a string for the genre. This is required to display genre in Admin'''
        return ','.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description='Genre'


    class Meta:
        ordering=['title','author']

    def __str__(self):
        '''String for representing the model object'''
        return self.title

    def get_absolute_url(self):
        '''Returns the Url  to access a detail record for this book'''
        return  reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    '''This model represents a specific copy of a book that someone might borrow and includes information
    about whether the copy is available or on what date it is expected back'''
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, help_text='Unique ID FOR THIS PARTICULAR BOOK ACROSSS WHOLE LIBRARY')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT,related_name="related_name")
    imprint = models.CharField(max_length=255, help_text='Version details', default='v2')
    due_back=models.DateField(null=True, blank=True)

    LOAN_STATUS=(
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status=models.CharField(max_length=1,choices=LOAN_STATUS,blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering=['due_back']

    def __str__(self):
        ''' String for representin the model object in admin site'''
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    '''Model representing an author'''
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    date_of_birth=models.DateField(null=True, blank=True)
    date_of_death=models.DateField('Died', null=True, blank=True)


    class Meta:
        ordering=['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])


    def __str__(self):
        '''String for representing the model object'''
        return f'{self.last_name},{self.first_name}'



class Review(models.Model):
    name=models.CharField(max_length=255)
    date_of_review=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')

