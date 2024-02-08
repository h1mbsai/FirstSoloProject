from django.urls import path
from . import views # . означает импорт из той же папки, в которой мы находимся. (в нашем случае - main)
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
]
