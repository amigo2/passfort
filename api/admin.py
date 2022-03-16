from django.contrib import admin
from .models import Document
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Document, SimpleHistoryAdmin)


