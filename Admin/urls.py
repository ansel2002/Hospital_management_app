from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns = [
    path('Activities', views.Activities,name='Activities'),
    path('Add-Appointment', views.Add_Appointment,name='Add-Appointment'),
    path('Add-Asset', views.Add_Asset,name='Ad-Add-Asset'),
    path('Add-blog', views.Add_blog,name='Add-blog'),
    path('Add-department', views.Add_department,name='Add-department'),
    path('Add-Doctor', views.Add_Doctor,name='Add-Doctor'),
    path('Add-Employee', views.Add_Employee,name='Add-Employee'),
    path('Add-expense', views.Add_expense,name='Add-expense'),
    path('Add-holiday', views.Add_holiday,name='Add-holiday'),
    path('Add-leave-type', views.Add_leave_type,name='Add-leave-type'),
    path('Add-leave', views.Add_leave,name='Add-leave'),
    path('Add-appointnment', views.Add_Appointment,name='Add-Appointment'),

    path('Add-patient', views.Add_patient,name='Add-patient'),
    path('Add-provident-fund', views. Add_provident_fund,name=' Add-provident-fund'),
    path('Add-role', views.Add_role,name='Add-role'),
    path('Add-salary', views. Add_salary,name=' Add-salary'),
    path('Add-schedule', views.Add_schedule,name='Add-schedule'),
    path('Add-tax', views.Add_tax,name='Add-tax'),
    path('Appointments', views.Appointments,name='Appointments'),
    path('Asset', views.Asset,name='Asset'),
    path('Attendence', views.Attendence,name='Attendence'),
    path('blank-page', views.blank_page,name='blank-page'),
    path('blog-details', views.blog_details,name='blog-details'),
    path('blog', views.blog,name='blog'),
    path('Calendar', views.Calendar,name='Calendar'),
    path('Chat', views.Chat,name='Chat'),
    path('compose', views.compose,name='compose'),
    path('create-invoice', views.create_invoice,name='create-invoice'),
    path('departments', views.departments,name='departments'),
    path('doctor', views.doctor,name='Doctors'),
    path('Dashboard', views.Dashboard,name='Dashboard'),
    path('edit-appoinment', views.edit_appoinment,name='edit-appoinment'),
    path('edit_asset', views.edit_asset,name='edit_asset'),
    path('edit-blog', views.edit_blog,name='edit-blog'),
    path('edit-department', views.edit_department,name='edit-department'),
    path('edit-doctor', views.edit_doctor,name='edit-doctor'),
    path('edit-employee', views.edit_employee,name='edit-employee'),
    path('edit-expense', views.edit_expense,name='edit-expense'),
    path('edit-holiday', views.edit_holiday,name='edit-holiday'),
    path('edit-invoice', views.edit_invoice,name='edit-invoice'),
    path('edit-leave-type', views.edit_leave_type,name='edit-leave-type'),
    path('edit_leave', views.edit_invoice,name='edit-invoice'),
    path('edit-invoice', views.edit_leave,name='edit-leave'),
    path('edit-patient', views.edit_patient,name='edit-patient'),
    path('edit-profile', views.edit_profile,name='edit-profile'),
    path('edit-provident-fund', views.edit_provident_fund,name='edit-provident-fund'),
    path('edit-role', views.edit_role,name='edit-role'),
    path('edit-salary', views.edit_salary,name='edit-salary'),
    path('edit-schedule', views.edit_schedule,name='edit-schedule'),
    path('edit-tax', views.edit_tax,name='edit-tax'),
    path('email-settings', views.email_settings,name='email-settings'),
    path('employees', views.employees,name='employees'),
    path('error-404', views.error_404,name='error-404'),
    path('error-500', views.error_500,name='error-500'),
    path('expense-report', views.expense_report,name='expense-report'),
    path('expenses', views.expenses,name='expenses'),
    path('form-basic-inputs', views.form_basic_inputs,name='form-basic-inputs'),
    path('form-horizontal', views.form_horizontal,name='form-horizontal'),
    path('form-input-groups', views.form_input_groups,name='form-input-groups'),
    path('form-vertical', views.form_vertical,name='form-vertical'),
    path('gallery', views.gallery,name='gallery'),
    path('holidays', views.holidays,name='holidays'),
    path('inbox', views.inbox,name='inbox'),
    path('incoming-call', views.incoming_call,name='incoming-call'),
    path('invoice-reports', views.invoice_reports,name='invoice-reports'),
    path('invoice-settings', views.invoice_settings,name='invoice-settings'),
    path('invoice-view', views.invoice_view,name='invoice-view'),
    path('invoices', views.invoices,name='invoices'),
    path('leave-type', views.leave_type,name='leave-type'),
    path('leaves', views.leaves,name='leaves'),
    path('localisation', views.localisation,name='localisation'),
    path('lock-screen', views.lock_screen,name='lock-screen'),
    path('mail-view', views.mail_view,name='mail-view'),
    path('notification-settings', views.notification_settings,name='notification-settings'),
    path('patients', views.patients,name='patients'),
    path('profile', views.profile,name='profile'),
    path('provident-fund', views.provident_fund,name='provident-fund'),
    path('payments', views.payments,name='payments'),
    path('register', views.register,name='register'),
    path('roles-permissions', views.roles_permissions,name='roles-permissions'),
    path('salary-settings', views.salary_settings,name='salary-settings'),
    path('settings', views.settings,name='settings'),
    path('salary-view', views.salary_view,name='salary-view'),
    path('salary', views.salary,name='salary'),
    path('schedule', views.schedule,name='schedule'),
    path('tables-basics', views.tables_basics,name='tables-basics'),
    path('tables-datatables', views.tables_datatables,name='tables-datatables'),
    path('tabs', views. tabs,name='tabs'),
    path('taxes', views.taxes,name='taxes'),
    path('theme-settings', views.theme_settings,name='theme-settings'),
    path('typography', views.typography,name='typography'),
    path('uikit', views.uikit,name='uikit'),



]