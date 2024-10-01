# home/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    testiMonials = TestiMonial.objects.all()
    servies = Servie.objects.all()
    blogposts = BlogPost.objects.all().order_by("-created_at")[:3]

    jsondata = {
        "skills": skills,
        "servies": servies,
        "testiMonials": testiMonials,
        "projects": projects,
        "blogposts": blogposts,
    }
    data = {"data": jsondata}
    return render(request, "index2.html", data)


def pricing_view(request):
    plans = Plan.objects.all()
    return render(request, "pricing.html", {"plans": plans})


def payment_view(request):
    plan_id = request.GET.get("plan")
    plan = get_object_or_404(Plan, name=plan_id)
    data = {"plan": plan}
    return render(request, "payment.html", data)


def success_view(request):
    return render(request, "success.html")


bot_token = "6308227197:AAHweeHPdwsa9SDWpr7g627qxpqtbZsaWsU"
chat_id = 5294965763




def success(request, data):
    Transaction_ID = data.split("$")[0]
    user_id = data.split("$")[1]
    planName = data.split("$")[2]
    plan = get_object_or_404(Plan, name=planName)

    text_msg = f"USER: {user_id}\nTransaction: {Transaction_ID}"

    sendMessageUrl = (
        f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text="
        + text_msg
    )
    x = requests.get(sendMessageUrl)

    return render(
        request,
        "success.html",
        {"Transaction_ID": Transaction_ID, "user_id": user_id, "plan": plan},
    )


def blog_post_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blog_post.html", {"blog_post": blog_post})
