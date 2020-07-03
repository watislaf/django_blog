from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# для собственного выделения обьектов, теперь запись  Post.published.filter(title__startswith='Who') будет работать
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'published')

class Post(models.Model):
    objects = models.Manager()  # The default manager.
    published = PublishedManager()

    title = models.CharField(max_length = 250)
    # This is the field for the post title. This field is CharField, which
    # translates into a VARCHAR column in the SQL database

    slug = models.SlugField(max_length = 250,
                            unique_for_date = 'publish')
    author = models.ForeignKey(
        User, on_delete = models.CASCADE,
        related_name = 'blog_posts')
    # ForeignKey -> a many-to-one relationship
    # on_delete

    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    # DateField.auto_now
    # Значение поля будет автоматически установлено
    # в текущую дату при каждом сохранении объекта.
    # DateField.auto_now_add
    # Значение поля будет автоматически установлено в
    # текущую дату при создании(первом сохранении) объекта.

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length = 10,
                              choices = STATUS_CHOICES,
                              default = 'draft')

    # каноничное url
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args = [self.publish.year,
                               self.publish.month,
                               self.publish.day,
                               self.slug],
                       )

    class Meta:
        ordering = ('-publish',)
        # u tell Django to sort results
        # by the publish field in descending order by default when you query the database.

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete = models.CASCADE,
                             related_name = 'comments')
    # related_name используется для обращения от post к его комментариям
    name = models.CharField(max_length = 80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
