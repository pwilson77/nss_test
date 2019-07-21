from django.shortcuts import render
from nss_test.tasks import upload_data
from django.core.files.storage import FileSystemStorage
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World </h1>") #string of html code
    if "GET" == request.method:
        return render(request, "home.html", {})
    else:
        excel_file = request.FILES["excel_file"]
        fs = FileSystemStorage()
        filename = fs.save(excel_file.name, excel_file)
        uploaded_file_url = fs.url(filename)

        upload_data.delay(BASE_DIR + uploaded_file_url)

        return render(request, "home.html", {})
