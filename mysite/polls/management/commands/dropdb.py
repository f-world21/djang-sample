import MySQLdb

from django.core.management.base import BaseCommand

import environ


class Command(BaseCommand):
    help = 'Drop database'

    def handle(self, *args, **options):
        print('Drop database!')
        database_name = 'django-sample32_development'
        env = environ.Env()
        db = MySQLdb.connect(host='localhost', user=env('DATABASE_USER'), passwd=env('DATABASE_PASSWORD'))
        # db = MySQLdb.connect(host='mysql', user='root', passwd='password1')
        cursor = db.cursor()
        sql = f'DROP DATABASE IF EXISTS `{database_name}`'
        print(cursor.execute(sql))
        db.close()
