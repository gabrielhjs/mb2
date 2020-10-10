from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel
from apps.product.models import Product


class Card(BaseModel):
  user_card_fk = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.PROTECT, null=False, blank=False)


class CardItems(BaseModel):
  class Meta:
    unique_together = ("card_fk", "product_fk")

  amount = models.PositiveIntegerField(_("Amount"), null=False, blank=False)

  card_fk = models.ForeignKey(Card, verbose_name=_("Card"), on_delete=models.CASCADE, null=False, blank=False)
  product_fk = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE, null=False, blank=True)
