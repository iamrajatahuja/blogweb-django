from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from datetime import date
from django.urls import reverse
# from django.template.loader import render_to_string
from .models import Post
from .forms import CommentForm

# Create your views here.

# blog_names = {
#     "python-intro": "Python Introduction",
#     "django-basics": "Django Basics",
#     "python-oops": "Python OOPs",
#     "regex": "Regular Expressions",
#     "tkinter": None
# }

# For In-memory implementation
# blog_details = [
#     {
#         "slug": "python-intro",
#         "image": "python_image.png",
#         "date": date(2026, 6, 26),
#         "title": "Python Introduction",
#         "preview": """Python is an opensource, high level programming language.
#         Applications of Python are Data Science, AI and ML etc.""",
#         "content": """Python is a high-level, interpreted programming language widely celebrated for its clear syntax,
#         readability, and versatile application across diverse technology sectors."""
#     },
#     {
#         "slug": "django-basics",
#         "image": "django_image.png",
#         "date": date(2026, 6, 27),
#         "title": "Django Basics",
#         "preview": """Django is a web framework for Python""",
#         "content": """Django is a high-level, open-source Python web framework designed to help developers build secure,
#          scalable, and maintainable web applications quickly."""
#     },
#     {
#         "slug": "python-oops",
#         "image": "python_image.png",
#         "date": date(2026, 6, 26),
#         "title": "Python OOPS",
#         "preview": """Object Oriented Programming in Python""",
#         "content": """Object-Oriented Programming (OOP) in Python is a paradigm that structures code by bundling related data
#          and behaviors into individual objects."""
#     },
#     {
#         "slug": "python-regex",
#         "image": "python_image.png",
#         "date": date(2026, 6, 27),
#         "title": "Python Regex",
#         "preview": """Regular Expressions in Python""",
#         "content": """In Python, regular expressions are handled through the built-in re Module. This module provides an interface to scan, match,
#         and modify strings based on structural patterns instead of literal text."""
#     }
# ]

def home_page(request):
    # sorted_blogs = sorted(blog_details, key=lambda post: post["date"], reverse=True) #To sort the list in descending order
    # latest_blogs = sorted_blogs[:2]
    latest_blogs = Post.objects.all().order_by('-date')[:2]
    return render(request, "blogs/index.html", {"l_blogs":latest_blogs})
    # res_data = render_to_string("blogs/index.html") #converts HTML content to string
    # return HttpResponse(res_data) #Returning HTML responses

def blogposts(request):
    # blog_list = list(blog_names.keys())
    blog_details = Post.objects.all()
    return render(request,"blogs/allposts.html", {"blogs":blog_details})

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

# def process_blog_name(blog):
#     # "python-intro" => ["python","intro"] => "python intro"
#     blog_list = blog.split("-")
#     return " ".join(blog_list)

# Dynamic Path Segment - taking path from user and store in blog argument

# def get_blog_by_slug(blog_url):
#     for blog in blog_details:
#         if blog['slug'] == blog_url:
#             return blog
#     return None

def blog_post(request,blog):
    post_data = Post.objects.get(slug=blog)
    tag_caption = post_data.tags.all()
    all_comments = post_data.comments.all().order_by('-id')

    if request.method == "POST":
        commented_data = request.POST
        form = CommentForm(commented_data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_data
            comment.save()
            return HttpResponseRedirect(reverse("blog-post", args=[blog]))
        return render(request, "blogs/posts.html", {"post": post_data, "tags": tag_caption, "comment_form": form, "comments": all_comments})
    else:
        try:
            # res = blog_names[blog]
            # res = get_blog_by_slug(blog)
            # return render(request, "blogs/posts.html", {"blog_text":res, "blog_name":process_blog_name(blog)})

            form_data = CommentForm()

            return render(request, "blogs/posts.html", {"post": post_data, "tags":tag_caption, "comment_form":form_data, "comments":all_comments})
        except Exception:
            # res_data = render_to_string("404.html")
            # return HttpResponseNotFound(res_data)
            raise Http404() #works when DEBUG=False in settings and loads 404.html

# def blog_post_by_number(request,blog):
#     return HttpResponse(blog)