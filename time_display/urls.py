from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.time_app.urls')),
    url(r'^', include('apps.random_word.urls')),
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
