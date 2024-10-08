from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from user_account.models import UserAccount
BORROW_STATUS = [
    ('Borrowed', 'Borrowed'),
    ('Returned', 'Returned'),
]

# Create your models here.
class Borrow(models.Model):
    borrower = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='borrowers')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    borrow_status = models.CharField(choices = BORROW_STATUS, max_length = 10, default = "Borrowed")
    balance_after_borrow=models.IntegerField(null=True, blank=True)
    balance_after_return=models.IntegerField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.book.title} Borrowed By {self.borrower.user.username}"