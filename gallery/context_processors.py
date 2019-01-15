from .models import ImageCategory

def categories(request):
    return {
        'categories': ImageCategory.objects.all()
    }