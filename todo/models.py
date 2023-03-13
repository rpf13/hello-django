from django.db import models


# Create your models here.
# Importing all possible built in Django model classes
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # This will overwrite the default naming for the items in the tasklist
    # with our given name.
    # self in this case is the class itself as its own argument
    def __str__(self):
        return self.name
