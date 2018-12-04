from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('detail/<int:pk>', views.news_detail, name="new_detail"),
    path('filter/<int:pk>', views.news_filter, name="new_filter"),
]