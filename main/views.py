from django.shortcuts import render

def show_main(request):
    context = {
            'shop': 'Rast-E',
            'name': 'Franky Raymarcell Sinaga',
            'class': 'PBP F',
    }

    return render(request, "main.html", context)
