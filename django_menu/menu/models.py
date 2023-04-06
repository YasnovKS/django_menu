from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    '''Class for creating main menu.'''
    title = models.CharField(max_length=50,
                             verbose_name='Название'
                             )

    def __str__(self) -> str:
        return self.title


class MenuItem(MPTTModel):
    '''Class for menu items.'''

    name = models.CharField(max_length=50,
                            verbose_name='Название',
                            )
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children'
                            )
    main_menu = models.ForeignKey(Menu,
                                  on_delete=models.CASCADE,
                                  verbose_name='Меню')

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self) -> str:
        return str(self.name)
