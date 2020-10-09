from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class ProductType(BaseModel):
  name = models.CharField(verbose_name=_("Product"), unique=True, null=False, blank=False)


class Product(BaseModel):
  code_validators = [
    MinLengthValidator(4),
    MaxLengthValidator(4),
  ]

  code = models.CharField(verbose_name=_("Code"), unique=True, validators=code_validators, null=False, blank=False)
  name = models.CharField(verbose_name=_("Product"), null=False, blank=False)
  description = models.CharField(verbose_name=_("Product description"), null=True, blank=True)

  product_type_fk = models.ForeignKey(
    ProductType,
    verbose_name=_("Product type"),
    on_delete=models.PROTECT,
    null=False,
    blank=False
  )


class ProductPrice(BaseModel):

  price = models.DecimalField(verbose_name=_("Price"), decimal_places=2)

  product_fk = models.ForeignKey(
    Product,
    verbose_name=_("Related product"),
    on_delete=models.PROTECT,
    null=False,
    blank=False
  )


class ProductFlowType(BaseModel):
  flow_type = models.CharField(verbose_name=_("Flow type"))


class ProductFlow(BaseModel):

  product_fk = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.PROTECT, null=False, blank=False)
  product_flow_type_fk = models.ForeignKey(
    ProductFlowType,
    verbose_name=_("Flow type"),
    on_delete=models.PROTECT,
    null=False,
    blank=False
  )
  user_to_fk = models.ForeignKey(User, verbose_name=_("To"), on_delete=models.PROTECT, null=True, blank=True)
