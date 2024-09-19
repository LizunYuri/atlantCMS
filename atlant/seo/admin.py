from django.contrib import admin
from .models import CompanyModel, SEOModel

@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', )
    search_fields = ('title', 'subtitle')

    def has_add_permission(self, request):
        return CompanyModel.objects.count() < 1



@admin.register(SEOModel)
class SEOModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ('title', 'subtitle')

    def has_add_permission(self, request):
        return SEOModel.objects.count() < 1
 