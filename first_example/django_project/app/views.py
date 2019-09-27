from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime

def sendinfo(request):
    assert isinstance(request, HttpRequest)
    if 'xml' in request.POST and 'schema' in request.POST:
        xml = request.POST['xml']
        schema = request.POST['schema']
        if xml and schema:
            return render(
                request,
                'send_results.html',
                {
                    'xml':xml,
                    'schema':schema,
                }
            )
        else:
            return render(
                request,
                'send_info.html',
                {
                    'error':True,
                }
            )
    else:
        return render(
            request,
            'send_info.html',
            {
                'error':False,
            }
        )



