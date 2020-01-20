from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
# from .models imoort *

class contact_us (forms.Form):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(), required=True, max_length=100)
    city = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    contact_no = forms.CharField(label='Contact Number', widget=forms.NumberInput(), required=True)
    description = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'city',
            'contact number',
            'description',
            Submit ('submit', 'Submit', css_class='btn-success')
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model=Snippet
        fields=('name','body')