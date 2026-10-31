from django.contrib import admin
from .models import BlogModel, SolutionModel,LinksModel,AboutMeModel
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(SolutionModel)

class SingleAdminModel(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)
    def has_delete_permission(self, request, obj = None):
        return False
admin.site.register(LinksModel, SingleAdminModel)
admin.site.register(AboutMeModel,SingleAdminModel)