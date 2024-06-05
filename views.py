from django.shortcuts import render
from .models import PDF
from .forms import PDFForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PDFForm()
    return render(request, 'upload.html', {'form': form})


def select_base_object(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PDFForm()
    return render(request, 'select_base_object.html', {'form': form})


def input_data(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PDFForm()
    return render(request, 'input_data.html', {'form': form})


def display_results(request):
    pdfs = PDF.objects.all()
    return render(request, 'display_results.html', {'pdfs': pdfs})