# django-generate-code

A tool that can write some code for you. Cool, yeah?

## Lyricism

I indeed was jelous to see that RoR programmers can just do their ```rails generate``` and so on. 
It is realy not a necessary tool, but... let it be!

## generate\_model

Will create a new model class in models.py of *your_app_name*.

### Command arguments
In order to create a model you need to pass:
- application name (where models.py is located)
- your model name
- (optional) fields and their data types

```shell
python manage.py generate_model *your_app_name* *new_model_name* some_field:string some_other_field:int
```

### Field types

Can translate the following 'data types' to fields:
- string: models.CharField(min_length=255)
- slug: models.SlugField()
- text: models.TextField()
- url: models.URLField()
- integer: models.IntegerField()
- decimal: models.DecimalField(max_digits=9, decimal_places=2)

### Usage example

```shell
python manage.py generate_model_code myapp MyModel title:string price:decimal description:text
```

Will generate the following code in ```myapp/models.py```:

```python
class MyModel(models.Model):
    title = models.CharField(min_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
```
