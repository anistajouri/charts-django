from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
import json


User = get_user_model()

class charts1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})


class charts2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts2.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        with open("aggr1.txt", 'rt') as f:
            aggr1 = json.loads(f.read().replace('\n', ''))
        buckets=aggr1["aggregations"]["all_counties"]["buckets"]
        print(aggr1["aggregations"]["all_counties"]["buckets"][0])
        #qs_count = User.objects.all().count()
        labels =  []
        default_items = []
        for count in range(0,len(buckets)):
            print(buckets[count]["key"])
            labels.append(buckets[count]["key"]) 
            default_items.append(int(buckets[count]["doc_count"]))
        print(labels)
        print(default_items)

        # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        # default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

