from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse
from .models import Medicine


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email)
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url="login")
def home(request):
    return render(request,'home.html')

@login_required(login_url="login")
def add_medicine(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        expiry = request.POST['expiry']
        
        user = request.user
        
        medicine = Medicine(name=name, description=description, price=price, quantity=quantity, expiry=expiry,user=user)
        medicine.save()
        return redirect('medicine_list')
    return render(request, 'addmedicine.html')

@login_required(login_url="login")
def edit_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    if request.method == 'POST':
        medicine.name = request.POST['name']
        medicine.description = request.POST['description']
        medicine.price = request.POST['price']
        medicine.quantity = request.POST['quantity']
        medicine.expiry = request.POST['expiry']
        medicine.save()
        return redirect('medicine_list')
    return render(request, 'editmedicine.html', {'medicine': medicine})

@login_required(login_url="login")
def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'deletemedicine.html', {'medicine': medicine})

@login_required(login_url="login")
def medicine_list(request):
    listmedicines = Medicine.objects.filter(user=request.user)
    return render(request, 'medicinelist.html', {'listmedicines': listmedicines})

@login_required(login_url="login")
def search_medicine(request):
    query = request.GET.get('query')
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()
    
    context = {
        'medicines': medicines,
        'query': query
    }
    return render(request, 'searchmedicine.html', context)