from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def telit_post_request(request):
	# print str(request.POST)
	return HttpResponse('ok POST: %s --- READ %s'%(request.POST, request.read()))