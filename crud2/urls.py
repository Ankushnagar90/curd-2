from django.urls import path

from . import views

# app_name = 'mysecapp'
urlpatterns = [
    # path('', views.home,name='record'),
    path('', views.UserAddShowView.as_view(),name='addstudent'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(),name='deletedata'),
    path('<int:id>/', views.UserUpdateView.as_view(),name='updatedata'),

]
