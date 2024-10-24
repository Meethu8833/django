"""
URL configuration for project1 project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("fun1",views.fun1),
    path("fun2",views.fun2),
    path('fun3',views.fun3),
    path('fun4',views.fun4),
    path('fun5',views.fun5),
    path('fun6',views.fun6),
    path('fun7',views.fun7),
    path('fun8',views.fun8),
    path('fun9',views.fun9),
    path('fun10',views.fun10),
    path('fun11',views.fun11),
    path('fun12',views.fun12,name='fun11'),
    path('fun13',views.fun13),
    path('fun14',views.fun14,name='product_table'),
    path('fun15/<int:id>',views.fun15,name='delete'),
    path('fun16/<int:id>',views.fun16,name='update'),
    path('cus_add',views.cus_add),
    path('cus_display',views.cus_display,name='display_customer'),
    path('cus_update/<int:id>',views.cus_update,name='update_customer'),
    path('cus_delete/<int:email>',views.cus_delete,name='delete_customer'),
    path('blog_add',views.blog_add),
    path('blog_display',views.blog_display,name='blog_display'),
    path('blog_update/<int:id>',views.blog_update,name='update_blog'),
    path('product_table',views.product_table),
    path('add_productForUser',views.add_productForUser),
    path('publisher_table',views.publisher_table,name='publisher_table'),
    path('publisher_book',views.publisher_book,name='publisher_book'),
    path('add_publisher_book',views.add_publisher_book),
    path('delete_publisher/<int:id>',views.delete_publisher,name='delete_publisher'),
    path('update_publisherr/<int:id>',views.update_publisherr,name='update_publisherr'),
    path('update_book_publisher/<int:id>',views.update_book_publisher,name='update_book'),
    path('delete_book_publisher/<int:id>',views.delete_book_publisher,name="delete_book"),

    path('displayCourses',views.displayCourses,name='displayCourses'),
    path('addStudent',views.addStudent),
    path('displayStudents',views.displayStudents,name='displayStudents'),
    path('displaySpecificStudent/<int:id>',views.displaySpecificStudent,name='dss'),
    path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),
    path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),
    path('display_specific_course/<int:id>',views.specificCourse,name='dsc'),

    path('add_organizer',views.add_organizer),
    path('add_event',views.add_event),
    path('display_organizer',views.display_organizer,name='display_organizer'),
    path('display_event',views.display_event,name='display_event'),
    path('update_organizer/<int:id>',views.update_organizer,name='update_organizer'),
    path('update_event/<int:id>',views.update_event,name='update_event'),
    path('delete_organizer/<int:id>',views.delete_organizer,name='delete_organizer'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),

]
