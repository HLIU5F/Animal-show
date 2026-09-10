from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# 确保导入所有需要的模型
from .models import Animal, Like, Comment


def index(request):
    """首页视图"""
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', {'animals': animals})


def animal_list(request):
    """
    列表页视图 (包含搜索功能)
    注意：这里合并了你之前的两个 animal_list，保留了搜索功能
    """
    query = request.GET.get('q')  # 获取搜索关键词
    animals = Animal.objects.all()

    if query:
        # 如果有关键词，进行过滤
        animals = animals.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # 渲染时传入 animals 和 query
    return render(request, 'animals/list.html', {'animals': animals, 'query': query})


def animal_detail(request, pk):
    """详情页视图 (包含评论功能)"""
    # 1. 获取动物对象
    animal = get_object_or_404(Animal, pk=pk)

   # 2. 处理评论提交
    if request.method == 'POST':
        # 【新增】先检查用户是否已经登录
        if request.user.is_authenticated:
            content = request.POST.get('content')
            if content:
                # 只有登录了，才执行创建评论的操作
                Comment.objects.create(
                    animal=animal,
                    user=request.user,
                    content=content
                )
                # 提交后刷新页面 (PRG模式)
                # 注意：这里的 return 必须比上面的 if content: 多缩进一级
                return redirect('animals:animal_detail', pk=pk)
    # 3. 渲染页面 (注意路径加上了 animals/)
    return render(request, 'animals/detail.html', {'animal': animal})


@login_required
def toggle_like(request, pk):
    """点赞/取消点赞视图"""
    if request.method == "POST":
        animal = get_object_or_404(Animal, pk=pk)
        like_obj, created = Like.objects.get_or_create(animal=animal, user=request.user)

        if not created:
            like_obj.delete()
            is_liked = False
        else:
            is_liked = True

        # 如果是 AJAX 请求，返回 JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'is_liked': is_liked, 'like_count': animal.likes.count()})

        # 否则重定向回详情页
        return redirect('animal_detail', pk=pk)

    # 如果不是 POST 请求，也重定向回去防止误触
    return redirect('animal_detail', pk=pk)


def animal_add(request):
    """添加动物视图"""
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        age = request.POST.get('age')
        # 建议加上 description 和 image 的处理，否则添加的动物没图没描述
        description = request.POST.get('description', '')

        Animal.objects.create(
            name=name,
            species=species,
            age=age,
            description=description
        )
        return redirect('list')  # 跳转到列表页

    return render(request, 'animals/add.html')