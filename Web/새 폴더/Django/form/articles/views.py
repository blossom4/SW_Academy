from django.shortcuts import render
from .models import Article
from .forms import ArticleForm, ArticleModelForm

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-id')

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    form = ArticleForm()
    model_form = ArticleModelForm()

    context = {
        'form': form,
        'model_form': model_form,
    }
    return render(request, 'articles/new.html', context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 모델폼을 이용한 데이터 저장
    model_form = ArticleModelForm(request.POST)
    if model_form.is_valid():
        model_form.save()
    
    return redirect('articles:new')

def new_create(request):
    # 5. POST방식으로 요청 (잘못된 데이터 저장요청)
    # 10. POST방식으로 요청 (옳은 데이터 저장요청)
    if request.method == 'POST':
        # 6. 빈 종이에 데이터를 입력
        # 11. 옳은 데이터 입력
        form = ArticleModelForm(request.POST)
        # 7. 유효성검사
        # 12. 유효성검사 성공
        if form.is_valid():
            # 13. 데이터 저장
            article = form.save()
            # 14. 상세페이지 이동
            return redirect('articles:detail', article.pk)
    # 1. GET방식으로 요청했으면 빈종이를 달라는 의미이다.
    else:
        # 2. 빈종이 생성 (모델폼)
        form = ArticleModelForm()
    # 3. 빈종이를 사용자에게 전송
    # 8. 유효성검사를 통과한 데이터만 입력되어 있는 종이를 전송 (통과한 입력은 살려주는 것이 좋다.)
    context = {
        'form': form
    }
    # 4. html파일 렌더링 (빈종이 포함)
    # 9. html파일 렌더링 (유효성 검사를 통과한 데이터 포함)
    return render(request, 'articles/new_create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 최신데이터 저장
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # 기존데이터 출력
    else:
        form = ArticleModelForm(instance=article)

    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)
    