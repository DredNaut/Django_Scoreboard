from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import F

from .models import Team
# Create your views here.

def index(request):
    latest_members_list = Team.objects.order_by('rank')
    rankings_list = Team.objects.annotate(fieldsum=F('pt_score') + F('ruck_score') + F('wpns_score') + F('ln_score') + F('tc3_score') + F('est_score') + F('radio_score') + F('hgac_score') + F('cff_score')).order_by('-fieldsum')

    template = loader.get_template('rankings/index.html')
    context = {
            'latest_members_list' : latest_members_list,
            'rankings_list' : rankings_list,
    }
    return HttpResponse(template.render(context, request))

def team_name(request, members):
    return HttpResponse(f"{members}")
