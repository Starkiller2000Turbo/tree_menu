import logging
from base64 import b64encode
from secrets import token_bytes
from typing import Any

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Команда для импорта ингредиентов из файла."""

    def handle(self, *args: Any, **options: Any) -> None:
        """Create a secret key.

        Returns:
            An example of a random secret key.
        """
        logger.error(b64encode(token_bytes(32)).decode())
