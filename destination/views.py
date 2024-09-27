from django.shortcuts import render, get_object_or_404
from .models import Destination
from django.core.paginator import Paginator
from django.db.models import Q

def destination_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'name')  # Default sort by name

    destinations = Destination.objects.all()

    if search_query:
        destinations = destinations.filter(
            Q(name__icontains=search_query) | Q(country__icontains=search_query)
        )

    if sort_by in ['name', 'country', 'created_at']:
        destinations = destinations.order_by(sort_by)

    paginator = Paginator(destinations, 6)  # 6 destinations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }

    return render(request, 'destination/destination_list.html', context)
