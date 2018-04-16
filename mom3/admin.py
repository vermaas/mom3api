from django.contrib import admin

# Register your models here.
from .models import Project, Mom2Object, Dataproduct, Mom2Objectstatus

# Register your models here.
admin.site.register(Dataproduct)
admin.site.register(Project)
admin.site.register(Mom2Object)
admin.site.register(Mom2Objectstatus)