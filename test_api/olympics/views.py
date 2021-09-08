from django.db.models import query
from django.db.models.fields import DateTimeField
from django.http import response
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
import datetime
ALLOWED_MEDALS = ['b','g','s']

# Create your views here.
from .models import Country, Event
import json

def list_events(request):
    events = Event.objects.select_related('country1','country2').all()
    data = []
    for e in events:
        ev_data={}
        ev_data['countries'] = [e.country1.name,e.country2.name]
        ev_data['event_name'] = e.event_type
        ev_data['start'] = str(e.start)
        ev_data['end'] = str(e.end)
        data.append(ev_data)
    data = json.dumps(data)
    return HttpResponse(data,content_type='application/json')

def filter_events(request,date,country):
    query_res = Country.objects.filter(name=country)
    response= {}
    if len(query_res)==0:
        response['message'] = "Country entry doesn't exist"
        response['error'] = "404"
    else:
        country_obj = query_res.first()
        query_res = Event.objects.filter(start=date)
        res1 = query_res.filter(country1=country_obj)
        res2 = query_res.filter(country2=country_obj)
        query_res = set(res1).union(res2)
        data = []
        for q in query_res:
            ev_data={}
            print(q.start)
            ev_data['countries'] = [q.country1.name,q.country2.name]
            ev_data['event_name'] = q.event_type
            ev_data['start'] = str(q.start)
            ev_data['end'] = str(q.end)
            data.append(ev_data)
        response['data'] = data
    response = json.dumps(response)
    return HttpResponse(response,content_type='application/json')

def upadte_medal(request,country,medal):
    countries = Country.objects.filter(name=country)
    response={}
    if len(countries)==0:
        response['message'] = "Country entry doesn't exist"
        response['error'] = "404"
        response = json.dumps(response)
        return HttpResponse(response,content_type='application/json')
    else:
        country_obj = countries.first()
        if medal=='b':
            country_obj.bronze+=1
        elif medal=='g':
            country_obj.gold+=1
        elif medal=='s':
            country_obj.silver+=1
        else:
            response['message'] = "Incorrect medal type entered. Allowed Only:b,g,s"
            response['error'] = "404"
            response = json.dumps(response)
            return HttpResponse(response,content_type='application/json')
    country_obj.save()
    response['message'] = "Successfully updated medal count!!"
    response = json.dumps(response)
    return HttpResponse(response,content_type='application/json')

def add_cheer(request,country):
    query_res = Country.objects.filter(name=country)
    response= {}
    if len(query_res)==0:
        response['message'] = "Country entry doesn't exist"
        response['error'] = "404"
    else:
        country_obj = query_res.first()
        country_obj.cheers+=1
        country_obj.save()
        response['message'] = f"You cheered for {country}!!"
    response = json.dumps(response)
    return HttpResponse(response,content_type='application/json')

def get_cheers(request):
    query_res = Country.objects.all()
    response= {}
    data = []
    for q in query_res:
        c_data = {}
        c_data['cheers'] = q.cheers
        c_data['country'] = q.name
        data.append(c_data)
    response['data'] = data
    response = json.dumps(response)
    return HttpResponse(response,content_type='application/json')

def get_medal_counts(request):
    query_res = Country.objects.order_by('gold','silver','bronze')
    response=[]
    for q in query_res:
        data = {}
        data['gold'] = q.gold
        data['bronze'] = q.bronze
        data['silver'] = q.silver
        data['country'] = q.name
        response.append(data)
    response = json.dumps(response)
    return HttpResponse(response,content_type='application/json')

