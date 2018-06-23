from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    request.session['name'] = request.POST['name'],
    request.session['location'] = request.POST['location'],
    request.session['fav_language'] = request.POST['fav_language'],
    request.session['comment'] = request.POST['comment']

    if not 'counter' in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return redirect('survey_form/result')

def result(request):
    return render(request, 'survey_form/result.html')