from django.shortcuts import render

from teammate.models import TeamMate

from django.shortcuts import render_to_response

def index(request):
    members = TeamMate.objects.all()
    return render_to_response('indexper.html',{'members':members})
