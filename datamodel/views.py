from django.shortcuts import render
from .models import Datamodel

# Create your views here.


def list_datamodels(request):
    obj = Datamodel.objects.all()
    context = {
        'my_list': obj
    }

    return render(request, "table.html", context)
