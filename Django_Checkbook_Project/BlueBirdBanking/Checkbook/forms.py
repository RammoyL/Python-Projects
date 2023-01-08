from django.forms import ModelForm
from .models import Account, Transaction


# Creates Account Form based on model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
