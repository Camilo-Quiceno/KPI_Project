"""Cases models"""

#Django
from django.db import models
from django.contrib.auth.models import User

class Case(models.Model):
    """Case model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    case_id = models.CharField(max_length=11,blank=False)
    step = models.CharField(max_length=30,blank=False)
    surgery_type = models.CharField(max_length=30,blank=False)
    
    is_qc = models.CharField(max_length=30,blank=False)
    is_rejected = models.CharField(max_length=30,blank=True)

    time = models.CharField(max_length=30,blank=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return case id"""
        return '{}'.format(self.case_id)




