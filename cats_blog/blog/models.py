from django.contrib.auth import get_user_model
from django.db import models


CHOICES = (
        ('Gray', 'Серый'),
        ('Black', 'Чёрный'),
        ('White', 'Белый'),
        ('Ginger', 'Рыжий'),
        ('Mixed', 'Смешанный'),
    )


User = get_user_model()


class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=CHOICES)
    birth_year = models.IntegerField()
    breed = models.CharField(max_length=150)
    owner = models.ForeignKey(
        User,
        related_name='cats',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owner'],
                name='unique_name_owner'
            )
        ]

    def __str__(self):
        return self.name
