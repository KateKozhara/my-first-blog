from django.shortcuts import render
from django.utils import timezone
from . models import Post


def KateK(request):
	return render(request, 'blog/KateK.html', {})

