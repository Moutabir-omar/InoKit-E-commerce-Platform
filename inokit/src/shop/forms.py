from django import forms
from .models import Complaint, Order

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'description']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CheckoutForm(forms.ModelForm):
    card_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1234 5678 9012 3456',
            'maxlength': '16',
            'pattern': '[0-9]{16}',
            'title': 'Enter a valid 16-digit card number'
        })
    )
    
    card_expiry = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/YY',
            'maxlength': '5',
            'pattern': '(0[1-9]|1[0-2])\/([0-9]{2})',
            'title': 'Enter expiry date in MM/YY format'
        })
    )
    
    card_cvv = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVV',
            'maxlength': '3',
            'pattern': '[0-9]{3}',
            'title': 'Enter a valid 3-digit CVV'
        })
    )

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'phone', 'card_number', 'card_expiry', 'card_cvv']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Shipping Address',
                'rows': 3
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            })
        }
    
    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not card_number.isdigit() or len(card_number) != 16:
            raise forms.ValidationError('Please enter a valid 16-digit card number')
        return card_number
    
    def clean_card_expiry(self):
        card_expiry = self.cleaned_data.get('card_expiry')
        if not card_expiry or len(card_expiry) != 5 or card_expiry[2] != '/':
            raise forms.ValidationError('Please enter expiry date in MM/YY format')
        return card_expiry
    
    def clean_card_cvv(self):
        card_cvv = self.cleaned_data.get('card_cvv')
        if not card_cvv.isdigit() or len(card_cvv) != 3:
            raise forms.ValidationError('Please enter a valid 3-digit CVV')
        return card_cvv 