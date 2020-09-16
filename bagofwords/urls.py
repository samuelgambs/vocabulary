from . views import TextCreateApiView
from django.urls import path

urlpatterns = [
    path('process-text/', TextCreateApiView.as_view(), name='process_text')
]


# from rest_framework import routers
# from . views import TextCreateApiView
# router = routers.SimpleRouter()
# router.register(r'text', TextCreateApiView.as_view())


# urlpatterns = router.urls
