from django.contrib import admin
from .models import Service, Project, Testimonial, ContactMessage, SiteSetting, PricingPlan

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'title_en', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'title_en', 'category_ar')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'position_ar')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'title_en', 'price', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
