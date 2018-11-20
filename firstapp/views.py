from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from firstapp.models import Curriculum


def index1(request):
    return HttpResponse('<h1>Hello</h1>')


def index2(request):
    return HttpResponse('<h1>Hi</h1>')


def main(request):
    return HttpResponse('<h1>Main</h1>')



def show(request):
    curriculum = Curriculum.objects.all()
    html = ''
    for c in curriculum:
        html += c.name + '<br>'
    #Ctrl+/ : 주석
    # return HttpResponse(html)
    return render(
        request,
        'firstapp/show.html',
        {'data':html, 'curriculum':curriculum}
    )
    #렌더(처음에 리쿼스트(무조건), 경로, 딕셔너리{}
    #딕셔너리의 키를 show 에 적어주면 템플릿에 전달됨
    #{{data}}








 #여러개를 가져올때는 all. 1개는 get.