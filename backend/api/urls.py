from django.urls import path
from .views import ProcessPlaylistURL, ProcessVideoURL


urlpatterns = [
    path('processPlaylistURL/', ProcessPlaylistURL.as_view(), name="process-url"),
    path('processVideoURL/', ProcessVideoURL.as_view(), name="process-url"),
]

