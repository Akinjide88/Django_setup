from django.urls import path

urlpatterns = [
    path(
        "home",
        views.home_view,
        name="home_view"
    )
