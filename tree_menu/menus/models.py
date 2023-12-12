from typing import Any

from django.core.exceptions import ValidationError
from django.db import models

from core.constants import BASE_URL
from core.models import NameURLModel


class MenuItem(NameURLModel):
    """Модель элемента меню."""

    parent = models.ForeignKey(
        'self',
        verbose_name='родительский элемент',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
    )
    is_root = models.BooleanField(verbose_name='корневой')
    level = models.PositiveSmallIntegerField(
        verbose_name='уровень',
        default=1,
        blank=True,
        null=True,
    )
    menu = models.ForeignKey(
        'menus.Menu',
        verbose_name='меню',
        on_delete=models.CASCADE,
        related_name='items',
    )

    class Meta:
        verbose_name = 'элемент меню'
        verbose_name_plural = 'элементы меню'

    def clean(self, *args: Any, **kwargs: Any) -> None:
        """Метод для валидации модели."""
        super().clean(*args, **kwargs)
        if self.parent == self:
            raise ValidationError(
                {'parent': 'Элемент не может быть родителем самому себе'},
            )
        if self.is_root:
            if self.parent:
                raise ValidationError(
                    {
                        'is_root': (
                            'При наличии родительского элемента '
                            'элемент не может быть корневым'
                        ),
                    },
                )
        if not self.is_root:
            if not self.parent:
                raise ValidationError(
                    {
                        'parent': (
                            'Если элемент не корневой, необходимо '
                            'указать родительский элемент'
                        ),
                    },
                )
        if self.is_root:
            if self.menu.root_item and self.menu.root_item != self:
                raise ValidationError(
                    {'is_root': 'У данного меню уже есть корневой элемент'},
                )

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Метод для сохранения модели."""
        if self.parent:
            self.url = '/'.join(
                [self.parent.url, self.directory],  # type: ignore[list-item]
            )
            self.level = self.parent.level + 1  # type: ignore[operator]
            super().save(*args, **kwargs)
        else:
            self.url = '/'.join(
                [BASE_URL, self.menu.directory, self.directory],
            )
            self.level = 0
            super().save(*args, **kwargs)
            self.menu.root_item = self
            self.menu.save()


class Menu(NameURLModel):
    """Модель меню."""

    root_item = models.ForeignKey(
        MenuItem,
        verbose_name='корневой элемент',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='menu_base',
    )

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Метод для сохранения модели."""
        self.url = '/'.join([BASE_URL, self.directory])
        super().save(*args, **kwargs)
