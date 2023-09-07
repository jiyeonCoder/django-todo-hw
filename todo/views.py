from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='/user/login/')
def create(request):
    if request.method == 'POST':
        Todo.objects.create(
            content=request.POST['content'], user=request.user)
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
        if request.user == todo.user:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return redirect('/todo/')
        else:
            return HttpResponse('You are not allowed to delete this todo', status=403)
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
        if request.user == todo.user:
            todo = Todo.objects.get(id=todo_id)
            todo.content = request.POST['content']
            todo.save()
            return redirect(f'/todo/{todo_id}/')
        else:
            return HttpResponse('You are not allowed to update this todo', status=403)
    else:
        return HttpResponse('Invalid request method', status=405)


def isdone(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.is_done = request.POST['is_done']
        return redirect('/todo/')
    elif request.method == 'GET':
        return render(request, 'todo/create.html')
    else:
        return HttpResponse('Invalid request method', status=405)
