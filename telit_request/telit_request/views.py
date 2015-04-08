import pytz, datetime
	
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings


@csrf_exempt
def telit_post_request(request):
	t_utc = timezone.now() # en UTC 
	t = t_utc.astimezone(pytz.timezone(settings.TIME_ZONE)) # hora de guatemala
	ts = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
	response = 'Go*d %s'%(ts,)
	return HttpResponse(response + " request.POST: " + str(request.POST) + " request.read(): " + request.read())


@csrf_exempt
def gtbiltregistro(request):
	t_utc = timezone.now() # en UTC 
	t = t_utc.astimezone(pytz.timezone(settings.TIME_ZONE)) # hora de guatemala
	ts = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
	response = 'Go*d %s'%(ts,)
	return HttpResponse(response + " request.POST: " + str(request.POST) + " request.read(): " + request.read())