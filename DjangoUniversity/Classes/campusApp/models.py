from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    Campus = models.CharField(max_length=60, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the campus, campus ID and state
        # field as a tuple tod display in the browser instead of the default titles
        display_location = '({0.Campus_ID}) {0.Campus}: {0.State}'
        return display_location.format(self)

    # Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
