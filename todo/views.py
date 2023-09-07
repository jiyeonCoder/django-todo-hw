from django.shortcuts import redirect, render
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
        Todo.objects.create(content=request.POST['content'], user=request.user)
        return redirect('/todo/')
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


def delete(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('/todo/')
    else:
        return HttpResponse('Invalid request method', status=405)


def update(request, todo_id):
    if request.method == 'GET':
        todo = Todo.objects.get(id=todo_id)
        context = {
            'todo': todo,
        }
        return render(request, 'todo/update.html', context)
    elif request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.content = request.POST['content']
        todo.save()
        return redirect(f'/todo/{todo_id}/')
    else:
        return HttpResponse('Invalid request method', status=405)
