from django.shortcuts import render
from content.models import AboutModel, BlogModel
from seo.models import CompanyModel, SEOModel
from shelude.models import ScheduleModel, ClientModel

def index(request):

    seo = SEOModel.objects.all()

            
    return render(request, 'index.html', {'seo' : seo})

