from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import Register

def home(request):
    message = ""  # Variable to hold messages for the user
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            em = fm.cleaned_data['email']
            nm = fm.cleaned_data['name']
            if Register.objects.filter(email=em,name=nm).exists():
                message = "Email ID Or Name is already exists. Please use a different email."
            else:
                reg = Register(name=nm, email=em)
                reg.save()
                return redirect('home')  # Redirect to clear the form after successful save
    else:
        fm = StudentRegistration()
        
    return render(request, 'forms/register.html', {'form': fm, 'message': message})
