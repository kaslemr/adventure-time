from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.generic import CreateView
from atus_analysis.models import PersonInfo


class HomeView(CreateView):
    model = PersonInfo
    fields =  ['id', 'person_id', 'weight', 'youngest_child', 'age', 'sex', 'education', 'race',
               'metro_status', 'labor_status', 'weekly_earnings']
    success_url = '/'