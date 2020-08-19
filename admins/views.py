from django.shortcuts import render


# admin index.
def admins(request):
    return render(request, 'home.html')