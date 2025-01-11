from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        moderators_group = Group.objects.create(name='Moderators')
        can_un_publish_product_permission = Permission.objects.get(codename='can_un_publish_product')
        moderators_group.permissions.add(can_un_publish_product_permission)