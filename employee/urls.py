from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("allemployees/", views.allemployees, name="allemployees"),
    path("singleemployee/<int:empid>", views.singleemployee, name="singleemployee"),
    path("addemployee/", views.addemployee, name="addemployee"),
    path("updateemployee/<int:empid>", views.updateemployee, name="updateemployee"),
    path("deleteemployee/<int:empid>", views.deleteemployee, name="deleteemployee"),
]
