from django.db import models


class Food(models.Model):
    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюды'

    name = models.CharField('название', max_length=150, unique=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)
    image = models.ImageField(verbose_name='рисунок', upload_to='image/', null=True, blank=True)
    description = models.CharField('описание', max_length=500)
    category = models.ForeignKey('food_service.Categories', on_delete=models.SET_NULL, verbose_name='Категории блюд', null=True, blank=True)




class Categories(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField('название', max_length=150, unique=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    


class FoodMakeup(models.Model):
    class Meta:
        verbose_name = ' Готовое блюдо'
        verbose_name_plural = ' Готовые блюды'

    name = models.CharField('название', max_length=150, unique=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')



class FoodSize(models.Model):
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    name = models.CharField('название', max_length=150, unique=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
    price = models.IntegerField('Цена блюд')



class FoodWeight(models.Model):
    class Meta:
        verbose_name = 'Вес'
        verbose_name_plural = 'Весы'

    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
    value = models.IntegerField('вес')






class OrderFood(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"
    
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    update_at = models.DateTimeField('дата обновления', auto_now=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
    name = models.CharField('Фамилия Имя', max_length=100)
    email = models.EmailField("Эл. адрес", max_length=50)
    phone = models.CharField("Телефон", max_length=20)
    address = models.CharField('Адрес', max_length=150 )
    comment = models.CharField('Комментарии', max_length=300)
    




        