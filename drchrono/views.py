# Create your views here.
import requests
import os
from social.backends.oauth import BaseOAuth2
from social_auth_drchrono.backends import drchronoOAuth2
import datetime, pytz, requests

from django.shortcuts import render_to_response, redirect,render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext




def home(request):
    #print(request.code)
    return render_to_response('hello.html')


def first(request):
    '''access_token = request.access_token
    response = requests.get('https://drchrono.com/api/users/current', headers={'Authorization': 'Bearer %s' % access_token})
    response.raise_for_status()
    data = response.json()'''

    ry = drchronoOAuth2()
    res = drchronoOAuth2.ret_res(ry)
    con = drchronoOAuth2.get_user_details(ry,res)
    # You can store this in your database along with the tokens
    context = {
    'username' : con['username']
    }
    return render(request,'hello.html',context);
