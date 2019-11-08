from django.shortcuts import render
import datetime
from .models import malzemeler
from django.views import generic
from django.http import HttpResponse


# Create your views here.
class DetailView(generic.DetailView):
    model = malzemeler
    template_name = 'myKitchen/detail.html'
#    def detail(request, malzemeid):
#        malzeme = get_object_or_404(malzemeler, pk=malzemeid)
#        return render(request, 'myKitchen/detail.html', {'malzeme': malzeme})
    
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><b>It is now </b>%s.</body></html>" % now
    return HttpResponse(html)

def my_view(request):
    # ...
    malzeme_list = malzemeler.objects.order_by('-malzeme_text')[:5]
    #template = loader.get_template('myKitchen/index.html')
    context = {
        'malzeme_list': malzeme_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'myKitchen/index.html', context)