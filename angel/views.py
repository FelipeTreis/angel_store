from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from angel.models import Clothes


def home(request):
    clothes = Clothes.objects.filter(
        is_published=True,).order_by('-id')

    return render(request, 'angel/pages/home.html', context={
        'clothes': clothes,
    })


def category(request, category_id):
    clothes = get_list_or_404(Clothes.objects.filter(
        category__id=category_id, is_published=True,).order_by('-id'))

    return render(request, 'angel/pages/category.html', context={
        'clothes': clothes,
        'title': f'Categoria-{clothes[0].category.name}'
    })


def piece(request, id):
    clothe = get_object_or_404(Clothes, pk=id, is_published=True)

    return render(request, 'angel/pages/piece-view.html', context={
        'clothe': clothe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    clothes = Clothes.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(gender__icontains=search_term) |
            Q(slug__icontains=search_term),
        ), is_published=True
    ).order_by('-id')

    return render(request, 'angel/pages/search.html', {
        'page_title': f'Pesquisa por "{search_term}" |',
        'search_term': search_term,
        'clothes': clothes,
    })
