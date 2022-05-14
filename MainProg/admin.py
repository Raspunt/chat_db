from django.contrib import admin

from . models import Message
from . models import Chat


class MessageAdmin(admin.ModelAdmin):
    search_fields = ["agent", "username"]
    readonly_fields = ('date',)





admin.site.register(Message,MessageAdmin)
admin.site.register(Chat)
