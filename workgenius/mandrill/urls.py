from django.urls import path
from .apis import WebhookApi 


urlpatterns = [
    path('hook/', WebhookApi.as_view(),name="hook"),
]
