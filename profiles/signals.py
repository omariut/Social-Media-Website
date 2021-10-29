from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship, Notification
from posts.models import Post, Like, Comment

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=Profile)
@receiver(post_save, sender=Comment)
@receiver(post_save, sender=Relationship)
@receiver(post_save, sender=Like)
def create_notification(sender, instance, created, **kwargs):
    if created:
        if sender == Profile:
            to_user = instance.user
            from_user = instance.user
            status ='New_Profile'

        if sender == Comment:
            to_user = instance.post.author
            from_user = instance.author
            status ='Comment'
        if sender == Relationship:
            to_user = instance.receiver
            from_user = instance.sender
            status ='Request'
        if sender == Like:
            to_user = instance.post.author
            from_user = instance.profile
            status ='Like'
            print('like')

    
        Notification.objects.create (to_user = to_user , 
                                    from_user=from_user,
                                    status= status)




