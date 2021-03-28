from django.shortcuts import render
import re


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	num = len(re.findall(r'\w+', user_text))
	reverse_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reverse_text, 'number': num})