from django import forms

class LoanForm(forms.Form):
    tipos = [('PERSONAL', 'Personal'),('PRENDARIO', 'Prendario'), ('HIPOTECARIO', 'Hipotecario')]
    tipo = forms.ChoiceField(label='Tipo de préstamo', initial=tipos[0], choices=tipos, required=True, widget=forms.Select(attrs={'class' : 'form-control'}))
    monto = forms.IntegerField(label='Monto', required=True, widget=forms.NumberInput(attrs={'placeholder' : 'Ingrese el monto deseado', 'class' : 'form-control'}))