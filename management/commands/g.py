from django.core.management.base import BaseCommand


def generate_model(name, *fields):
    """
    >>> print generate_model('MyModel', 'title:string', \
        'rate:integer', 'price:decimal', 'description:text')
    class MyModel(models.Model):
        title = models.CharField(min_length=255)
        rate = models.IntegerField()
        price = models.DecimalField(max_digits=9, decimal_places=2)
        description = models.TextField()
    <BLANKLINE>

    >>> print generate_model('MyModel')
    class MyModel(models.Model):
        pass
    <BLANKLINE>

    >>> print generate_model('MyModel', 'foo:bar')
    Traceback (most recent call last):
    ...
    KeyError: 'bar'
    """
    ret = "class %s(models.Model):\n" % name

    if not fields:
        ret += "    pass\n"
        return ret

    field_samples = {
        # basic text fields
        'string': 'models.CharField(min_length=255)',
        'slug': 'models.SlugField()',
        'text': 'models.TextField()',
        'url': 'models.URLField()',

        # basic numeric fields
        'integer': 'models.IntegerField()',
        'decimal': 'models.DecimalField(max_digits=9, decimal_places=2)',
    }

    for f in fields:
        field_name, type_shortcut = f.split(":")
        field_definition = field_samples[type_shortcut]

        ret += "    %s = %s\n" % (field_name, field_definition)

    return ret


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

    def handle(self, generate_what, *args, **kwargs):
        """
        >>> c = Command()
        >>> c.handle('model')
        Usage: g model <Appication.Model> <field:type> <field:type> ...
        """
        if generate_what == 'model':
            if not args:
                print 'Usage: g model <Appication.Model> <field:type> <field:type> ...'
                return

            module_descr = args[0]
            field_args = args[1:]
