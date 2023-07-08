from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from .serializers import FamilySerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests;

# Create your views here.

class FamilyViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Family.objects.all()
    serializer_class = FamilySerializer



def index(request):
    data={
        'royalData':Royal.objects.all(),
    }
    return render(request, 'index.html', data)

def contact(request):
    if request.method == 'POST':
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail("Subject:"+ subject, message, email, ['magarindra927@gmail.com'], fail_silently=False)
        messages.success(request, 'Your message has been sent successfully')
        back=request.META.get('HTTP_REFERER')
        return redirect (back)
    else:    
        return render(request, 'contact.html')

def family(request):
    if request.method == 'POST':
        search=request.POST['search']
        find_data=Family.objects.filter(royal__name=search)| Family.objects.filter(title__icontains=search)         
        paginator=Paginator(find_data,3)
        page=request.GET.get('page')
        find_data=paginator.get_page(page)
        data={
            'familyData':find_data,
            'title':'Search Result'
        }
        return render(request, 'family.html', data)
    else:
        family_data=Family.objects.all()
        paginator=Paginator(family_data,3)
        page=request.GET.get('page')
        family_data=paginator.get_page(page)
        data={
            'familyData':family_data,
            'title': 'All News'
        }
    return render(request, 'family.html', data)
    




def royal_family(request, slug):
    data={
        'royData':Royal.objects.get(slug=slug),
    }
    return render(request, 'royal_family.html', data)

def family_details(request, slug):
    familyData=Family.objects.get(slug=slug)
    royal=familyData.royal.id
    related_family=Family.objects.filter(royal=royal).exclude(id=familyData.id)
    data={
        'familyData':Family.objects.get(slug=slug),
        'related_family':related_family,
    }
    return render(request, 'family_details.html', data)


def page(request, slug):
    data={
       'pageContent':Page.objects.get(slug=slug)
    }
    return render(request, 'page.html', data)

def popular_page(request, slug):
    data={
        'popularContent':Popular.objects.get(slug=slug)
        }
    return render(request, 'popular_page.html', data)


def news_api(request):
    url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=d9ee7c42051e40ffa298114b256596fa"
    response=requests.get(url)
    data=response.json()
    data=data['articles']
    send_data={
        'familyData':data
    }
    return render(request, 'news_api.html', send_data)


