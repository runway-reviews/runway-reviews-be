from django.contrib import admin
from .models import Review
from .models import Airport
from .models import User

admin.site.register(Review)
admin.site.register(Airport)
admin.site.register(User)
# Register your models here.
