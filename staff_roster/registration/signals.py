from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import Employee
from registration.models import CustomUser


@receiver(post_save, sender=Employee)
def create_user_for_employee(sender, instance, created, **kwargs):
    if created and instance.is_user:
        username = f"{instance.surname.lower()}{instance.name[0].lower()}{instance.patronymic[0].lower()}"
        user = CustomUser.objects.create(username=username, name=instance.name, surname=instance.surname,
                                         patronymic=instance.patronymic)
        user.set_unusable_password()
        user.save()
        instance.user = user
        instance.save()
