from django.shortcuts import render
from django.views.generic import TemplateView, View

# Создание метода. В конце концов это то, что увидит пользователь. Это конечный файл после перехода по main/. здесь html шаблоны
# к коду ниже - request(в переводе запрос) обязательный тег, необходим для работы метода.
# <h4> - форматирование текста

#def index(request): 
#    return render(request, 'main/index.html' )

class HomeView(TemplateView):
    template_name = 'main/index.html'