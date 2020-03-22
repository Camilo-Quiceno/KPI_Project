"""Case forms"""

#Django
from django import forms

#models
from cases.models import Case

class CaseForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings"""

        model = Case
        fields = (
                'user',
                'profile',
                'case_id',
                'step',
                'surgery_type',
                'is_qc',
                'is_complex',
                'is_rejected',
                'time',
                'comments'
        )