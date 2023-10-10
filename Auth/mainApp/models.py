from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name,last_name,email,password=None):
        if not email:
            raise ValueError("Email field cannot be empty!")
        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,email,password=None):
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="Email Address", unique=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name"]
    def __str__(self) -> str:
        return self.email
    def has_perm(sefl,perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    @property
    def create_user_name(self):
        user_name="_".join([f[0]+f2[0] for f in self.first_name for f2 in self.last_name])
        return user_name
    


