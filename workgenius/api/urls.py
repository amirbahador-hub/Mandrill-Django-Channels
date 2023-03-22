from django.urls import path, include


urlpatterns = [
    path('mandrill/', include(('workgenius.mandrill.urls', 'mandrill'))),
    path('socket/', include(('workgenius.socketapp.urls', 'socket')))
]
