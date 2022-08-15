from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
from .models import Dasan
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
    dasanu=Dasan.objects.all()
    return render(request, 'server/dasan.html', {'dasan':dasanu});

def yangjae(request):
    return render(request, 'server/yangjae.html');

def user_info(request):
    userinf=User.objects.get(user_id=request.session['user'])
    if request.method=='POST':
        userinf.nickname=request.POST['nickname']
        userinf.hakbu=request.POST['hakbu']
        userinf.hakgwa=request.POST['hakgwa']
        userinf.save()
        return redirect(user_info)
    return render(request, 'server/user_info.html', {'user':userinf});

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
                return redirect(select)
            return redirect(login)
        except:
            return redirect(login)
    
    return render(request, 'server/login.html');

def signup(request):
    if(request.method=="POST"):
        id=User.objects.filter(user_id=request.POST['user_id']).count()
        print(id)
        if(id!=0):
            return redirect(signup,{'msg':'이미 존재하는 아이디입니다'})
            #return redirect(signup);
        User.objects.create(user_id=request.POST['user_id'], password=request.POST['password'],nickname=request.POST['user_id'],hakbu="",hakgwa="")
        return redirect(login)
    return render(request, 'server/signup.html');


def dasan_result(request):
    num=request.GET.get('dasan_btn')
    dasantmp=Dasan.objects.get(dasan_no=num)
    dasantmp.used=0
    dasantmp.save()
    print(dasantmp.used)
    return redirect(dasan)


def test(request):
    return render(request, 'server/test.html');


def select(request):
    return render(request, 'server/select.html');

def bannap(request):
    return render(request, 'server/bannap.html');

def bannap_dasan(request):
    dasanu=Dasan.objects.all()
    return render(request, 'server/bannap_dasan.html', {'dasan':dasanu});

def bannap_dasan_result(request):
    num=request.GET.get('dasan_btn')
    dasantmp=Dasan.objects.get(dasan_no=num)
    dasantmp.used=1
    dasantmp.save()
    print(dasantmp.used)
    return redirect(bannap_dasan)

def open_door():
        '''GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        pwm=GPIO.PWM(servo_pin, 50)
        
        pwm.start(3.0)
        pwm.ChangeDutyCycle(3.0)
        time.sleep(1.0)
        pwm.stop()
        GPIO.cleanup()'''