from django.shortcuts import render
from statistic.read_json.read_json import ReadJson
from statistic.models import *


def index(request):
    read_json = ReadJson()
    read_json()
    all_object = Statistics.objects.all().order_by('data')
    labels = list(all_object.values_list('data', flat=True))
    eur = list(all_object.values_list('eur', flat=True))
    usd = list(all_object.values_list('usd', flat=True))
    jpy = list(all_object.values_list('jpy', flat=True))
    cny = list(all_object.values_list('cny', flat=True))

    return render(request,
                  'html/index.html', context={'eur': eur,
                                              'usd': usd,
                                              'cny': cny,
                                              'jpy': jpy,
                                              'labels': labels})
