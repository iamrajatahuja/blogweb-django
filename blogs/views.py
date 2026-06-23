from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
# from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.

blog_names = {
    "python-intro": "Python Introduction",
    "django-basics": "Django Basics",
    "python-oops": "Python OOPs",
    "regex": "Regular Expressions",
    "tkinter": None
}

def home_page(request):
    return render(request, "blogs/index.html")
    # res_data = render_to_string("blogs/index.html") #converts HTML content to string
    # return HttpResponse(res_data) #Returning HTML responses

def blogposts(request):
    blog_list = list(blog_names.keys())

    return render(request,"blogs/allposts.html", {"blogs":blog_list})

    # Same logic below is applied in allposts.html via templates
    # list_items = ""
    # for b in blog_list:
    #     blog_path = reverse("blog-post", args=[b]) #reverse generate dynamic url
    #     list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    # res_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(res_data)

    # Instead of manually writing list items we use named urls above
    # res_data = """
    # <ul>
    #     <li><a href="allposts/python-intro">Python Intro</a></li>
    #     <li><a href="allposts/django-basics">Django Basics</a></li>
    # </ul>
    # """

# def python_intro(request):
#     return HttpResponse("Python Introduction")
#
# def django_basic(request):
#     return HttpResponse("Django Basics blogs")
#
# def python_oops(request):
#     return HttpResponse("Python OOPs")

def process_blog_name(blog):
    # "python-intro" => ["python","intro"] => "python intro"
    blog_list = blog.split("-")
    return " ".join(blog_list)

# Dynamic Path Segment - taking path from user and store in blog argument

def blog_post(request,blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {"blog_text":res, "blog_name":process_blog_name(blog)})
    except Exception:
        # res_data = render_to_string("404.html")
        # return HttpResponseNotFound(res_data)
        raise Http404() #works when DEBUG=False in settings and loads 404.html

# def blog_post_by_number(request,blog):
#     return HttpResponse(blog)