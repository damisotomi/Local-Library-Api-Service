from cgitb import lookup
from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from pprint import pprint


router=routers.DefaultRouter()
router.register('books',views.Book,basename='books')
router.register('authors',views.Author)
router.register('genre',views.Genre)
router.register('language',views.Language)
pprint(router.urls)

book_router=routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('reviews',views.Review,basename='book-reviews')
pprint(book_router.urls)
urlpatterns=router.urls +book_router.urls