from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView

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

    # if request.method == "POST":
    #     searched = request.POST['searched']
    #     return render(request, 'events/search_bar.html', {})
    # else:
    #     return render(request, 'events/search_bar.html', {})

    return HttpResponse(template.render(context, request))


#will be used for the search bar in the homepage
    # if request.method == "POST":
    #     searched = request.POST['searched']
    #     return render(request, 'events/search_bar.html', {})
    # else:
    #     return render(request, 'events/search_bar.html', {})

    # this if statememt was used at the beginning of training to create a template to submit new resources
    # not needed for the home page but will be used for the add_resources page

    # if request.POST:
    #     resource_form = ResourceForm(request.POST)
    #     if resource_form.is_valid():
    #         resource = resource_form.save(commit=False)
    #         resource.save()
    # else:
    #     resource_form = ResourceForm()
    # template = loader.get_template('home.html')
    # resource_list = ", ".join([r.name for r in resources])
    # context = {
    #     "resources": resources,
    #     "resource_form": resource_form
    # }

    #return HttpResponse(template.render(context, request))
    # return render(request, 'home.html')
    # return HttpResponse(resource_list)


def add_resource(request):
    resources = Resources.objects.all()
    if request.POST:
        resource_form = ResourceForm(request.POST)
        if resource_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.save()
            return redirect('/journal/')
    else:
        resource_form = ResourceForm()
    template = loader.get_template('home.html')
    context = {
        "resources": resources,
        "resource_form": resource_form
    }
    return HttpResponse(template.render(context, request))


# currently being used instead of ResourceCreate
# class ResourceView(generic.ListView):
#     template_name = 'home.html'
#     context_object_name = 'resources'

    #add_resource(request)

    def get_queryset(self):
        return Resources.objects.order_by('name')


# this class should be used in the resource_create page to create a new resource
class ResourceCreate(CreateView):
    #template_name = 'add_resource.html'
    # context_object_name = 'resources'
    model = Resources
    fields = ['name', 'description_name', 'url']

    def get_queryset(self):
        return render(Resources.new_fields, 'add_resource.html')

    def get_success_url(self):
        return reverse('index')





class ResourceUpdate(UpdateView):
    model = Resources
    fields = ['name', 'description_name', 'url']


def searchview(request):

    return render(request, 'search.html', {})

def calendar(request):
    context = 'Calendar'
    return render(request, 'calendar.html', {})
