from django.urls import path
from web_quedadas import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # URL de la vista principal
    path('', views.vista_principal, name='vista_principal'),

    # URLs de autenticación
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLs de Quedadas
    path('quedadas/', views.listar_quedadas, name='listar_quedadas'),
    path('quedadas/crear/', views.crear_quedada, name='crear_quedada'),
    path('quedadas/eliminar/<int:quedada_id>/', views.eliminar_quedada, name='eliminar_quedada'),


    # URLs de Usuarios
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),


]
