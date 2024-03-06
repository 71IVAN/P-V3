from django.shortcuts import render,redirect
from .forms import formThird

def create_third(request):
    if request.method == 'POST':
        form = formThird(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirige a una página de éxito o a donde desees
    else:
        form = formThird()
    return render(request, 'your_template.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')