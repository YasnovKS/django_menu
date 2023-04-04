from django.db import models


class MenuItem(models.Model):
    '''Class for menu items'''

    name = models.CharField(max_length=50,
                            verbose_name='Название',
                            )
    url = models.URLField(verbose)
    position = models.PositiveIntegerField(default=0,
                                           verbose_name='Уровень вложенности',
                                           )

    class Meta:
        ordering = ['position']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    '''intermediate class for many-to-many relationship'''

    parent = models.ForeignKey(MenuItem,
                               on_delete=models.CASCADE,
                               related_name='main_menu',
                               )
    child = models.ForeignKey(MenuItem,
                              on_delete=models.DO_NOTHING,
                              related_name='sub_menu',
                              null=True,
                              )

    class Meta:
        constraints = [models.UniqueConstraint(fields=['parent', 'child'],
                                               name='unique_menu_relation'
                                               ),
                       ]

    def __str__(self) -> str:
        if not self.child:
            return f'Меню {self.parent}'
        return f'Подменю {self.child} меню {self.parent}'
