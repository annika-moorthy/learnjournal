from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, ListView

from journal.models import Resources
from journal.forms import ResourceForm


# this method will be the homepage, which will contain the search bar & filters
def home(request):
    # a list of all resources pulled from the database
    resources = Resources.objects.all()
    template = loader.get_template('home.html')
    context = {
        "resources": resources,
    }

    return HttpResponse(template.render(context, request))


def delete_resource(request, resources_id):
    resources = Resources.objects.get(pk=resources_id).delete()
    return redirect('index')


# def add_resource(request):
#     resources = Resources.objects.all()
#     if request.POST:
#         resource_form = ResourceForm(request.POST)
#         if resource_form.is_valid():
#             resource = resource_form.save(commit=False)
#             resource.save()
#             return redirect('index')
#     else:
#         resource_form = ResourceForm()
#     template = loader.get_template('home.html')
#     context = {
#         "resources": resources,
#         "resource_form": resource_form
#     }
#     return HttpResponse(template.render(context, request))


# the resource_create page to create a new resource
class ResourceCreate(CreateView):
    model = Resources
    template_name = 'add_resource.html'
    fields = ['name', 'description_name', 'url', 'topic']

    def get_queryset(self):
        return render(Resources.new_fields, {'form': ResourceForm})

    def get_success_url(self):
        return reverse('index')


class SearchView(ListView):
    model = Resources
    template_name = 'search.html'
    context_object_name = 'resources'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Resources.objects.filter(name__icontains=query).order_by('name')


def calendar(request):
    context = 'Calendar'
    return render(request, 'calendar.html', {})
