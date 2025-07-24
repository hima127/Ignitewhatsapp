from django.contrib import admin
from .models import Review
from .models import Job, JobApplication

admin.site.register(Review)




@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'submitted_at')  # ✅ use correct field
    list_filter = ('job', 'submitted_at')                    # ✅ use correct field

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'location')  # Removed 'industry'
    prepopulated_fields = {'slug': ('title',)}
