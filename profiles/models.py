from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    friends = models.ManyToManyField ("self", blank = True)
    image = models.ImageField(upload_to='images', null=True, blank=True, default='avatar.png')

    def get_all_posts(self):
        all_posts=self.user.posts.all()
        return all_posts

    def get_friend_list(self):
        friends=self.friends.all()
        return friends
    def get_mutual_friends(self, friend):
        self_friends= self.get_friend_list()
        friends_friends=friend.get_friend_list()
        mutual_friends = self_friends.intersection(friends_friends)
        return mutual_friends

    def get_friends_of_friends(self):
        me = self
        my_friends= self.get_friend_list()
        print(my_friends)
        friends_of_friends =[]
        for friend in my_friends:
            friends_friends=friend.get_friend_list()
            for friend in friends_friends:
                if friend not in my_friends and friend != me and friend not in friends_of_friends :
                    friends_of_friends.append(friend)
        return friends_of_friends

    def get_request_sent_list(self):
        user=self.user
        request_sent_rel = Relationship.objects.filter(sender=user)
        request_sent_list_1 = [rel.receiver for rel in request_sent_rel]
        request_sent_list=[]
        for rel in request_sent_rel:
            request_sent_list.append(rel.receiver)
        return request_sent_list

    def get_request_rcv_list(self):
        user=self.user
        request_rcv_rel = Relationship.objects.filter(receiver=user)
        request_rcv_list=[]
        for rel in request_rcv_rel:
            request_rcv_list.append(rel.sender)
        return request_rcv_list

    def get_friends_posts(self):
        friends=self.get_friend_list()
        posts=[post for friend in friends for post in friend.user.posts.all()]
        return posts

    def get_all_notifications(self):
        return Notification.objects.filter(to_user = self.user)

    def get_absolute_url(self):
        return reverse('profile:profile-detail', args=[str(self.id)])




    def __str__(self):
        return self.name
STATUS_CHOICES  = (
                ('New_Profile', 'New_Profile'),
                ('Like','Like'),
                ('Comment','Comment'),
                ('Request','Request'),
                ('Share','Share')
)
class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_profile')
    from_user = models.ForeignKey(User, blank = True, on_delete=models.CASCADE, related_name='from_profile')
    status = models.CharField(max_length = 11, choices=STATUS_CHOICES )
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return str(self.id)


class Relationship(models.Model):
    sender= models.ForeignKey(User, on_delete=models.CASCADE,default=None, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,default=None, related_name='receiver')

    def __str__(self):
        return str(self.id)









