from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    inmenu = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    # header_image = models.ImageField(null=True, blank=True,
    #      upload_to="blog-images",
    #      storage=S3Storage())
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    intro = models.TextField(max_length=1000, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Content(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.slug
