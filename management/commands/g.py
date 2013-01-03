from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    G example:

    python manage.py g model App.MyModel title:string price:decimal \
     description:text

    Will add to app/models.py code like this:

    class MyModel(models.Model):
        title = models.CharField(min_length=255)
        price = models.DecimalField(max_digits=9, decimal_places=2)
        description = models.TextField()
    """
    help = 'Generates useful code for you'

    def handle(self, *args, **kwargs):
        pass
