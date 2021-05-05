import MySQLdb

from django.core.management.base import BaseCommand

import environ


class Command(BaseCommand):
    help = 'Create database'

    def handle(self, *args, **options):
        print('create database!')
        database_name = 'django-sample32_development'
        env = environ.Env()
        db = MySQLdb.connect(host='localhost', user=env('DATABASE_USER'), passwd=env('DATABASE_PASSWORD'))
        cursor = db.cursor()
        sql = f'CREATE DATABASE IF NOT EXISTS `{database_name}` DEFAULT CHARACTER SET `utf8mb4`'
        print(cursor.execute(sql))
        db.close()
