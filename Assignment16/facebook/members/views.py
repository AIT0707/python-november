from django.shortcuts import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse (template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse (template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse (template.render())

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse (template.render())

def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse (template.render())

def products(request):
    template = loader.get_template('products.html')
    return HttpResponse (template.render())

def news(request):
    template = loader.get_template('news.html')
    return HttpResponse (template.render())

def vacancy(request):
    template = loader.get_template('vacancy.html')
    return HttpResponse (template.render())


