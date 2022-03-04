from sqlite3 import Date
from django.shortcuts import render
from reviews.forms import ReviewForm
from django.shortcuts import redirect

def reviews(request):
    if request.method == 'GET':
        form = ReviewForm()
        #date_time_1=request.GET.get("date")
        return render(request,'review.html',{'form':form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            date = request.POST.get("date")
            rating = data.get('rating')
            with open('data.csv','a')as file:
                file.write(f'{name}|{email}|{review}|{date}|{rating}\n')
            return redirect('reviews')
        else:
            form = ReviewForm()
            return render(request,'review.html',{'form':form})
   
    name_1=request.GET.get("name")
    email_1=request.GET.get("email")
    review_1=request.GET.get("review")
    date_time_1=request.GET.get("date")
    print(f"Name:{name_1} , Date and Time:{date_time_1} , Email:{email_1} , Review:{review_1}")
    return render(request,'review.html',{'name_1':name_1 , 'email_1':email_1, 'review_1':review_1, 'date_time_1':date_time_1, 'form':form})