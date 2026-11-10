# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# Create your views here.

# def index(request):
#     return HttpResponse("Главная страница новостей")

def index(request):
    articles = Article.objects.filter(
        is_published=True
    ).order_by("-created_at")

    context = {
        "articles": articles,
    }

    return render(
        request,
        "news/index.html",
        context,
    )


def about(request):
    return HttpResponse("О нашем новостном издании")


# def index(request):
#     return render(request, "news/index.html")

# def index(request):
#     context = {
#         "headline": "лололо",
#         "title": "В городе открылся новый парк",
#         "text": (
#             "В центральной части города открылся новый парк "
#             "с прогулочными дорожками и детской площадкой."
#         ),
#         "author": "Редакция",
#     }
#     return render(request, "news/index.html", context)

# context = {
#     "article_1": "Первая новость",
#     "article_2": "Вторая новость",
#     "article_3": "Третья новость",
# }

# def index(request):
#     context = {
#         "title": "Главные новости дня",
#         "articles": [
#             "В городе открылся новый парк",
#             "Учёные представили новую технологию",
#             "В университете начался учебный год",
#         ],
#     }
#     return render(request, "news/index.html", context)

# def category(request):
#     context = {
#         "title": "Технологии",
#         "articles": [
#             "Представлена новая модель смартфона",
#             "Компания выпустила обновление программного обеспечения",
#             "Учёные разработали новый процессор",
#         ],
#     }
#     return render(request, "news/category.html", context)

def category(request, category_name=None):
    if category_name is None:
        articles = Article.objects.filter(
            is_published=True
        ).order_by("-created_at")

        category_name = "Все категории"
    else:
        articles = Article.objects.filter(
            is_published=True,
            category__iexact=category_name,
        ).order_by("-created_at")

    context = {
        "articles": articles,
        "category_name": category_name,
    }

    return render(
        request,
        "news/category.html",
        context,
    )


def about(request):
    context = {
        "title": "Информация о нас",
        "articles": [
            "Публикуем самые свежие новости",
            "Нашей компании уже более 15 лет",
        ],
    }
    return render(request, "news/about.html", context)


def contact(request):
    context = {
        "title": "Контактные данные",
        "articles": [
            "номер телефона",
            "имеил",
        ],
    }
    return render(request, "news/contact.html", context)


def article_detail(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id,
        is_published=True,
    )

    context = {
        "article": article,
    }

    return render(
        request,
        "news/article_detail.html",
        context,
    )


def edit_article(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id
    )

    if request.method == "POST":
        form = ArticleForm(
            request.POST,
            request.FILES,
            instance=article
        )

        if form.is_valid():
            article = form.save()

            if article.is_published:
                return redirect(
                    "article_detail",
                    article_id=article.id
                )

            return redirect("home")

    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }

    return render(
        request,
        "news/edit_article.html",
        context
    )


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id
    )

    if request.method == "POST":
        article.delete()
        return redirect("home")

    context = {
        "article": article,
    }

    return render(
        request,
        "news/delete_article.html",
        context
    )


def test_form(request):
    context = {}

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        context = {
            "title": title,
            "content": content,
        }

    return render(
        request,
        "news/test_form.html",
        context,
    )


def add_article(request):
    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()

            return redirect("article_created")


    else:
        form = ArticleForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "news/add_article.html",
        context,
    )


def article_created(request):
    return render(
        request,
        "news/article_created.html",
    )
