from django.urls import path

from angel import views

app_name = 'angel'

urlpatterns = [
    path('', views.home, name='home'),
    path('angel/search/', views.search, name='search'),
    path('angel/category/<int:category_id>/',
         views.category, name='category'),
    path('angel/<int:id>/', views.piece, name='piece'),
]
