from django.contrib import admin

from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
	search_fields = ["user__username", "user__email", "name", "user__id"]
	raw_id_fields = ["user"]
	readonly_fields = ["user"]
	
	class Meta:
		model = Car

	def save_model(self, request, obj, form, change):
		if change:
			obj.updated_by = request.user
		obj.save()


admin.site.register(Car, CarAdmin)
