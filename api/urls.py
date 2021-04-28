from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('categories/', views.categories),
    path('user/login/', obtain_jwt_token),
    path('products/', views.ProductV.as_view()),
    path('products/subcategory/', views.by_subcat),    
    path('products/orders/', views.OrderV.as_view()),
    path('products/<int:id>/', views.by_category),

    path('products/update/<int:id>/', views.ProductDV.as_view()),
]