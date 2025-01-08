from django.urls import path, include
from rest_framework import routers
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/',views.JavobgarList.as_view()),
    path('users/<int:pk>/', views.JavobgarDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)