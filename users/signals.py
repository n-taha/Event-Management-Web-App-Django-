from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

@receiver(post_save, sender=User)
def send_activation_email(sender, instance , created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_url = f'{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}'
        subject = 'Activate Your Account By Clicking Thsi Link'
        message = f'Hey {instance.username} , how are you? \nyou have signed up Event Management web . please activate your account by clicking this link {activation_url}\n Thank you'
        recipient_list = [instance.email]
        host_mail = settings.EMAIL_HOST_USER


        try:
            send_mail(
                subject,
                message,
                host_mail,
                recipient_list,
                fail_silently= False
            )
        except Exception as e:
            print(f'Failed send to email at {instance.email} :  {str(e)}')


@receiver(post_save, sender=User)
def default_role_set(sender, instance, created , **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='Participant')
        instance.groups.add(user_group)
        instance.save()