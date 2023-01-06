from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    """Подсписки."""

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]


class Post(models.Model):
    """Структура поста."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey('Group', blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='post', verbose_name='Группа',
                              help_text='Группа, к которой относиться пост')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        """Читабельность объекта."""
        return self.text


class Group(models.Model):
    """Группы."""

    title = models.CharField(max_length=200, verbose_name='Название',
                             help_text='Введите название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание',
                                   help_text='Введите описание')

    def __str__(self):
        """Читабельность объекта."""
        return self.title


class Comment(models.Model):
    """Комментарии."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        """Читабельность объекта."""
        return self.text
