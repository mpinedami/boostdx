from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
