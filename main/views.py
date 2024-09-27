from django.shortcuts import render
from destination.models import Destination
from destination.models import Country
from django.core.paginator import Paginator

# Create your views here.
def home_page(request):

    return render(request, 'home.html')

def destination_page(request):
    countries = Country.objects.all()
    destinations = Destination.objects.all()

    selected_country_id = request.GET.get('country')
    if selected_country_id:
        destinations = destinations.filter(country_id=selected_country_id)  # Filter by country ID

    # Pagination: Show 3 destinations per page
    paginator = Paginator(destinations, 3)  # 3 destinations per page
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context ={
        'countries': countries,
        'selected_country_id': selected_country_id,
        'destinations': destinations,
        'page_obj': page_obj 
    }
    return render(request, 'destination.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

