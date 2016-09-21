from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		'courses' : Course.objects.all()
	}
	return render(request, 'courses/index.html', context)

def create(request):
	Course.objects.create(name=request.POST['course_name'], description=request.POST['course_description'])
	return redirect('/')

def delete(request, id):
	course_to_delete = Course.objects.get(id=id)
	if request.method == "GET":
		return render(request, 'courses/course_delete.html', {'course' : course_to_delete})
	course_to_delete.delete()
	return redirect('/')