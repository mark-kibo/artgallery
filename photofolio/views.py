from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegisterForm, ArtImagesForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, ArtImages

from django.contrib import messages


# Create your views here.

# login decorator to restrict users

@login_required(login_url="login")


#home rendering function
def home(request):
    data_from_db=ArtImages.objects.all()#list of images from db
    return render(request, 'index.html', {'images': data_from_db})


#about page function
def about(request):
    return render(request, 'about.html')


#contact page function
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send mail from user page to the admin communication center
        send_mail(subject, message, email, ['kibochamark@gmail.com'])
        return render(request, 'contact.html', {'message_name': name})
    return render(request, 'contact.html')


#services page function
def services(request):
    return render(request, 'services.html')


#gallery of images function
def gallery(request, pk):
    print(pk)
    images_in_db=ArtImages.objects.filter(type=pk).all()
    print(images_in_db)
    count=ArtImages.objects.filter(type=str(pk)).count()

    return render(request, 'gallery.html', {'images':images_in_db, 'count': count, 'type': pk})



def galleryinner(request):
    return render(request, 'gallery-single.html')


#login user or admin based on role(is_admin)
def login_user_or_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #authenticate user or admin 
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('upload')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login1.html')



#logout user or admin when request is passsed
def logout_user_or_admin(request):
    logout(request)
    return redirect('home')


#set login decorator to restrict users that are not admins
@login_required(login_url='login')
def upload(request):
    #upload images posted by the admin to the db
    if request.method == "POST":
        form = ArtImagesForm(request.POST, request.FILES)
        print(form)
        type=form.cleaned_data['type']
        images= request.FILES.getlist('art_image')
        print(images)
        if form.is_valid():
            for instance in images:
                data=ArtImages(type=type, art_image=instance)
                data.save()
            return redirect('home')
        else:
            messages.info(request, "form is not valid")
            return redirect('upload')
    else:
        form = ArtImagesForm()
        return render(request, 'up.html', {'form': form})



#register user or admin based on role
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'user_registration.html', {'form': form})