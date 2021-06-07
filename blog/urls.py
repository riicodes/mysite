from django.urls import path
from . import views
from .views import PostList

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
]
