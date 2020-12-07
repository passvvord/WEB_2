from django.urls import path
from . import views

app_name = 'tours'
urlpatterns = [
	path('',views.start, name = 'start'),
	path('tour_list',views.tour_list_view, name = 'tour_list_view'),
	path('tour_list/<int:tour_id>',views.tour_view, name = 'tour_view'),
	path('tour_list/<int:tour_id>/add_person',views.add_person, name = 'add_person'),
	path('register',views.register_view, name = 'register_view'),
	path('register/create_person',views.create_person, name = 'create_person'),
	path('log_in',views.log_in_view, name = 'log_in_view'),
	path('log_in/check',views.log_in, name = 'log_in'),
	path('log_out',views.log_out, name = 'log_out'),
]