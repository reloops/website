from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Pastline,Futureline


# Create your views here.
def index_view(request):
    pl1=Pastline.objects.count()
    pl2=Futureline.objects.count()
    print(pl1)
    context={
        'total1': pl1,
        'total2':pl2
             }
    #print(context.items())
    return render(request, 'index/index.html', context)


def addpast_view(request):
    if request.method == "POST":
        detail = request.POST['detail']
        username = request.POST['username']
        try:
            pastline = Pastline.objects.create(username=username, detail=detail)
        except Exception as e:
            # 有可能 报错 - 重复插入 [唯一索引注意并发写入问题]
            print('--create user error %s' % (e))
            return HttpResponse('注册失败，请刷新页面重试')
        return JsonResponse({"msg": "ok"})
    if request.method=="GET":
        total=Pastline.objects.count()
        num=request.GET.get('num')
        pl=Pastline.objects.all()[total-int(num)-1]
        res={
            "username": pl.username,
            "datetime": pl.createtime,
            "detail":pl.detail
        }
        return JsonResponse(res)

def addfuture_view(request):
    if request.method == "POST":
        detail = request.POST['detail']
        username = request.POST['username']
        targetdatetimt=request.POST['futuredatetime']
        try:
            futureline = Futureline.objects.create(username=username, detail=detail,targettime=targetdatetimt)
        except Exception as e:
            # 有可能 报错 - 重复插入 [唯一索引注意并发写入问题]
            print('--create user error %s' % (e))
            return HttpResponse('注册失败，请刷新页面重试')
        return JsonResponse({"msg": "ok"})
    if request.method=="GET":
        total=Futureline.objects.count()
        num=request.GET.get('num')
        pl=Futureline.objects.all()[int(num)]
        res={
            "username": pl.username,
            "datetime": pl.targettime,
            "detail":pl.detail
        }
        return JsonResponse(res)

def reflash_view(request):
    if request.method=="GET":
        total=Pastline.objects.count()
        divnum=request.GET.get('divnum')
        ci=request.GET.get('ci')
        pl=Pastline.objects.all()[total-int(divnum)-int(ci)]
        res={
            "datetime": pl.createtime,
            "detail": pl.detail
        }
    return JsonResponse(res)


def reflashf_view(request):
    if request.method=="GET":
        total=Futureline.objects.count()
        divnum=request.GET.get('divnum')
        ci=request.GET.get('ci')
        pl=Futureline.objects.all()[int(divnum)+int(ci)]

        res={
            "futuredatetime":pl.targettime,
            "detail":pl.detail
        }
    return JsonResponse(res)