from django.contrib import admin
from jobapp.models import Indorejob , Punejob , Banglorejob , Hyderabadjob
# Register your models here.
class IndorejobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class PunejobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class BanglorejobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class HyderabadjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Indorejob,IndorejobAdmin)
admin.site.register(Punejob,PunejobAdmin)
admin.site.register(Banglorejob,BanglorejobAdmin)
admin.site.register(Hyderabadjob,HyderabadjobAdmin)