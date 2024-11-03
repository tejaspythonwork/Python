from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Policy, PolicyHolder
from .forms import PolicyRequestForm
from .utils import send_confirmation_email
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .forms import QuestionForm
from .models import Question


@login_required
def question_dashboard(request):
    return render(request,'myapp/question_dashboard.html')

# @login_required
# def ask_question_view(request):
#     return render(request,'myapp/ask_question.html')

# @login_required
# def questions_list_view(request):
#     return render(request,'myapp/question_list.html')


@login_required
def ask_question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user  
            question.save()
            
            return redirect('questions_list') 
    else:
        form = QuestionForm()
    
    return render(request, 'myapp/ask_question.html', {'form': form})


@login_required
def questions_list_view(request):
    
    questions = Question.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'myapp/question_list.html', {'questions': questions})


def index(request):
    total_users = User.objects.count()
    listed_policies = Policy.objects.count()
    total_policy_holder = PolicyHolder.objects.count()
    approve_policy_holders = PolicyHolder.objects.filter(is_approved=True).count()
    disapproved_policy_holders = PolicyHolder.objects.filter(is_approved=False).count()
    total_number_of_questions = Question.objects.count()
    context = {
        'total_users' : total_users,
        'listed_policies' : listed_policies,
        'total_policy_holder' : total_policy_holder,
        'approved_policy_holder': approve_policy_holders,
        'disapproved_policy_holders' : disapproved_policy_holders,
        'total_question' : total_number_of_questions,
    }
    return render(request,'myapp/index.html',context)

def customer_operations(request):
    return render(request,'myapp/customer_operations.html')


def policy_operations(request):
    policy_data = PolicyHolder.objects.all()
    context = {
        'policy_holders' : policy_data
    }
    return render(request,'myapp/policy_operations.html',context)


def user_list(request):
    users = User.objects.all()  
    return render(request, 'myapp/user_list.html', {'users': users})


def policy_list(request):
    policies = Policy.objects.filter(is_approved=True)  
    return render(request, 'myapp/policy_list.html', {'policies': policies})


@login_required
def request_policy(request):
    if request.method == 'POST':
        form = PolicyRequestForm(request.POST)
        if form.is_valid():
            policy_holder = form.save(commit=False)
            policy_holder.user = request.user 
            policy_holder.save()
            # Send confirmation email
            # send_confirmation_email(policy_holder.user.email)
            messages.success(request, "Your policy request has been submitted successfully!")
            return redirect('ind')
    else:
        form = PolicyRequestForm()


    policies = Policy.objects.filter(is_approved=True)
    return render(request, 'myapp/policy_request.html', {'form': form, 'policies': policies})


@login_required
def user_dashboard(request):
    policy_holders = PolicyHolder.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'policy_holders': policy_holders})


@login_required
def admin_dashboard(request):

    policy_holders = PolicyHolder.objects.all()
    return render(request, 'admin_dashboard.html', {'policy_holders': policy_holders})


@login_required
def approve_policy(request, holder_id):
    policy_holder = get_object_or_404(PolicyHolder, id=holder_id)
    if not policy_holder.is_approved:  
        policy_holder.is_approved = True
        policy_holder.approval_date = timezone.now()  
        policy_holder.save()
        # Send approval confirmation email
        # send_confirmation_email(policy_holder.user.email, approved=True)
        messages.success(request, f"Policy for {policy_holder.user.username} has been approved!")
    else:
        messages.warning(request, "This policy request is already approved.")
    
    return redirect('admin_dashboard')


@login_required
def reject_policy(request, holder_id):
    policy_holder = get_object_or_404(PolicyHolder, id=holder_id)
    if not policy_holder.is_approved:  
        policy_holder.delete()  
        messages.success(request, f"Policy request from {policy_holder.user.username} has been rejected and deleted.")
    else:
        messages.warning(request, "Approved policies cannot be rejected.")
    
    return redirect('ind')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()

        if user:
            # Trigger the password reset process (Django's built-in password reset)
            # send_mail(
            #     'Password Reset Request',
            #     'Please follow the link below to reset your password.',
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False,
            # )
            messages.success(request, "Password reset email has been sent!")
        else:
            messages.error(request, "No account found with that email address.")

    return render(request, 'forgot_password.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            return redirect('user-list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'myapp/register.html', {'form': form})


def add_policy(request):
    if request.method == 'POST':
        policy_number = request.POST.get('policy_number')
        policy_name = request.POST.get('policy_name')
        description = request.POST.get('description')
        premium_amount = request.POST.get('premium_amount')
        is_approved = request.POST.get('is_approved') == 'on'  
        

        Policy.objects.create(
            policy_number=policy_number,
            policy_name=policy_name,
            description=description,
            premium_amount=premium_amount,
            is_approved=is_approved
        )
        
        return redirect('policy_success')  
    
    return render(request, 'myapp/add_policy.html')

def success_policy_creation(request):
    return render(request,'myapp/policy_success.html')


def displaypolicy(request):
    return render(request,'myapp/policies.html')


    