from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

blog_names = {
    "python-intro": "<h1>Python Introduction</h1>",
    "django-basics": "<h1>Django Basics</h1>",
    "python-oops": "<h1>Python OOPs</h1>",
    "regex": "<h1>Regular Expressions</h1>"
}

def home_page(request):
    return HttpResponse("<h1>Home Page</h1>") #Returning HTML responses

def blogposts(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b]) #reverse generate dynamic url
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    res_data = f"<ul>{list_items}</ul>"

    # Instead of manually writing list items we use named urls above
    # res_data = """
    # <ul>
    #     <li><a href="allposts/python-intro">Python Intro</a></li>
    #     <li><a href="allposts/django-basics">Django Basics</a></li>
    # </ul>
    # """

    return HttpResponse(res_data)

# def python_intro(request):
#     return HttpResponse("Python Introduction")
#
# def django_basic(request):
#     return HttpResponse("Django Basics blogs")
#
# def python_oops(request):
#     return HttpResponse("Python OOPs")

# Dynamic Path Segment - taking path from user and store in blog argument

def blog_post(request,blog):
    try:
        res = blog_names[blog]
    except Exception:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")
    else:
        return HttpResponse(res)

# def blog_post_by_number(request,blog):
#     return HttpResponse(blog)