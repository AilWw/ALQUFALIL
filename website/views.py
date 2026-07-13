from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import translation
from .models import Service, Project, Testimonial, ContactMessage, SiteSetting, PricingPlan

def home(request):
    lang = translation.get_language()
    services = Service.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    pricing_plans = PricingPlan.objects.all()
    settings = SiteSetting.objects.first()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'pricing_plans': pricing_plans,
        'settings': settings,
        'lang': lang,
    }
    return render(request, 'website/home.html', context)

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, 'تم إرسال رسالتك بنجاح!' if translation.get_language() == 'ar' else 'Message sent successfully!')
    return redirect('home')
