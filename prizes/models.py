from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    class that extends the user profile from django
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)
    contact_info = models.CharField(max_length=250)

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
    title = models.CharField(max_length=30)
    landing_page = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def update_description(self, update):
        self.description = update
        self.save()

    @classmethod
    def delete_project(cls, id):
        to_delete = cls.objects.filter(id=id)
        to_delete.delete()

    @classmethod
    def get_by_user(cls, id):
        return cls.objects.filter(user=id)


    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')

    @classmethod
    def search_project(cls, search_term):
        return cls.objects.filter(caption__icontains=search_term)

    @classmethod
    def get_project_by_id(cls, ide):
        project = cls.objects.get(id=ide)
        return project


class Ratings(models.Model):
    """
    class that defines the post comments
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField()
    pub_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.project

    def save_rating(self):
        self.save()

    @classmethod
    def get_by_project(cls, id):
        return cls.objects.filter(project=id)