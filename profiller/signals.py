from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiller.models import Profil


@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    print(instance.username, "____Created:__",created)
    if created:
        Profil.objects.create(user=instance)