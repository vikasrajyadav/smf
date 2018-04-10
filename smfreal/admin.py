from django.contrib import admin
from smfreal.models import fundlist,UserProfileInfo,Post, Comment, Myuserdb

admin.site.register(fundlist)
admin.site.register(UserProfileInfo)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Myuserdb)
