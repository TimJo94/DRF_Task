from django.urls import path

from main.views import PostSerializerView

urlpatterns = [
    path('post/', PostSerializerView.as_view())
]