from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    
    def create_user(self, email, name, password=None):
        """
        Create a new user profile object.
        """
        if not email:
            raise ValueError('Users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user 

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser with given details.
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Represents a "user profile" inside our system. 
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Used to get a users full name.
        """
        return self.name

    def get_short_name(self):
        """
        Used to get a users short name.
        """
        return self.name

    def __str__(self):
        """
        Django uses this when it needs to convert the object to a string.
        """
        return self.email
    
    class Meta:
        db_table = 'user_profile'
        default_related_name = 'user_profiles'

class ProfileFeedItem(models.Model):
    """
    Profile status update.
    """
    user_profile = models.ForeignKey('UserProfile', on_delete=models.RESTRICT)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
    
    class Meta:
        db_table = 'profile_feed_item'
        default_related_name = 'profile_feed_items'