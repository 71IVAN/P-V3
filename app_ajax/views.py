from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View

class UsersList(View):
    def get(self,request):
        users = list(User.objects.values())
        
        return   JsonResponse({'users': users})