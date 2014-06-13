from django.shortcuts import  render_to_response
from django.template.context import RequestContext

from prueba.apps.main.models import Setting
from prueba.apps.social.models import Social

# Create your views here.

def index_view(request):
    redes = Social.objects.filter(status=True)
    sett = Setting.objects.filter(status=True)[0]
    ctx = {'redes':redes,'sett':sett} 
    return render_to_response('main/index.html',ctx,context_instance = RequestContext(request))