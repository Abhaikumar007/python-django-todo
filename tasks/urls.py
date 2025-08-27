from django.urls import path #type: ignore
from . import views 

urlpatterns=[
    path('',views.list_items,name="list"),
    path('create',views.create_items,name="create"),
    path('complete/<int:task_id>',views.complete_task,name="complete"),
    path('delete/<int:task_id>/',views.delete_task,name="delete"),

]