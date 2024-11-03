from django.urls import path
from . import views


urlpatterns = [
    path('policies/', views.policy_list, name='policy_list'),
    path('request-policy/', views.request_policy, name='request_policy'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('approve-policy/<int:holder_id>/', views.approve_policy, name='approve_policy'),
    path('reject-policy/<int:holder_id>/', views.reject_policy, name='reject_policy'),
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user-list'),
    path('',views.index,name='ind'),
    path('policy_operations/',views.policy_operations,name='policyoperations'),
    path('customer_operations/',views.customer_operations,name='customersoperations'),
    path('create_policy/',views.add_policy,name='createpolicy'),
    path('success_policy_creation/',views.success_policy_creation,name='policy_success'),
    path('disppolicies/',views.displaypolicy,name='disppolicy'),
    path('ask-question/', views.ask_question_view, name='ask_question'),
    path('my-questions/', views.questions_list_view, name='questions_list'),
    path('question_dashboard/',views.question_dashboard,name='qdashboard')
    # path('/', views.count_total_registered_user, name='indusercnt'),
]