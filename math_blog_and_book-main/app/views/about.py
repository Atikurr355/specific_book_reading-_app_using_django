from django.shortcuts import render
from django.views import View
from app.models import About


class Abouts(View):
    def get(self, request):
        abouts = About.objects.all()
        context = {
            'about': abouts,
        }
        return render(request, 'about.html',context)
