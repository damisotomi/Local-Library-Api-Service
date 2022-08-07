from . import views
from rest_framework.routers import DefaultRouter
from pprint import pprint


router=DefaultRouter()
router.register('books',views.Book)
router.register('authors',views.Author)
router.register('genre',views.Genre)
router.register('language',views.Language)

urlpatterns=router.urls