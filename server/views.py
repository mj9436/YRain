from django.shortcuts import redirect, render
from django.http import HttpResponse


#import RPi.GPIO as GPIO
import time
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
        return render(request, 'server/main.html', {'GET':'0도'});

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

def record(request):
    return render(request, 'server/record.html');

def user_info(request):
    return render(request, 'server/user_info.html');