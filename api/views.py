from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger

from .tasks import demo_task

logger = getLogger(__name__)

def tasks(request):
    if request.method == 'POST':
        message = request.POST['message']
        logger.debug(f"llamando a demo_task. message={message}")
        demo_task("desde views.py: "+message)
        return JsonResponse({}, status=302)
    else:
        return JsonResponse({}, status=405)



