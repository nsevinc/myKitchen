"""myKitchenProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from myKitchen import views


app_name = 'myKitchen'
urlpatterns = [
    path('', views.index),
    path('stocks/', views.index),
    path('shoppinglist/', views.index),
    path('recipes/', views.index),
    
    path('locations/', views.locations_view),
    path('locations/new', views.locations_new_view),
    path('locations/view', views.locations_view),
    path('locations/<int:pk>/edit', views.locations_edit_view.as_view(), name='editlocations'),  
    path('locations/locations_delete/<int:pk>',views.locations_delete_post,name='locations_delete'),
    
    path('qunits/', views.qunits_view),    
    path('qunits/new', views.qunits_new_view),    
    path('qunits/<int:pk>/edit', views.qunits_edit_view.as_view(), name='editqunits'),  
    path('qunits/qunits_delete/<int:pk>',views.qunits_delete_post,name='qunits_delete'),
    
    
    path('materialgroups/', views.material_groups_view),    
    path('materialgroups/new', views.material_groups_new_view),    
    path('materialgroups/<int:pk>/edit', views.material_groups_edit_view.as_view(), name='editmaterialgroups'),  
    path('materialgroups/material_groups_delete/<int:pk>',views.material_groups_delete_post,name='materialgroups_delete'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

