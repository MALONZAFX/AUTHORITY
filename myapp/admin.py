
from django.contrib import admin
from . models import Gallery,Video,PrivitasationUsers,AvailableOpening,News,RecentActivities

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Video)
admin.site.register(PrivitasationUsers)
admin.site.register(AvailableOpening)
admin.site.register(News)
admin.site.register(RecentActivities)
