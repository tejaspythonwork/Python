from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone






class Policy(models.Model):
    policy_number = models.CharField(max_length=20, unique=True)
    policy_name = models.CharField(max_length=100)
    description = models.TextField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.policy_name

    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = "Policies"



class PolicyHolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approval_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.policy.policy_name}"

    class Meta:
        verbose_name = "Policy Holder"
        verbose_name_plural = "Policy Holders"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



class PolicyTransaction(models.Model):
    policy_holder = models.ForeignKey(PolicyHolder, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)  
    transaction_date = models.DateTimeField(default=timezone.now)
    details = models.TextField()

    def __str__(self):
        return f"{self.transaction_type} - {self.policy_holder.user.username}"

    class Meta:
        verbose_name = "Policy Transaction"
        verbose_name_plural = "Policy Transactions"


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f"Question by {self.user.username} on {self.created_at}"

