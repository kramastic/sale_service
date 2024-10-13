from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def image_path(instance, filename):
    return "images/user_{0}/{1}".format(instance.user.id, filename)


class Objects(models.Model):

    class Meta:
        verbose_name_plural = "Объекты"
        verbose_name = "Объект"
        ordering = ["id"]

    category = models.CharField(
        max_length=10, verbose_name="Категория", null=False
    )
    title = models.CharField(
        max_length=100, verbose_name="Название объекта", null=False
    )
    address = models.TextField(verbose_name="Адрес", null=False)
    description = models.TextField(verbose_name="Описание", null=False)
    price = models.IntegerField(verbose_name="Цена", null=False)
    image_id = models.ImageField(
        verbose_name="Фотографии", upload_to=image_path, null=True, blank=True
    )
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.PROTECT, editable=False
    )
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время размещения"
    )

    def get_absolute_url(self):
        return reverse("show_adv", kwargs={"pk": self.id})
