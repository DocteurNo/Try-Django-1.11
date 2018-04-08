import random
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	num = None
	some_list = [
		random.randint(0, 100000),
		random.randint(0, 100000),
		random.randint(0, 100000)
	]
	condition_bool_item = False
	if condition_bool_item:
		num = random.randint(0, 100000)
	context = {
		"num": num,
		"some_list": some_list
	}
	return render(request, "base.html", context)# 1h08 39s