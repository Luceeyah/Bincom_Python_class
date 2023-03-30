from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def home(request):
    images = Image.objects.all()
    return render(request, 'base.html', {'images': images})


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


# Create your views here.
