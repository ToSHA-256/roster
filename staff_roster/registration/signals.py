from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import Employee
from registration.models import CustomUser


@receiver(post_save, sender=Employee)
def create_user_for_employee(sender, instance, created, **kwargs):
    if created and instance.is_user:
        username = f"{instance.surname.lower()}.{instance.name.lower()}"
        user = CustomUser.objects.create(username=username)
        user.set_unusable_password()
        user.save()
        instance.user = user
        instance.save()
