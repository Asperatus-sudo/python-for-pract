from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article

        fields = [
            "title",
            "content",
            "category",
        ]

        labels = {
            "title": "Заголовок новости",
            "content": "Текст новости",
            "category": "Категория",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите заголовок новости",
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Введите текст новости",
                }
            ),

            "category": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Например: Спорт",
                }
            ),
        }