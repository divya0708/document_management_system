from django.shortcuts import render
from django.http import HttpResponse
from documents.models import *

# Create your views here.
def Form(request):
	return render(request, "documents/form.html", {})

def Upload(request):
	for count,x in enumerate(request.FILES.getlist("files")):
		def process(f):
			with open('E:/doc_man_system/dms/media/file_' + str(count),'wb+') as destination:
				for chunk in f.chunks():
					file_upload=destination.write(chunk)

					Documents.objects.create(file_upload=str(file_upload))		
		process(x)
	return render(request, "documents/upload.html", {})			