# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import FileUploadForm

# Create your views here.

def home(request):
    return render(request, 'upload_file.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file from the form
            uploaded_file = request.FILES['file']

            # Define the destination path where you want to save the files
            destination_path = '/home/lgucebu1/Print/' + uploaded_file.name

            # Save the uploaded file to the destination destination_path
            with  open(destination_path, 'wb') as destination_file:
                for chunk in uploaded_file.chunks():
                    destination_file.write(chunk)

            # Redirect to a success page or perform further actions
            return redirect('success_url')

    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

