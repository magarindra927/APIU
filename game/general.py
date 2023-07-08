from .models import Royal,Page,Popular

def global_data(request):
    data={
        'royalData':Royal.objects.all(),
        'pageData':Page.objects.all(),
        'popularData':Popular.objects.all(),
    }
    return data