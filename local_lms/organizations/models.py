from django.db import models

from local_lms.utils.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="organizations/logos/", blank=True, null=True)
    members = models.ManyToManyField(
        "users.User",
        related_name="organizations",
        blank=True,
    )

    def __str__(self):
        return self.name
