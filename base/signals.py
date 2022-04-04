from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_profile=instance)
        print('profile created')

@receiver(post_save, sender=User)
@receiver(m2m_changed, sender=Profile)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('profile updated!')
