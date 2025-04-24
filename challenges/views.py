from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Challenges home page")

def monthly_challenge(request, month):
    months = {
        "january": "1",
        "february": "2",
        "march": "3",
        "april": "4",
        "may": "5",
        "june": "6",
        "july": "7",
        "august": "8",
        "september": "9",
        "october": "10",
        "november": "11",
        "december": "12"
    }
    
    challenges = [
        "Learn Django",
        "Learn Japanese"
    ]
    print(month)
    return render(request, "challenges/list.html", {
        "challenges": challenges,
        "month": month
    })

