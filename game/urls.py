from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.FamilyViewSet)



urlpatterns = [
    path('',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    path('family',views.family, name='family'),
    path('royal/<slug>',views.royal_family, name='royal'),
    path('family_detials/<slug>', views.family_details, name='family_details'),
    path('page/<slug>',views.page, name='page'),
    path('popular/<slug>', views.popular_page, name='popular'),   
    path('api/', include(router.urls)),
    path('news_api', views.news_api, name='news_api')
]