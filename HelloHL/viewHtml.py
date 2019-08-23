from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World html'
    return render(request, 'hello.html', context)

