from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo


def index(request):
    # name = request.GET.get('name')
    return render(request, 'todo/index.html')


def create(request):
    if request.method == 'POST':
        Todo.objects.create(content=request.POST['content'])
        return HttpResponse('create!')
    elif request.method == 'GET':
        return render(request, 'todo/create.html')
    else:
        return HttpResponse('Invalid request method', status=405)
