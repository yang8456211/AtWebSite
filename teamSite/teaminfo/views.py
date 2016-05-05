from django.shortcuts import render

from teaminfo.models import TeamInfo

from django.shortcuts import render_to_response


def showinfo(request):
    infos = TeamInfo.objects.all()
    return render_to_response('teaminfo.html',{'infos':infos})
