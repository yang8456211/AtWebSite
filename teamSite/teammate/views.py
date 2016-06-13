from django.shortcuts import render

from teammate.models import TeamMate

from django.shortcuts import render_to_response

def showTeammate(request):
    members = TeamMate.objects.all()
    return render_to_response('teammate.html',{'members':members})
