from django.contrib import admin
from users import models
# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Posts)
admin.site.register(models.Comment)