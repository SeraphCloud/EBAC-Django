import pytest
from blog.models import Post
from blog.factories import PostFactory

@pytest.mark.django_db
def test_post_creation():
    post = PostFactory()
    assert Post.objects.count() == 1