
### Problem Statement 2

Suppose we have two websites with different database schema and we have
to keep data of the user table the same in both databases, suppose we add
one user in the first website then it should automatically be added in another
website and vice versa. How can we do that using Django?

This can be achieved using a CustomUser class and CustomUserManager.

Let us assume two websites, website1 and website2.

The User model for website1 is CustomUser1:

```
user2_register_view_url = "https://website2.com/register_user2/"

def register_user2(user_name, email, password):
   data = {
       "user_name": user_name,
       "email": email,
       "password": password
   }
   res = requests.post(user2_register_view_url, data = data)


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_name, email, password):
        """
        Creates and saves a User with the given username and password.
        """
        if not user_name:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email')

        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            user_name=user_name,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)

        register_user2(user.user_name, user.email, password)

        return user

    def create_superuser(self, user_name, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            user_name=user_name,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser1(AbstractBaseUser, PermissionsMixin):
    """The Custom User model"""
    user_name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(blank=True, unique=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    interests = models.ManyToManyField(Interest)
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    objects = CustomUser1Manager()

```

Here, the create_user() method in the CustomUserManager is used to create a new CustomUser1.

Inside create_user(), we can call register_user2(), and pass it the user_name, email and password. 

register_user2() sends a POST request to the view on website2 which is responsible for registering a User on website2.

Thus, everytime an object of CustomUser1 is created, User object for website2 will also be created.

Same can be implemented on website2 to achieve vice-versa.