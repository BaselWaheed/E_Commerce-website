from .models import Category


def get_category(request):
    return {
        'category': Category.objects.all(),
        }