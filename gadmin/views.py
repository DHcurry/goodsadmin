from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import re
from .models import User,Goods,TypeInfo,StoreInfo
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import View

# Create your views here.
def test(request):
    va = User.objects.all()
    goods = Goods.objects.all()
    return render(request, 'test.html', {"va":va,"goods":goods})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/gadmin/logout_success')

def logout_success(request):
    return render(request, 'logout.html')

def store_info(request):
    store = StoreInfo.objects.all()
    context = {"store":store}
    return render(request, 'store.html',context=context)

def store_detail(request, store_id):
    store = StoreInfo.objects.get(id=store_id)
    g = Goods.objects.filter(store=store_id)
    return render(request, 'store_detail.html',{'store':store,'goods':g})

def goods(request):
    goods = Goods.objects.all()
    return render(request, 'goods.html', {'goods':goods})

class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        tel = request.POST.get('tel')
        email = request.POST.get('email')

        if not all([username, password, email]):
            #  这个表示数据不完全就要做如下处理
            return render(request, 'register.html', {'errmsg':'数据不完整'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户已存在'})

        # user = User()
        # user.username = username
        # user.password = password
        # user.tel = tel
        # user.email = email
        user = User.objects.create_user(username=username, email=email, password=password, tel=tel)
        user.save()

        return HttpResponseRedirect('/gadmin/index/')

class LoginView(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        # 验证数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg':'数据不完整'})
        
        # 应答(验证账号密码比对正确)
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html', {"errmsg":'用户不存在'})
        else:
            # 判断是否记住用户名
            login(request, user)
            return HttpResponseRedirect('/gadmin/index') 

class IndexView(View):

    def get(self, request):
        goods = Goods.objects.all()[:10]
        ty = TypeInfo.objects.all()[:10]
        context = {"goods":goods,"type":ty}
        return render(request, 'index.html',context=context)

    
