from django.contrib import admin

from ArtI.models import Creator, Creation, Category


class CreatorAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


class CreationAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "created_at", "updated_at")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("style", "created_at", "updated_at")


admin.site.register(Creator, CreatorAdmin)
admin.site.register(Creation, CreationAdmin)
admin.site.register(Category, CategoryAdmin)
