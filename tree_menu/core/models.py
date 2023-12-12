from django.db import models


class NameURLModel(models.Model):
    """Абстрактная модель с именем."""

    name = models.CharField(max_length=250, verbose_name='имя')
    directory = models.CharField(max_length=200, verbose_name='директория')
    url = models.URLField(verbose_name='адрес', blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self) -> str:
        """Представление модели при выводе.

        Returns:
            Строка поля name.
        """
        return self.name
