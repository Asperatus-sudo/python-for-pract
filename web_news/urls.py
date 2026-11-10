"""
URL configuration for web_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from news import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path(
        "article/<int:article_id>/",
        views.article_detail,
        name="article_detail",
    ),
    path(
        "category/<str:category_name>/",
        views.category,
        name="category_detail",
    ),
    path(
        "article/<int:article_id>/edit/",
        views.edit_article,
        name="article_edit"
    ),
    path(
        "test-form/",
        views.test_form,
        name="test_form",
    ),
    path(
        "add-article/",
        views.add_article,
        name="add_article",
    ),
    path(
        "article-created/",
        views.article_created,
        name="article_created",
    ),
    path(
        "article/<int:article_id>/delete/",
        views.delete_article,
        name="article_delete",
    ),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
