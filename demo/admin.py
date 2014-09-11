from demo.models import Post,Meter
from django.contrib import admin

class PostAdmin(admin.ModelAdmin): 
	list_display = ('title', 'created_date')

admin.site.register(Post, PostAdmin)

from import_export.admin import ImportExportModelAdmin
from import_export import resources

class MeterResource(resources.ModelResource):

    class Meta:
        model = Meter

class MeterAdmin(ImportExportModelAdmin):
    resource_class = MeterResource
    pass

admin.site.register(Meter, MeterAdmin)
