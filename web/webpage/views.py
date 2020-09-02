from django.shortcuts import redirect, render, reverse
from .forms import CreateWrite

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    return render(request, 'accounts/index.html')

def cafeMain(request):
    return render(request, 'cafeMain.html')

def createWrite(request):

    if request.method == 'POST':
        form = CreateWrite(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cafeMain')
        else:
            return redirect('cafeMain')
    else:
        form = CreateWrite()
        
        return render(request, 'createWrite.html', {'form': form})
   

