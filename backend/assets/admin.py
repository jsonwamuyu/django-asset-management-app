from django.contrib import admin
from .models import User,Asset, AssetAssignment

admin.site.register(User)
admin.site.register(Asset)
admin.site.register(AssetAssignment)
