from django.contrib import admin
from django.urls import path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure_name>/', DepartureView.as_view(), name="departure_view"),
    path('tour/<int:id>/', TourView.as_view(), name="tour_view"),
    path('admin/', admin.site.urls),
]