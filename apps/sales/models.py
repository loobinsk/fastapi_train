from django.db import models
from django.core.validators import MinValueValidator

class Sale(models.Model):
    scenario_id = models.IntegerField(verbose_name='Сценарий')
    date = models.DateField(verbose_name='Дата', help_text='Дата продажи')
    product_name = models.CharField(max_length=255, verbose_name='Название продукта', help_text='Название продукта')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма',
        validators=[MinValueValidator(0)],
        help_text='Сумма продажи'
    )
    vat_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='НДС',
        validators=[MinValueValidator(0)],
        help_text='НДС'
    )
    description = models.TextField(verbose_name='Описание', help_text='Описание продажи')

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return self.product_name
