from django.contrib import admin
from .models import Language, Book, BookInstance, Author, Genre
# Register your models here.

admin.site.site_header ='Local Library Admin'
admin.site.index_title='Admin'

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra=0

class BookInline(admin.TabularInline):
    model=Book
    extra=0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','display_genre','number_of_copies']
    inlines = [BookInstanceInline]

    def number_of_copies(self,book:Book):
        return book.related_name.count()


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','author','status','due_back')
    list_filter = ('status','due_back','book')
    fieldsets = (
        (None,{'fields':('book','imprint','id')}),
        ('Avaialability',{'fields':('status','due_back')})
    )

    def author(self,bookinstance:BookInstance):
        return bookinstance.book.author
    
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('full_name', 'date_of_birth', 'number_of_books')
    fields = ['first_name', 'last_name',('date_of_birth','date_of_death')]
    inlines = [BookInline]

    def full_name(self,author:Author):
        return author.last_name, author.first_name

    def number_of_books(self,author:Author):
        return author.related_name.count()



admin.site.register(Book,BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance,BookInstanceAdmin)


