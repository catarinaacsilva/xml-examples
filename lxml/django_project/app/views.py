from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime

#TODO: verify this error
from library.xml_proc import read_xml, valid_doc

def sendinfo(request):
    assert isinstance(request, HttpRequest)
    if 'xml' in request.POST and 'schema' in request.POST:
        xml = request.POST['xml']
        schema = request.POST['schema']
        # TODO: verify if it is correct
        result_read = read(xml)  
        result_read = request.POST["result read"]
        result_valid = valid_doc(xml)
        result_valid = request.POST["result validate"]
        if xml and schema:
            return render(
                request,
                'send_results.html',
                {
                    'xml':xml,
                    'schema':schema,
                    'result read': result_read,
                    'result valid': result_valid,
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



