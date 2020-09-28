

from django.contrib import admin
from django.urls import include, path
from trip.views import hello_world, home ,post_detail
import re

urlpatterns = [
    
    path('trip/' , include('trip.urls')),
    path('admin/', admin.site.urls),
    path('' , home ,name='Fuck uou') , #空白於是默認為主頁
    path(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]

