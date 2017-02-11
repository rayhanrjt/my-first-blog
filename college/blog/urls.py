from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
  url(r'^post/slist/$', views.studentlist, name='studentlist'),
url(r'^post/list/$', views.post_list, name='post_list'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^scholarship/$', views.scholarship, name='scholarship'),
url(r'^course/$', views.course, name='course'),
url(r'^gallery/$', views.gallery, name='gallery'),
url(r'^blog/$', views.blog, name='blog'),
url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),

]
