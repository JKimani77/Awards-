from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from awards import views 


urlpatterns  = [
    path('^$', views.index, name='index'),
    # path(r'^profile/$', views.profile, name='create-profile'),
    # path(r'^profile/(\d+)/$', views.profile_user, name='dipslay-profile'),
    # path(r'^postproject/', views.post_project, name = 'postproject'),
    # path(r'^search/', views.search, name='searchbyprojectname'),
    # # path(r'^login/', views.login, name='login'),
    # path(r'^logout/$', views.logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)