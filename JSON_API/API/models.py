from django.db import models


'''Класи моделей БД'''


class Cldr(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'cldr'


class Docu(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'docu'


class Pd(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'pd'


class Pins(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'pins'


class Pvl(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'pvl'


class Run(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'run'


class Zm(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(verbose_name='volume', primary_key=True)

    class Meta:
        managed = True
        db_table = 'zm'


class Zuo(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'zuo'
