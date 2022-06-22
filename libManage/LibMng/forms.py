from django import forms

from .models import Student,Instructor

class Student_login(forms.ModelForm):
    # stu_id=forms.CharField(required=True)
    class Meta:
        model = Student
        fields = ['stu_id','password',]

        widgets = {
            'stu_id': forms.TextInput(attrs={'class':'form-control'}),
            # 'name': forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            # 'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def save(self,commit=True):
        stud = super(Student_login,self).save(commit=False)
        if commit:
            stud.save()
        return stud



class Employee_login(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['emp_id','password',]

        widgets = {
            'emp_id': forms.TextInput(attrs={'class':'form-control'}),
            # 'name': forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            # 'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def save(self,commit=True):
        empl = super(Employee_login,self).save(commit=False)
        if commit:
            empl.save()
        return empl