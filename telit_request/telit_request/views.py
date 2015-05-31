import pytz, datetime, json
	
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings


@csrf_exempt
def telit_post_request(request):
	t_utc = timezone.now() # en UTC 
	t = t_utc.astimezone(pytz.timezone(settings.TIME_ZONE)) # hora de guatemala
	ts = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
	estado_bloqueo = 'B1'
	anuncio = 'adsZZZZZZ'
	response = 'Go*d {fecha_hora} {estado_bloqueo} {anuncio}'.format(fecha_hora=ts, estado_bloqueo=estado_bloqueo, anuncio=anuncio)
	return HttpResponse(response)


@csrf_exempt
def gtbiltregistro(request):
	t_utc = timezone.now() # en UTC 
	t = t_utc.astimezone(pytz.timezone(settings.TIME_ZONE)) # hora de guatemala
	ts = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
	estado_bloqueo = 'B1'
	anuncio = 'adsZZZZZZ'
	response = 'Go*d {fecha_hora} {estado_bloqueo} {anuncio}'.format(fecha_hora=ts, estado_bloqueo=estado_bloqueo, anuncio=anuncio)
	return HttpResponse(response)


entradaanalogica_valores = (
	(1,	3.29758241758, 9.9916747252674, '17:08:09'),
	(2,	3.29758241758, 9.9916747252674, '17:08:09'),
	(3,	3.29597069597, 9.9867912087891, '12:06:36'),
	(4,	3.29597069597, 9.9867912087891, '12:06:36'),
	(5,	3.29597069597, 9.9867912087891, '12:06:36'),
	(6,	3.29677655678, 9.9892329670434, '12:06:36'),
	(7,	3.29758241758, 9.9916747252674, '12:06:36'),
	(8,	3.29677655678, 9.9892329670434, '13:48:57'),
	(9,	3.29355311355, 9.9794659340565, '15:05:49'),
	(10, 3.29838827839,	9.9941164835217, '17:27:35'),
	(11, 3.29194139194,	9.9745824175782, '21:31:57'),
	(12, 3.29597069597,	9.9867912087891, '21:34:30'),
	(13, 3.29597069597,	9.9867912087891, '00:23:04'),
	(14, 3.29758241758,	9.9916747252674, '08:50:49'),
	(15, 3.29758241758,	9.9916747252674, '08:50:49'),
	(16, 3.29597069597,	9.9867912087891, '09:15:22'),
	(17, 3.29597069597,	9.9867912087891, '09:15:22'),
	(18, 3.29597069597,	9.9867912087891, '09:27:59'),
	(19, 3.29758241758,	9.9916747252674, '09:27:59'),
	(20, 3.29677655678,	9.9892329670434, '09:27:59'),
	(21, 3.29677655678,	9.9892329670434, '09:27:59'),
	(22, 3.29597069597,	9.9867912087891, '16:38:32'),
	(23, 0,	0,	'12:30:20'),
	(24, 0,	0,	'12:30:20'),
	(25, 0,	0,	'12:30:20'),
	(26, 3.29838827839,	9.9941164835217, '12:36:43'),
	(27, 3.29516483516,	9.9843494505348, '14:55:16'),
	(28, 0.00161172161172, 0.0048835164835116, '14:55:16')
)

@csrf_exempt
def entradaanalogica(request):
	entradaanalogica_valores_json = json.dumps(entradaanalogica_valores)
	return HttpResponse(entradaanalogica_valores_json)


@csrf_exempt
def entradaanalogica_dato(request, ident):
	entradaanalogica_valores_dict = {valor[0]: valor for valor in entradaanalogica_valores}
	dato = entradaanalogica_valores_dict[int(ident)]
	return HttpResponse(json.dumps(dato))


