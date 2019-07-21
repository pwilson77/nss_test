from django.shortcuts import render
from .models import Fileupload
# Create your views here.


def list_fileuploads(request):
    obj = Fileupload.objects.all()
    context = {
        'my_list': obj
    }

    return render(request, "fileuploadtable.html", context)
