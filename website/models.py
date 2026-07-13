from django.db import models

class Service(models.Model):
    title_ar = models.CharField(max_length=200, verbose_name="عنوان الخدمة (عربي)")
    title_en = models.CharField(max_length=200, verbose_name="Service Title (English)")
    description_ar = models.TextField(verbose_name="وصف الخدمة (عربي)")
    description_en = models.TextField(verbose_name="Service Description (English)")
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class e.g. fas fa-code")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title_ar

    class Meta:
        ordering = ['order']

class Project(models.Model):
    title_ar = models.CharField(max_length=200, verbose_name="اسم المشروع (عربي)")
    title_en = models.CharField(max_length=200, verbose_name="Project Name (English)")
    description_ar = models.TextField(verbose_name="وصف المشروع (عربي)")
    description_en = models.TextField(verbose_name="Project Description (English)")
    image = models.ImageField(upload_to='projects/')
    category_ar = models.CharField(max_length=100, verbose_name="التصنيف (عربي)")
    category_en = models.CharField(max_length=100, verbose_name="Category (English)")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title_ar

    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name="الاسم (عربي)")
    name_en = models.CharField(max_length=100, verbose_name="Name (English)")
    position_ar = models.CharField(max_length=100, verbose_name="المنصب (عربي)")
    position_en = models.CharField(max_length=100, verbose_name="Position (English)")
    content_ar = models.TextField(verbose_name="الشهادة (عربي)")
    content_en = models.TextField(verbose_name="Testimonial (English)")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name_ar

class PricingPlan(models.Model):
    title_ar = models.CharField(max_length=100, verbose_name="اسم الباقة (عربي)")
    title_en = models.CharField(max_length=100, verbose_name="Plan Name (English)")
    price = models.CharField(max_length=50, verbose_name="السعر")
    features_ar = models.TextField(help_text="أدخل كل ميزة في سطر جديد (عربي)")
    features_en = models.TextField(help_text="Enter each feature on a new line (English)")
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def get_features_ar(self):
        return self.features_ar.split('\n')
    
    def get_features_en(self):
        return self.features_en.split('\n')

    class Meta:
        ordering = ['order']

class SiteSetting(models.Model):
    site_name_ar = models.CharField(max_length=100, default="علي القفيلي للبرمجيات")
    site_name_en = models.CharField(max_length=100, default="Ali Al-Qafili Software")
    hero_title_ar = models.CharField(max_length=200)
    hero_title_en = models.CharField(max_length=200)
    hero_subtitle_ar = models.TextField()
    hero_subtitle_en = models.TextField()
    about_text_ar = models.TextField()
    about_text_en = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_ar = models.CharField(max_length=300)
    address_en = models.CharField(max_length=300)
    
    def __str__(self):
        return self.site_name_ar

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
