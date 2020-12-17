from django.urls import
from .views import *

urlpatterns = [
    path('abc/',MessageList.as_view(),name='msg_list'),
    path('<int:pk>/',MessageDetail.as_view(), name='msg_view'),
    path('create/',MesageCreate.as_view(), name="msg_create"),

]
