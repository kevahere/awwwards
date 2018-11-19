from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    class that extends the user profile from django
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)

    @classmethod
    def get_user(cls, user):
        ask = cls.objects.filter(user=user)
        return ask

    @classmethod
    def update_profile(cls, id, bio, pic):
        upd8 = cls.objects.filter(user=id)
        upd8.bio= bio
        upd8.profile_pic = pic
        upd8.save()

    def save_profile(self):
        self.save()

    @classmethod
    def search_profiles(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term)

    @classmethod
    def delete_profile(cls, id):
        to_delete = cls.objects.filter(id=id)
        to_delete.delete()

class Project(models.Model):
    """
    class that defines the projects to be uploaded on the site
    """
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def update_caption(self, update):
        self.caption = update
        self.save()

    @classmethod
    def delete_image(cls, id):
        to_delete = cls.objects.filter(id=id)
        to_delete.delete()

    @classmethod
    def get_by_user(cls, id):
        return cls.objects.filter(user=id)

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')

    @classmethod
    def search_image(cls, search_term):
        return cls.objects.filter(caption__icontains=search_term)

    @classmethod
    def get_img_by_id(cls, ide):
        picture = cls.objects.get(id=ide)
        return picture


class Comments(models.Model):
    """
    class that defines the post comments
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=1)
    comment = models.CharField(max_length=250)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_comment(self):
        self.save()

    @classmethod
    def get_by_image(cls, id):
        return cls.objects.filter(image=id)