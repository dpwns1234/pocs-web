from django.shortcuts import redirect, render, reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    return render(request, 'accounts/index.html')
