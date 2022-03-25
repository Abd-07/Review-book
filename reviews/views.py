from sqlite3 import Date
from django.shortcuts import render
from reviews.forms import ReviewForm
from django.shortcuts import redirect
from reviews.models import Review
from django.views import View

class ReviewsView(View):
    def get(self,request):
        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request,'review.html',{'form':form,'reviews':reviews})
    def post(self,request):
        form = ReviewForm(request.POST) 

        if form.is_valid(): 
            data = form.cleaned_data 
            name = data.get('name') 
            email = data.get('email') 
            review = data.get('review') 
            rating = data.get('rating') 
            Review.objects.create(name=name, email=email, review=review, rating=rating) 
            return redirect('reviews') 
        form = ReviewForm() 
        reviews = Review.objects.all() 
        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

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
            date = request.POST.get('date')
            rating = data.get('rating')
            Review.objects.create(name,email,review,date,rating)
            return redirect('reviews')
        else:
            form = ReviewForm()
            return render(request,'review.html',{'form':form})
   
    name_1=request.GET.get("name")
    email_1=request.GET.get("email")
    review_1=request.GET.get("review")
    date_time_1=request.GET.get("date")
    print(f"Name:{name_1} , Date and Time:{date_time_1} , Email:{email_1} , Review:{review_1}")
    return render(request,'review.html',{'form':form})