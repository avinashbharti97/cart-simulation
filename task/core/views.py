from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from core.forms import UserForm
from django.shortcuts import render, get_object_or_404
from .models import Cart, Product
from .cart_api import CartSerializer, ProductSerializer
from rest_framework import generics
import datetime

# Create your views here.

class GetCart(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        id = self.kwargs['user_id']
        return Cart.objects.filter(userId = id)


class GetNoti(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        id = self.kwargs['user_id']
        now = datetime.datetime.now()


        #update date here//


        if ((now.month ==2 and now.day == 28)or(now.day == 20)) and (Cart.objects.filter(userId = id)):
            return Cart.objects.filter(userId = id)
        else:
            return Cart.objects.none()



def index(request):
    return render(request, 'index.html')

#Auth views

#registration view
def register(request):
    #A boolean value is added to tell the template
    #whether the registration was successful
    #Initially it is set to False. It will change
    #to True when registration succeeds.
    registered = False

    #if it's a HTTP POST, processing of form data should done :D.
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)


        if user_form.is_valid():
            user = user_form.save()

            #saving the password after hashing wtih the set_password method
            user.set_password(user.password)
            user.save()

            #Updating variable to indicate that the template
            #registration was successful
            registered = True
        else:
            #Invalid form - mistaken something?
            #lets Print the problem
            print(user_form.errors)
    else:
        #Not a HTTP POST? render the form again :D
        user_form = UserForm()


    #Render the template with context
    return render(request,
                'register.html',
                {
                'user_form':user_form,
                'registered':registered
                })


#login views
def user_login(request):
    # if the request is a HTTP POST,
    #trying to pull the relevent information
    if request.method == 'POST':
        #gather the username and Password
        #here request.POST.get('<variable>')
        #is used instead of request.POST.('<variable>')
        #beacuse later raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        #checking if the combination of
        #username and password is valid or not
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('index'))

                return redirect('/api/')

            else:
                return HttpResponse("Your account is disabled")

        else:
            print('Invalid login details: {0}, {1}').format(username, password)
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'login.html',{})


#logout views
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))