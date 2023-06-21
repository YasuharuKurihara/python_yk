from django.views import generic
from .models import GoodsGroup, CustomGoods
from .forms import GroupCreationForm, CustomGoodsCreationForm, CustomGoodsSearchForm


class GroupCreateView(generic.CreateView):
    model = GoodsGroup
    success_url = '/search/group_create'
    template_name = 'search/group_create.html'
    form_class = GroupCreationForm


class CustomGoodsCreateView(generic.CreateView):
    model = CustomGoods
    success_url = '/search/custom_goods_create'
    template_name = 'search/custom_goods_create.html'
    form_class = CustomGoodsCreationForm

class CustomGoodsListView(generic.ListView):
    model = CustomGoods
    form_class = CustomGoodsSearchForm
    template_name = 'search/custom_goods_list.html'
    paginate_by = 1
    # 並び替えをする order_by('フィールド名') 昇順
    # order_by('-フィールド名') -をつける降順
    queryset = CustomGoods.objects.all().order_by('-id')

    #テンプレートファイルに検索フォームを渡せる
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomGoodsSearchForm(self.request.GET)
        return context

    # def get_queryset(self):
    #
    #     queryset = super().get_queryset()
    #     #GETパラメータをフォームに紐づける
    #     form = CustomGoodsSearchForm(self.request.GET)
    #     form.is_valid()
    #
    #     #値 = フォームオブジェクト.ckeaned_data.get('フィールド名')
    #     name = form.cleaned_data.get('name')
    #     management_code = form.cleaned_data('management_code')
    #     price_begin = form.cleaned_data('price_begin')
    #     price_end = form.cleaned_data('price_end')
    #     goup = form.cleaned_data('group')
    #
    #     if name:
    #         quertset = queryset.filter(name=name)
    #     if management_code:
    #         quertset = queryset.filter(management_code=management_code)
    #     if price_begin:
    #         quertset = queryset.filter(price__gte=price_begin)
    #     if name:
    #         quertset = queryset.filter(price__end=price_end)
    #     if name:
    #         quertset = queryset.filter(group=group)
    #     if name:
    #         quertset = queryset.filter(name=name)

    def get_queryset(self):
        # 絞り込みのために上書き
        queryset = super().get_queryset()

        # GETパラメータを、フォームに紐づける
        form = CustomGoodsSearchForm(self.request.GET)
        form.is_valid()  # フォームからデータを取り出すのに必要な行

        # 値 = フォームオブジェクト.cleaned_data.get('フィールド名')
        name = form.cleaned_data.get('name')
        management_code = form.cleaned_data.get('management_code')
        price_begin = form.cleaned_data.get('price_begin')
        price_end = form.cleaned_data.get('price_end')
        group = form.cleaned_data.get('group')

        if name:
            # .filter(フィールド名=値)
            queryset = queryset.filter(name=name)
        if management_code:
            queryset = queryset.filter(management_code=management_code)
        if group:
            queryset = queryset.filter(group=group)
        if price_begin:
            # filter(フィールド名__特殊条件=値)
            # gte greater than equal >=のこと
            queryset = queryset.filter(price__gte=price_begin)
        if price_end:
            queryset = queryset.filter(price__lte=price_end)
        return queryset
