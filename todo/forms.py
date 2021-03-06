from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
            widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Add your new todo', 'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn'}))
