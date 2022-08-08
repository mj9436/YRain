from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
#import RPi.GPIO as GPIO
import time
import logging
servo_pin=18

def main(request):
    if request.method=='POST':
        '''GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        pwm=GPIO.PWM(servo_pin, 50)

        pwm.start(3.0)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1.0)
        pwm.stop()
        GPIO.cleanup()'''
        return render(request, 'server/main.html');
        #return render(request, 'server/index.html', {'POST':request.POST['one']});
        
    if request.method=='GET':
        '''GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        pwm=GPIO.PWM(servo_pin, 50)
        
        pwm.start(3.0)
        pwm.ChangeDutyCycle(3.0)
        time.sleep(1.0)
        pwm.stop()
        GPIO.cleanup()'''
        return render(request, 'server/main.html', {'GET':"test"});

def borrow(request):
    #if request.method=='POST':
     #   return redirect(index)
    return render(request, 'server/borrow.html');

def cur_status(request):
    return render(request, 'server/cur_status.html');

def dasan(request):
    return render(request, 'server/dasan.html');

def yangjae(request):
    return render(request, 'server/yangjae.html');

def user_info(request):
    return render(request, 'server/user_info.html');

def profile(request):
    return render(request, 'server/profile.html');

def money(request):
    return render(request, 'server/money.html');

def app_info(request):
    return render(request, 'server/app_info.html');

def login(request):    
    if(request.method=="POST"):
        users=User.objects.all()
        IDtmp=request.POST['user_id']
        try:
            user=User.objects.get(user_id=IDtmp)
            if(user.password==request.POST['password']):
                response=render(request,'server/main.html')
                request.session['user'] = user.user_id
                return redirect(main)
            return redirect(login)
        except:
            return redirect(login)
    return render(request, 'server/login.html');

def signup(request):
    if(request.method=="POST"):
        User.objects.create(user_id=request.POST['user_id'], password=request.POST['password'])
        return redirect(login)
    return render(request, 'server/signup.html');

