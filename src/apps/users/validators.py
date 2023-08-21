from django.core.validators import RegexValidator

class AccountNumberValidator(RegexValidator):
    regex = r'^[A-Z0-9-]+$'
    message = "Invalid Account Number"
    code = "invalid_account_number"