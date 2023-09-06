from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo


def index(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, 'todo/index.html', context)
    else:
        return HttpResponse('Invalid request method', status=405)


def create(request):
    if request.method == 'POST':
        Todo.objects.create(content=request.POST['content'])
        return HttpResponse('create!')
    elif request.method == 'GET':
        return render(request, 'todo/create.html')
    else:
        return HttpResponse('Invalid request method', status=405)


def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/detail.html', context)
