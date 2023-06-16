from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm, StaffInformationUpdateForm

class StaffListView(ListView):
    model = Staff
    tempfile_name = 'myapp2/staff_list.html'

# CreateViewの、関数バージョン
# def staff_information(request):
#     if request.method == 'POST':
#         form = StaffInformationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:home')
#         else:
#             context = {
#                 'form': form,
#             }
#             return render(request, 'myapp/staff_information_create.html', context)
#     else:
#         form = StaffInformationForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'myapp/staff_information_create.html', context)
class StaffInformationCreateView(CreateView):
    model = StaffInformation
    form_class = StaffInformationForm
    template_name = 'myapp2/staff_information_create.html'
    success_url = reverse_lazy('myapp:home')


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'myapp2/department_create.html'
    success_url = reverse_lazy('myapp:home')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp2/book_create.html'
    success_url = reverse_lazy('myapp:home')


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'myapp2/staff_create.html'
    # 処理が成功した場合の、リダイレクト先
    # 追加・削除・更新は、処理の後にリダイレクトするのが普通
    success_url = reverse_lazy('myapp:home')

class StaffDetailView(DetailView):
    # primary_key=Trueなフィールドを自分で作っていない場合は、これが暗黙のうちに、全てのモデルに存在する
    #id = models.PositiveIntegerField('id', primary_key=True)
    model = Staff
    template_name = 'myapp2/staff_detail.html'

    # def get_object(self, queryset=None):
    #     #self.kwargsはURL内のint:pkといった部分が入っている
    #     staff = Staff.objects.get(id=1)
    #     # ->Staff.objects.get(pk=1) 今回、URLはstaff_detail/1/
    #     # ->Staff.objects.get(pk=1) pkというのはprimarykeyのこと、今回ならidフィールドの事
    #     print(staff)
    #     return staff


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #DetailViewにはget_objectメソッドがあり
        #URLのidを元にモデルのインスタンスを取得している
        staff = self.get_object()
        context['books'] = staff.rented_books.all()
        return context

class StaffInformationUpdateView(UpdateView):
    model = StaffInformation
    form_class = StaffInformationUpdateForm
    template_name = 'myapp2/staff_information_update.html'
    success_url = reverse_lazy('myapp:home')

    #フォームが作る入力欄のHTMLに一括でclass="input"のように指定したい場合
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-input'

