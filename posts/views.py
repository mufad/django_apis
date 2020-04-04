from django.http import HttpResponse 

def index(request):
	return HttpResponse("<h3>Content Will Be Here</h3>")