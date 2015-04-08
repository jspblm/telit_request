from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def telit_post_request(request):
	print request.POST
	return HttpResponse('ok')