"""farmcon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import single_product, search, home_view
from orders.views import checkout, orders
from accounts.views import (logout_view, login_view, 
                            register_view, farmer_view, 
                            buyer_view, verify_number, send_code,
                            update_profile,user_profile, email_sent,
                            activate_email)

urlpatterns = [
    path('admin/', admin.site.urls), #admin view

    #views from products app
    path('', home_view, name='home'),
    path('product/<str:slug>/', single_product, name='single_product'),
    path('s/', search, name='search'),

    #views from order app
    path('orders/', orders, name='user_orders'),
    path('checkout/', checkout, name='checkout'),

    #views from account app
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('farmer/', farmer_view, name='farmer'),
    path('buyer/', buyer_view, name='buyer'),
    path('verify/', verify_number, name='verify_number'),
    path('send_code/', send_code, name='send_code'),
    path('update/', update_profile, name='update_profile'),
    path('profile/', user_profile, name='user_profile'),
    path('email_sent/', email_sent, name='email_sent'),
    path('activate_email/<uidb64>/<token>/', activate_email, name='activate_email'),


    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
     name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
