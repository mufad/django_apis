from django.http import HttpResponse 
from .models import Post

def index(request):
#connect to DB
	all_posts = Post.objects.all()

	html = ''

	for post in all_posts:
		url = '/posts/'+ str(post.id)

		html +=  '<a href ="'+url+'">'+post.title+'</a><br>'	

	return HttpResponse(html)


def post_details(request, post_id):
	return HttpResponse("<h2>Post Details will be here with id:"+str(post_id)+"</h2>")
