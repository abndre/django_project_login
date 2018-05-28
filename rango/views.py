from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse("Rango here")
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)