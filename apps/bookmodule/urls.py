from django.urls import path
from . import views

#task6:
#urlpatterns = [
#    path('', views.index), 
#    path('index2/<int:val1>/', views.index2),
#    path('<int:bookId>', views.viewbook),#task7
#]

#task4-lab4
#urlpatterns = [
#path('', views.index, name= "books.index"),
#path('list_books/', views.list_books, name= "books.list_books"),
#path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
#path('aboutus/', views.aboutus, name="books.aboutus"),
#]

#lab5
urlpatterns = [
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.text_formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
#lab6
    path('search', views.search_view),
#lab7
    path('insert', views.insert_books, name='insert_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
#lab8
    path('lab8/task1', views.lab8_task1),
    path('lab8/task2', views.lab8_task2),
    path('lab8/task3', views.lab8_task3),
    path('lab8/task4', views.lab8_task4),
    path('lab8/task5', views.lab8_task5),
    path('lab8/task7', views.lab8_task7),
#lab9
    path('lab9/task1', views.lab9_task1),
    path('lab9/task2', views.lab9_task2),
    path('lab9/task3', views.lab9_task3),
    path('lab9/task4', views.lab9_task4),
    path('lab9/task5', views.lab9_task5),
    path('lab9/task6', views.lab9_task6),
    ]
