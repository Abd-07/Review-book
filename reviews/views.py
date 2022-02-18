from django.shortcuts import render

def reviews(request):
    name_1=request.GET.get("name")
    email_1=request.GET.get("email")
    review_1=request.GET.get("review")
    print(f"Name:{name_1} , Email:{email_1} , Review:{review_1}")
    return render(request,'review.html',{'name_1':name_1 , 'email_1':email_1, 'review_1':review_1})