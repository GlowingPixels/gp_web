from .models import ImageCategory, SubCategory

def categories(request):
    
    return {
        'categories': ImageCategory.objects.all()
    }