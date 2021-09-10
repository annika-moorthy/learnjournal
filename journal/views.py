from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic import CreateView, UpdateView

from journal.models import Resources
from journal.forms import ResourceForm


def home(request):
    context = 'Solirius Journal App'
    resources = Resources.objects.all()
    # template = loader.get_template('resources_.html')
    # resource_list = ", ".join([r.name for r in resources])
    # context = {
    #     "resources": resources,
    # }

    if request.POST:
        resource_form = ResourceForm(request.POST)
        if resource_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.save()
    else:
        resource_form = ResourceForm()
    template = loader.get_template('resources_.html')
    resource_list = ", ".join([r.name for r in resources])
    context = {
        "resources": resources,
        "resource_form": resource_form
    }

    return HttpResponse(template.render(context, request))
    #return HttpResponse(resource_list)


class ResourceView(generic.ListView):
    template_name = 'resources_.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return Resources.objects.order_by('name')


class ResourceCreate(CreateView):
    model = Resources
    fields = ['name', 'description_name', 'url']


class ResourceUpdate(UpdateView):
    model = Resources
    fields = ['name', 'description_name', 'url']


def calendar(request):
    context = 'Calendar'
    return HttpResponse(context)
