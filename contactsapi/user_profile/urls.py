from django.urls import path
from .views import UserList, UserListDetailView


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:id>', UserListDetailView.as_view()),

]