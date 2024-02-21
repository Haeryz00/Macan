from django.shortcuts import render, redirect

from item.models import Category, Item

from . forms import SignupForm

from django.contrib.auth import logout


# Create your views here.
def index(request):
    item = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : item,
    })

def contact(request):
    return render(request, 'core/contact.html')
def about(request):
    return render(request, 'core/about.html')
def Privacy_of_policy(request):
    return render(request, 'core/Privacy_of_policy.html')
def FAQ(request):
    return render(request, 'core/FAQ.html')
def Term_of_use(request):
    return render(request, 'core/Term_of_use.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('core:login')  # Redirect to the login page after logout