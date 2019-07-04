from django.urls import path
from .views import RegisterView,LoginView,IndexView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('test/', views.test, name='test'),
    path('logout/', views.logout_view, name="logout"),
    path('logout_success/', views.logout_success, name="logout_success"),
    path('store/', views.store_info, name='store'),
    path('store/<int:store_id>', views.store_detail, name="detail"),
    path('goods/', views.goods, name='goods'),
]