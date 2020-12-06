from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Tour,Tour_event,Person

# http://127.0.0.1:8000
def start(request):
	return HttpResponseRedirect(reverse('tours:tour_list_view'))

# http://127.0.0.1:8000/tour_list
def tour_list_view(request):
	tour_list = Tour.objects.order_by('difficulty')
	try:
		a = Person.objects.get(id = request.session.get('PersonID'))
		return render(request, 'tours/tours_list.html', {'tour_list': tour_list,'login':a})
	except:
		pass

	return render(request, 'tours/tours_list.html', {'tour_list': tour_list})

# http://127.0.0.1:8000/tour_list/<int:tour_id>
def tour_view(request, tour_id):
	try:
		a = Tour.objects.get(id = tour_id)
	except:
		raise Http404('Виникла помилка, походу з таким id не має)')

	try:
		b = Person.objects.get(id = request.session['PersonID'])
		return render(request, 'tours/tour.html', {'tour': a,'login': b})
	except:
		pass

	return render(request, 'tours/tour.html', {'tour': a})

# http://127.0.0.1:8000/tour_list/<int:tour_id>/add_person
# def add_person(request, tour_id):
# 	return

# http://127.0.0.1:8000/register
def register_view(request):
	return render(request, 'accounts/register.html')

# http://127.0.0.1:8000/register/create_person
def create_person(request):
	a = Person(
		nickname  = request.GET['nickname' ],
		password  = request.GET['password' ], 
		name      = request.GET['name'     ],
		age       = request.GET['age'      ],
		phone     = request.GET['phone'    ],
		email     = request.GET['email'    ],
		condition = request.GET['condition'],
	)

	a.save()
	request.session['PersonID'] = a.id

	return HttpResponseRedirect(reverse('tours:tour_list_view'))

# http://127.0.0.1:8000/log_in
def log_in_view(request):
	return render(request, 'accounts/log_in.html')

# http://127.0.0.1:8000/log_in/check
def log_in(request):
	try:
		m = Person.objects.get(nickname=request.GET['nickname'])
		if m.password == request.GET['password']:
			request.session['PersonID'] = m.id
			return HttpResponseRedirect(reverse('tours:tour_list_view'))
		else:
			return Http404('Такого Акаунту з таким паролем не існує')
	except:
		raise Http404('Такого Акаунту з таким паролем не існує')
	# return render(request, 'accounts/log_in.html')

# http://127.0.0.1:8000/log_out
def log_out(request):
	try:
		del request.session['PersonID']
	except:
		pass
	return HttpResponseRedirect(reverse('tours:tour_list_view'))


