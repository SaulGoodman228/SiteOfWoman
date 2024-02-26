#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteofwomen.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()




# git init - инициализирует локальный репозиторий
# git remote add origin https://github.com/SaulGoodman228/sqlAlchemyPractice.git - привязывает локальный репозиторий к облачному
# --------
#
# git add -A - смотрит есть ли изменения
# git commit -m"tables created" - сохраняеь т изменения в коде ЛОКАЛЬНО
# git push origin master - отправит все изменения в облако (на github)
# git rm --cached Spotify_Dataset_V3.csv