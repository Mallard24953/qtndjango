from django.db import router
from django.urls import path
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('api/paper', views.PaperView)
router.register('api/contactor', snippet_list.as_view())

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
]
urlpatterns += router.urls