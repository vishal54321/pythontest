from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("api/user",views.users,name="userapi"),
    path("api/user/update",views.updateuser,name="userupdate"),
    path("api/user/delete",views.delete,name="delete"),
    path("api/logs",views.logs,name="logs")

]

