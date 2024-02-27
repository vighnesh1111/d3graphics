from django.shortcuts import render
from page.models import Information

def index(request):
    allinfos = Information.objects.all()
    return render(request, 'index.html', {'allinfos': allinfos})

def intensity(request):
    intensity = Information.objects.values('intensity').distinct()
    searches = Information.objects.all()
    return render(request, 'intensity.html', {'intensity': intensity, 'searches': searches})

def likelihood(request):
    likelihood = Information.objects.values('likelihood').distinct()
    return render(request, 'likelihood.html', {'likelihood': likelihood})

def country(request):
    countries = Information.objects.values('country').distinct()
    return render(request, 'country.html', {'countries':countries})

def relevance(request):
    relevance = Information.objects.values('relevance').distinct()
    return render(request, 'relevance.html', {'relevance': relevance})

def year(request):
    years = Information.objects.values('end_year').distinct()
    return render(request, 'year.html', {'years': years})

def topics(request):
    return render(request, 'topics.html')

def region(request):
    return render(request, 'region.html')

def sector(request):
    return render(request, 'sector.html')

def search(request):
    return render(request, 'search.html')

def sf(request):
    query = request.GET["search"]
    searches = Information.objects.filter(title__icontains=query)
    params = {"searches": searches}
    return render(request, 'search.html', params)

def sf1(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, intensity = query)
    intensity = Information.objects.values('intensity').distinct()
    return render(request, 'intensity.html', {"searches": searches, 'intensity': intensity})

def sf2(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, likelihood = query)
    likelihood = Information.objects.values('likelihood').distinct()
    return render(request, 'likelihood.html', {"searches": searches, 'likelihood': likelihood})

def sf3(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, relevance = query)
    relevance = Information.objects.values('relevance').distinct()
    return render(request, 'relevance.html', {"searches": searches, 'relevance': relevance})

def sf4(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, start_year = query)
    year = Information.objects.values('start_year').distinct()
    return render(request, 'year.html', {"searches": searches, 'year': year})

def sf5(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, country = query)
    country = Information.objects.values('country').distinct()
    return render(request, 'country.html', {"searches": searches, 'country': country})

def sf6(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, topic = query)
    topics = Information.objects.values('topic').distinct()
    return render(request, 'topics.html', {"searches": searches, 'topics': topics})

def sf7(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(title__icontains=query, region = query)
    region = Information.objects.values('region').distinct()
    return render(request, 'region.html', {"searches": searches, 'region': region})

def sf8(request):
    query = request.GET["f1"]
    searches = Information.objects.filter(sector = query)
    return render(request, 'sector.html', {"searches": searches})