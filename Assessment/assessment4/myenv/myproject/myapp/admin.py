from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Policy)
admin.site.register(PolicyHolder)
admin.site.register(PolicyTransaction)
admin.site.register(UserProfile)
admin.site.register(Question)
