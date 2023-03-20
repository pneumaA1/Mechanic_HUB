from django.shortcuts import render
def index(request):
    return render(request, 'webapp/index-2.html')

def about(request):
    return render(request, 'webapp/about.html')

def account(request):
    return render(request, 'webapp/account.html')

def blog_grid(request):
    return render(request, 'webapp/blog-grid.html')

def blog_single(request):
    return render(request, 'webapp/blog-single.html')

def blog_with_sidebar(request):
    return render(request, 'webapp/blog-with-sidebar.html')

def checkout(request):
    return render(request, 'webapp/checkout.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def faq(request):
    return render(request, 'webapp/faq.html')

def gallery(request):
    return render(request, 'webapp/gallery.html')

def gallery_single(request):
    return render(request, 'webapp/gallery-single.html')

def pricing(request):
    return render(request, 'webapp/pricing.html')

def services(request):
    return render(request, 'webapp/services.html')

def shop(request):
    return render(request, 'webapp/shop.html')
def shop_single(request):
    return render(request, 'webapp/shop-single.html')

def shopping_cart(request):
    return render(request, 'webapp/shopping-cart.html')

def team(request):
    return render(request, 'webapp/team.html')
def testimonials(request):
    return render(request, 'webapp/testimonials.html')

def wheel_works(request):
    return render(request, 'webapp/ser-single1-wheel-works.html')

def painting_works(request):
    return render(request, 'webapp/ser-single2-painting-works.html')

def air_conditioner(request):
    return render(request, 'webapp/ser-single3-air-conditioner.html')

def water_service(request):
    return render(request, 'webapp/ser-single4-water-service.html')

def engine_works(request):
    return render(request, 'webapp/ser-single5-engine-works.html')

def oil_filter(request):
    return render(request, 'webapp/ser-single6-lube-oil-filters.html')

def brake_repairs(request):
    return render(request, 'webapp/ser-single7-brake-repairs.html')

def belts_hoses(request):
    return render(request, 'webapp/ser-single8-belts-hoses.html')