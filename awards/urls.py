from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from awards import views 
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns  = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='createprofile'),
    path('profile/<int:id>/', views.profile_user, name='profiley'),
    path('api/proj/', views.ProjectsList.as_view()),
    # path('api/proj/<int:id>/', views.ProjectsDescription.as_view()),
    path('post/', views.post, name = 'postproject'),
    path('search/', views.search, name='searchbyprojectname'),
    path('ratingform/<int:id>/',views.rate, name='ratingz'),
    path('rate/<int:id>',views.rated,name='rated'),
    #https://overflow.io/ 
    #https://www.abbeyroad.com/about-us
    #https://www.swiss.com/worldofswiss/en
    #https://www.virgin.com/
    #https://www.franshalsmuseum.nl/en/

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)