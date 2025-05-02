import factory
from faker import Faker
from django.contrib.auth import get_user_model
from blog.models import Post

fake = Faker()
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda x: fake.email())
    username = factory.LazyAttribute(lambda x: fake.user_name())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop('password', None)
        user = super()._create(model_class, *args, **kwargs)
        if password:
            user.set_password(password)
            user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda x: fake.sentence())
    slug = factory.LazyAttribute(lambda x: fake.slug())
    author = factory.SubFactory(UserFactory)
    content = factory.LazyAttribute(lambda x: fake.text())
    created_on = factory.LazyAttribute(lambda x: fake.date_time_this_year())
    status = 0