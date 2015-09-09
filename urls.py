from django.conf.urls import include, url


urlpatterns = (
    url(r'', include("physical.urls", namespace='physical')),
)
