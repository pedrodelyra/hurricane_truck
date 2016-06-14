from django import forms
from microposts.models import Micropost

class MicropostForm(forms.ModelForm):
	content = forms.CharField(max_length=150, required=True)

	class Meta:
		model = Micropost
		fields = ('content', )
