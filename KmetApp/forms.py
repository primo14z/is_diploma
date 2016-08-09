class OglasForm(forms.ModelForm):
	"""docstring for OglasForm"""
	def __init__(self, arg):
		super(OglasForm, self).__init__()
		self.arg = arg
		