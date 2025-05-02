from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

class PostViews(generic.View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the blog index.")