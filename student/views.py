from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def form_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)  # request the server reconfirmation for end user register
        if form.is_valid():  # validation check is form data is valid?
            form.save()
            return redirect("/")  # redirect to home page
    return render(request, "home.html", {'form': form})
