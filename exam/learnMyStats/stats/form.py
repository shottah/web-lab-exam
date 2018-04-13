from django import forms
from .courses import Course

class CourseForm (forms.ModelForm):
    # Define Input Labels
    code = forms.CharField(label="Code", max_length=10)
    name = forms.CharField(label="Name", max_length=200)
    credits = forms.IntegerField()
    

    class Meta:
        # Define Model being written to
        model = Course
        # Define fields being set
        fields = (
            'code',
            'name',
            'credits'
        )

    def save (self, commit=True):
        # Override save() method
        c = Course()
        c.code = self.cleaned_data['code']
        c.name = self.cleaned_data['name']
        c.credits = self.cleaned_data['credits']

        if commit:
            c.save()
        
        # Return new Object
        return c