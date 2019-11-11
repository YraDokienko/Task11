from django.shortcuts import render_to_response, render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import TypeGroupModel


def get_choice(request):
    return render(request, 'base.html', )


class ModelView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'data': TypeGroupModel.objects.all()
        }
        return render_to_response('view.html', context)


class ModelViewTemplate(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super(ModelViewTemplate, self).get_context_data(**kwargs)
        context['data'] = TypeGroupModel.objects.all()
        return context


class ModelsViewList(ListView):
    model = TypeGroupModel
    template_name = 'view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TypeGroupModel.objects.all()
        return context
