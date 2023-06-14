from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def hello(request):
    return HttpResponse('Hello')

def home(request):
    return render(request, 'myapp/home.html')

class Character:
     def __init__(self,name):
         self.name = name

     def greed(self):
         print(f'{self.name}: こんにちは!')

def home2(request):
    context = {
        'title': 'ホーム２です ',
        # 1: 1,
        'number_list': [1,2,3,4,5],
        'user':Character('Kurihara')
    }
    return render(request, 'myapp/home2.html', context)


class Home(generic.TemplateView):   #TemplateViewはhtmlを単純に表示するのに使う
    template_name = 'myapp/home2.html'

    def get_context_data(self, **kwargs):   #テンプレートファイルに追加で渡したいデータがあるときはこのメソッドを呼ぶ
        #このメソッド上書きの時は、毎回super()で親のメソッドを呼ぶこと
        context = super().get_context_data(**kwargs)
        #辞書[キー名] = 値　形式で追加のデータを渡す
        context['title'] = 'ホームです'
        return context

# Create your views here.
