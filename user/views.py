from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import hashlib
from .models import User


# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']





        m = hashlib.md5()
        m.update(password1.encode())
        password_m = m.hexdigest()


        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            # 有可能 报错 - 重复插入 [唯一索引注意并发写入问题]
            print('--create user error %s' % (e))
            return HttpResponse('注册失败，请刷新页面重试')
        request.session['username'] = username
        request.session['uid'] = user.id
        # TODO 修改session存储时间为1天

        return HttpResponseRedirect('/index')




def login_view(request):
    if request.method == 'GET':
        # 获取登录页面
        # 检查登录状态，如果登录了，显示 ‘已登录’
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        # 检查Cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 处理数据
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % (e))
            return HttpResponse('错误，请重试')

        # 比对密码
        m = hashlib.md5()
        m.update(password.encode())

        if m.hexdigest() != user.password:
            return JsonResponse({"msg":"error"})

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        resp = HttpResponseRedirect('/index')
        # 判断用户是否 点选了 ‘记住用户名’
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        # 点选了 ->  Cookies 存储 username,uid 时间3天
        return resp





def logout_view(request):
    # 删除session值
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    # 删除Cookies
    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp

def ajax_view(request):
    if request.method=="GET":
        username=request.GET.get('username')
        print(username)
        old_user = User.objects.filter(username=username)
        if old_user:
            return JsonResponse({"msg":"ok"})
        else:return JsonResponse({"msg":"no"})

