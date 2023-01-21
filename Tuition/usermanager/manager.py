
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrattions = True


    def create_user(self , phone_number , password = None, **extra_fields):
        print("Inside custom user manager")
        if not phone_number:
            raise ValueError("Phone number required")
        user = self.model(phone_number = phone_number,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self , phone_number , password = None, **extra_fields) :
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)
        user = self.create_user(phone_number, password, **extra_fields)  
        # user.save()
        print("Inside Create Super User")
        return user  


    