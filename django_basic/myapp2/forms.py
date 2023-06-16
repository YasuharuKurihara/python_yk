from django import forms
from .models import StaffInformation, Department, Book, Staff


class StaffInformationForm(forms.ModelForm):
    class Meta:
        model = StaffInformation
        #fields = '__all__' <-でモジュールの全ての要素を表示する
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'management_code')


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'information', 'department', 'rented_books')


class StaffInformationUpdateForm(forms.ModelForm):

    class Meta:
        model = StaffInformation
        fields = ('staff_name', 'email', 'address', 'birthday', 'hire_date', 'at_desk')