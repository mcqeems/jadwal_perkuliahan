from django import forms
from .models import jadwal


class jadwalForm(forms.ModelForm):
	class Meta:
		model = jadwal
		fields = ['matkul', 'dosen', 'ruang', 'jam', 'hari', 'semester']
  
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		readonly_fields = ['matkul', 'dosen']
		for field_name in readonly_fields:
			if field_name in self.fields:
				self.fields[field_name].widget.attrs['readonly'] = True