from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for january",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Build one web based project",
    "april": "Learn Node JS",
    "may": "Contribute to open source project",
    "june": "Visit Girlfriend",
    "july": "Build one web based project",
    "august": "Learn Django",
    "september": "Build dating App",
    "october": "Vacation in Dubai",
    "november": "Get new job",
    "december": "Buy a car",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    keys = list(monthly_challenges.keys())

    if month > len(keys):
        return HttpResponseNotFound("Month not found")

    redirect_month = keys[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        return render(request, "challenges/challenge.html", {
            'text': monthly_challenges[month],
            'month': month
        })
    except:
        raise Http404()
