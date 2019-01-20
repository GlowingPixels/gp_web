from .models import ImageCategory,Gallery

def categories(request):
    return {
        'categories': ImageCategory.objects.all()
    }