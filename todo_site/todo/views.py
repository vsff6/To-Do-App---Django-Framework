
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################


def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')



from django.shortcuts import get_object_or_404
from .models import Todo
from .forms import TaskProgressForm
from django.http import HttpResponseRedirect

from django.http import JsonResponse

def update_task_progress(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Todo, id=task_id)
        form = TaskProgressForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # Retorna uma resposta JSON indicando sucesso
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #return JsonResponse({"success": True, "message": "Progresso atualizado com sucesso."})
        else:
            # Retorna uma resposta JSON indicando falha na validação do formulário
            return JsonResponse({"success": False, "message": form.errors.as_json()})
    # Para métodos não-POST, você pode decidir retornar um erro ou simplesmente redirecionar
    return JsonResponse({"success": False, "message": "Método inválido."})
