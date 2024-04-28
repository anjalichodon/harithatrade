"""HarithaTraders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.login),
    path('login_post', views.login_post),
    path('admin_home', views.admin_home),
    path('add_category', views.add_category),
    path('add_category_post', views.add_category_post),
    path('view_category', views.view_category),
    path('edit_category/<id>', views.edit_category),
    path('edit_category_post/<id>', views.edit_category_post),
    path('delete_category/<id>',views.delete_category),
    path('add_subcategory',views.add_subcategory),
    path('add_subcategory_post',views.add_subcategory_post),
    path('view_subcategory',views.view_subcategory),
    path('edit_subcategory/<id>',views.edit_subcategory),
    path('edit_subcategory_post/<id>',views.edit_subcategory_post),
    path('delete_subcategory/<id>',views.delete_subcategory),
    path('add_product', views.add_product),
    path('add_product_post', views.add_product_post),
    path('view_product', views.view_product),
    path('edit_product/<id>',views.edit_product),
    path('edit_product_post/<id>',views.edit_product_post),
    path('delete_product_post/<id>',views.delete_product_post),
    path('add_stock/<id>',views.add_stock),
    path('add_stock_post/<id>',views.add_stock_post),
    path('view_stock/<id>',views.view_stock),
    path('edit_stock/<id>',views.edit_stock),
    path('edit_stock_post/<id>',views.edit_stock_post),
    path('delete_stock/<id>',views.delete_stock),
    path('add_staff',views.add_staff),
    path('add_staff_post',views.add_staff_post),
    path('view_staff',views.view_staff),
    path('edit_staff/<id>',views. edit_staff),
    path('edit_staff_post/<id>',views. edit_staff_post),
    path('delete_staff_post',views.delete_staff_post),
    path('view_complaint',views.view_complaint),
    path('sent_reply/<id>',views.sent_reply),
    path('sent_reply_post/<id>',views.sent_reply_post),
    path('view_rating',views.view_rating),
    path('view_order',views.view_order),
    path('add_employe', views.add_employe),
    path('add_employe_post', views.add_employe_post),
    path('view_employe', views.view_employe),
    path('edit_employe/<id>', views.edit_employe),
    path('edit_employe_post/<id>', views.edit_employe_post),
    path('delete_employe_post', views.delete_employe_post),
    path('logout', views.logout),
    path('view_order_by_date', views.view_order_by_date),
    path('forgot_password', views.forgot_password),
    path('forgot_password_post', views.forgot_password_post),


# ================================Android=========================================================================================

    path('andro_log',views.andro_log),
    path('andro_register',views.andro_register),
    path('andro_view_category',views.andro_view_category),
    path('andro_view_subcategory',views.andro_view_subcategory),
    path('andro_view_product',views.andro_view_product),
    path('andro_add_rate',views.andro_add_rate),
    path('andro_send_complaint',views.andro_send_complaint),
    path('adro_view_complaint',views.adro_view_complaint),
    path('andro_place_order',views.andro_place_order),
    path('andro_add_to_cart',views.andro_add_to_cart),
    path('andro_cartview',views.andro_cartview),
    path('andro_delete',views.andro_delete),
    path('andro_update_order',views.andro_update_order),
    path('andro_view_approved_orders',views.andro_view_approved_orders),
    path('andro_offline',views.andro_offline),
    path('andro_view_order_history',views.andro_view_order_history),
    path('android_online_payment',views.android_online_payment),
    path('andro_payoffline',views.andro_payoffline),
    path('andro_view_delivery_status',views.andro_view_delivery_status),

# =====================staff===============================================================================================
    path('staff_home',views.staff_home),
    path('staff_view_stock',views.staff_view_stock),
    path('staff_view_orders',views.staff_view_orders),
    path('staff_view_employee/<id>',views.staff_view_employee),
    path('allocate_employee/<id>',views.allocate_employee),
    path('view_customers',views.view_customers),
    path('staff_changepassword',views.staff_changepassword),
    path('staff_changepassword_post',views.staff_changepassword_post),
    path('staff_view_profile',views.staff_view_profile),

# ======================deliveryboy====================================================================================================
    path('deliverey_home',views.deliverey_home),
    path('view_allocation',views.view_allocation),
    path('deliver_view_product/<id>',views.deliver_view_product),
    path('update_delivery_status/<id>',views.update_delivery_status),
    path('update_delivery_status_post/<id>',views.update_delivery_status_post),
    path('deli_changepassword',views.deli_changepassword),
    path('deli_changepassword_post',views.deli_changepassword_post),


]
