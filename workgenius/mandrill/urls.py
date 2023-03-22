from django.urls import path
from .apis import WebhookApi, EventList


urlpatterns = [
    path('hook/', WebhookApi.as_view(),name="hook"),
    path('events/', EventList.as_view(),name="events"),
]
