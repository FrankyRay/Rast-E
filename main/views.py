from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ShopForm
from main.models import Shop

def show_main(request):
    context = {
            'shop': 'Rast-E',
            'name': 'Franky Raymarcell Sinaga',
            'class': 'PBP F',
            'shops': Shop.objects.all()
    }

    return render(request, "main.html", context)

def create_shop(request):
    form = ShopForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = { "form": form }
    return render(request, "create_shop.html", context)

def show_xml(request):
    data = Shop.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Shop.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Shop.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Shop.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
