from django.urls import path, include

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
