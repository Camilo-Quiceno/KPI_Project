from django.contrib import admin

# Register your models here.


from django.contrib.auth.models import User
from cases.models import Case

@admin.register(Case)
class PostAdmin(admin.ModelAdmin):
    """Profile admin"""
    
    list_display = (
                'user',
                'case_id',
                'step',
                'surgery_type',
                'is_qc',
                'is_complex',
                'is_rejected',
                'time'
    )

    search_fields=('case_id','step','surgery_type',)
    list_filter=('step','surgery_type','is_qc')