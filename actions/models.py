
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user = models.ForeignKey('auth.User',
                             related_name = 'actions',
                             db_index = True,
                             on_delete = models.CASCADE)
    verb = models.CharField(max_length = 255)

    created = models.DateTimeField(auto_now_add = True,
                                   db_index = True)


    # : This will tell you the model for the relationship
    target_ct = models.ForeignKey(ContentType,
                                  blank = True,
                                  null = True,
                                  related_name = 'target_obj',
                                  on_delete = models.CASCADE)

    #  This will usually be a PositiveIntegerField to match Django's automatic primary key fields
    target_id = models.PositiveIntegerField(null = True,
                                            blank = True,
                                            db_index = True)

    # A field to define and manage the generic relation using the two previous fields
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ('-created',)
