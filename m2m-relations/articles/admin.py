from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Article, Scope, ArticleInScope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ArticleInScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data and not form.cleaned_data.get('is_main'):
                count += 1

        if count > 1:
            raise ValidationError('Укажите основной раздел')
        if count < 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleInScopeInLine(admin.TabularInline):
    model = ArticleInScope
    formset = ArticleInScopeInLineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInScopeInLine]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleInScopeInLine]

