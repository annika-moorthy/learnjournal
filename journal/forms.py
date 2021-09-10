from django.forms import ModelForm
from journal.models import Resources


# Create the form class.
class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['name', 'description_name', 'url']
