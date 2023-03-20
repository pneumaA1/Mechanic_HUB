from django.urls import path

from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('blog-grig/', blog_grid, name='blog-grid'),
    path('blog-single/', blog_single, name='blog-single'),
    path('blog-sb/', blog_with_sidebar, name='blog-sb'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('gallery/', gallery, name='gallery'),
    path('gallety-single/', gallery_single, name='gallery-single'),
    path('pricing/', pricing, name='pricing'),
    path('services/', services, name='services'),
    path('shop/', shop, name='shop'),
    path('shop-single/', shop_single, name='shop-single'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('team/', team, name='team'),
    path('testimonials/', testimonials, name='testimonials'),
    path('wheel-works/', wheel_works, name='wheel-works'),
    path('painting_works', painting_works, name='painting-works'),
    path('air-conditioner/', air_conditioner, name='air-conditioner'),
    path('water-service/', water_service, name='water-service'),
    path('engine-works/', engine_works, name='engine-works'),
    path('oil-filters/', oil_filter, name='oil-filters'),
    path('brake-repairs', brake_repairs, name='brake-repairs'),
    path('belts-hoses/', belts_hoses, name='belts-hoses')
]