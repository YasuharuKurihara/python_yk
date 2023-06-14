from django.views.generic import CreateView, DetailView, UpdateView, FormView, ListView
from django.urls import reverse_lazy
from .models import StaffInformation, Department, Book, Staff
from .forms import StaffInformationForm, DepartmentForm, BookForm, StaffForm

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
