from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, *args, **kwargs):
        return None