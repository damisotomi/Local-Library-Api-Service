from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from pprint import pprint


router=routers.DefaultRouter()
router.register('books',views.BookViewSet,basename='books')
router.register('authors',views.AuthorViewSet,basename='authors')
router.register('genre',views.GenreViewSet,basename='genre')
router.register('language',views.LanguageViewSet,basename='language')
# pprint(router.urls)

book_router=routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('reviews',views.ReviewViewSet,basename='book-reviews')
# pprint(book_router.urls)
urlpatterns=router.urls +book_router.urls