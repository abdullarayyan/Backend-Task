from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EnumField(models.Field):

    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        if not self.choices:
            raise AttributeError('EnumField requires `choices` attribute.')

    def db_type(self):
        return "enum(%s)" % ','.join("'%s'" % k for (k, _) in self.choices)

GENDER_MALE = 'm'
GENDER_FEMALE = 'f'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)


MARITAL_Single='s'
MARITAL_Married='m'
MARITAL_Divorced='D'
MARITAL_CHOICES=(
    (MARITAL_Single,'Single'),
    (MARITAL_Married,'Married'),
    (MARITAL_Divorced,'Divorced')
)
#############################################################33
class UserProfile(models.Model):
    owner =models.ForeignKey(to=User,on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False, blank=False, default="-1",primary_key=True)
    gender = EnumField(choices=GENDER_CHOICES)
    maital_status=models.IntegerField(choices=MARITAL_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#####################################################################################################################

class Posts(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False, blank=False, default="-1",primary_key=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





