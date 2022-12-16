from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'base', views.base, name='base'),
    url(r'post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url('post/new/', views.post_new, name='post_new'),
    url('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]