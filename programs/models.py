from uuid import uuid4

from django_countries.fields import CountryField

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class College(models.Model):
    """
    College, Univerisity or Inistitute
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=30, unique=True)
    summary = models.TextField(blank=True)
    country = CountryField()
    city = models.CharField(max_length=60)
    link = models.URLField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.short_name


class Program(models.Model):
    """
    College/Univerisity programs
    """
    BACHELOR = 'BD'
    MASTERS = 'MD'
    PHD = 'PD'

    DEGREE_CHOICE = (
        (BACHELOR, 'Bachelor'),
        (MASTERS, 'Masters'),
        (PHD, 'Ph.D')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    degree_type = models.CharField(max_length=2, choices=DEGREE_CHOICE)
    summary = models.TextField(blank=True)
    program_start_date = models.DateField(blank=True, null=True)
    application_start_date = models.DateField()
    application_end_date = models.DateField()
    link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', )
        default_related_name = 'programs'

    def __str__(self):
        return self.title


class Requirement(models.Model):
    """
    Requirements for a program application
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_optional = models.BooleanField(default=False)
    link = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'program'
        default_related_name = 'requirements'

    def __str__(self):
        return self.name


class Application(models.Model):
    """
    Application to a program
    """
    IN_PROGRESS = 'IP'
    SUBMITTED = 'SU'
    ACCEPTED = 'AC'
    REJECTED = 'RE'

    STATUS_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (SUBMITTED, 'Submitted'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    completed_requirements = models.ManyToManyField(Requirement)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=IN_PROGRESS
    )
    remark = models.TextField(blank=True)
    link = models.URLField(max_length=255, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-started_at', )
        default_related_name = 'applications'

    def __str__(self):
        return f'Application for {self.program}'
