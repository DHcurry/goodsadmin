from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='最近更新时间')

    class Meta:
        abstract = True


class StoreInfo(BaseModel):
    name = models.CharField(max_length=50, verbose_name='仓库名')
    desc = models.CharField(max_length=200, verbose_name='描述')
    addr = models.CharField(max_length=50, verbose_name='地址')
    max_store = models.IntegerField(default=1, verbose_name='最大库存')
    objects = models.Manager()

    class Meta:
        verbose_name = verbose_name_plural = '仓库信息'
    
    def __str__(self):
        return self.name
    

class User(BaseModel, AbstractUser):
    sex_choise = ((1,'男'),(0,'女'))
    job_choise = (
        (0, '员工'),
        (1, '仓库管理员'),
        (2, '主管'),
        (3, '经理'),
    )
    tel = models.CharField(max_length=11, verbose_name='电话')
    con_store = models.ForeignKey(to='StoreInfo', on_delete=models.CASCADE, verbose_name='所属仓库',null=True)
    sex = models.SmallIntegerField(choices=sex_choise, verbose_name='性别',null=False ,default=1)
    job = models.SmallIntegerField(choices=job_choise, verbose_name='工种',null=False,default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class TypeInfo(BaseModel):
    name = models.CharField(max_length=50, verbose_name='分类名')
    image = models.ImageField(upload_to='typeinfo', verbose_name='总类图片')
    desc = models.CharField(max_length=200, verbose_name='描述')
    objects = models.Manager()
    
    class Meta:
        verbose_name = verbose_name_plural = "零件种类"

    def __str__(self):
        return self.name

class Goods(BaseModel):
    name = models.CharField(max_length=50, verbose_name='物品名称')
    desc = models.CharField(max_length=200, verbose_name='描述')
    goodstype = models.ForeignKey('TypeInfo', verbose_name='商品种类',on_delete=models.CASCADE, null=True,related_name="goods")
    store = models.ForeignKey('StoreInfo',verbose_name='所属仓库', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='Goods', verbose_name='商品图片')
    objects = models.Manager()

    class Meta:
        verbose_name = verbose_name_plural = '零件信息'

    def __str__(self):
        return self.name