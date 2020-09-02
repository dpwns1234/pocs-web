from django.shortcuts import redirect, render, reverse, get_object_or_404
from .forms import CreateWrite
from .models import Write

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    return render(request, 'accounts/index.html')

def cafeMain(request):
    writes = Write.objects.all()

    return render(request, 'cafeMain.html', {'writes': writes})

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
   
def detail(request, write_id):
    write_detail = get_object_or_404(Write, pk=write_id)
 
    return render(request, 'detail.html', {'write_detail': write_detail})