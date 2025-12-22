"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from basic.views import sample,sample1,sampleInfo,dynamicResponse,health,addstudent
from basic.views import addPost,get_all_students,filter_age_gte,filter_age_gte,order_by_name,get_unique_ages,count_students,job1,job2,check,login
from basic.views import signUp,hashed,getAllusers,home,about,welcome,contact,services,projects
from basic2.views import bs2,productById,productBycategory,movivebyid


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path('53r/',sample1),
    path('info/',sampleInfo),
    path("name/",dynamicResponse),
    path('health/',health),
    path('add/',addstudent),
    path('addpost/', addPost),
    path('student/',get_all_students),
    path("gte/",filter_age_gte),
    path("gte1/",filter_age_gte),
    path("order/",order_by_name),
    path("get/",get_unique_ages),
    path("count/",count_students),
    path('job1/',job1),
    path('job2/',job2),
    path('signup/', signUp),
    path('check/',check),
    path('login/',login),
    path('hashed/', hashed),
    path('users/',getAllusers),
    path('home/',home, name='home'),
    path('about/',about,name='about'),
    path('welcome/',welcome,name='welcome'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('projects/', projects, name='projects'),
    path('bs2/',bs2),
    path('product/<int:id>',productById),
    path('product/category/<str:ctg>',productBycategory),
    path('movie/<int:id>',movivebyid),


    
    
]
