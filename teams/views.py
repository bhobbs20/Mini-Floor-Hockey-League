from django.shortcuts import render
from .models import Team

# Create your views here.
def index(request):
    teams = Team.objects.all()
    
    context = {
        'teams': teams
    }
    
    return render(request, 'teams/index.html', context)


def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    
    context = {
        'team': team,
        
    }
    
    return render(request, 'teams/team_detail.html', context)