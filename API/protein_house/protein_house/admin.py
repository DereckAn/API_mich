from django.contrib import admin
from .models import User, Userphone, Phonetype, Useraddress, Addresstype, Userinfo, Pagedata


admin.site.register(User)
admin.site.register(Userphone)
admin.site.register(Phonetype)
admin.site.register(Useraddress)
admin.site.register(Addresstype)
admin.site.register(Userinfo)
admin.site.register(Pagedata)
