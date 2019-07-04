from django.contrib import admin
from .models import User,StoreInfo,Goods,TypeInfo

# Register your models here.
admin.site.register(User)
admin.site.register(StoreInfo)
admin.site.register(Goods)
admin.site.register(TypeInfo)