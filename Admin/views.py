from django.shortcuts import render
import uuid
#import requests
from django.shortcuts import render,redirect,reverse

# Create your views here.


def Activities(request):
    return render(request,'Admin/activities.html')

def Add_Appointment(request):
    return render(request,'Admin/add-appointment.html')

def Add_Asset(request):
    return render(request,'Admin/add-asset.html')

def Add_blog(request):
    return render(request,'Admin/add-blog.html')

def Add_department(request):
    return render(request,'Admin/add-department.html')

def Add_Doctor(request):
    return render(request,'Admin/add-doctor.html')

def Add_Employee(request):
    return render(request,'Admin/add-employee.html')

def Add_expense(request):
    return render(request,'Admin/add-expense.html')

def Add_holiday(request):
    return render(request,'Admin/add-holiday.html')

def Add_leave_type(request):
    return render(request,'Admin/add-leave-type.html')

def Add_leave(request):
    return render(request,'Admin/add-leave.html')

def Add_patient(request):
    return render(request,'Admin/add-patient.html')

def Add_provident_fund(request):
    return render(request,'Admin/add-provident-fund.html')

def Add_role(request):
    return render(request,'Admin/add-role.html')

def Add_salary(request):
    return render(request,'Admin/add-salary.html')

def Add_schedule(request):
    return render(request,'Admin/add-schedule.html')

def Add_tax(request):
    return render(request,'Admin/add-tax.html')

def Appointments(request):
    return render(request,'Admin/appointments.html')

def Asset(request):
    return render(request,'Admin/assets.html')

def Attendence(request):
    return render(request,'Admin/attendence.html')

def blank_page(request):
    return render(request,'Admin/blank-page.html')

def blog_details(request):
    return render(request,'Admin/blog-details.html')

def blog(request):
    return render(request,'Admin/blog.html')

def Calendar(request):
    return render(request,'Admin/Calendar.html')

def Chat(request):
    return render(request,'Admin/chat.html')

def compose(request):
    return render(request,'Admin/compose.html')

def create_invoice(request):
    return render(request,'Admin/create-invoice.html')

def departments(request):
    return render(request,'Admin/departments.html')

def doctor(request):
    return render(request,'Admin/doctors.html')

def Dashboard(request):
    return render(request,'Admin/dashboard.html')

def edit_appoinment(request):
    return render(request,'Admin/edit-appointment.html')

def edit_asset(request):
    return render(request,'Admin/edit-assett.html')

def edit_blog(request):
    return render(request,'Admin/edit-blog.html')

def edit_department(request):
    return render(request,'Admin/edit-department.html')

def edit_doctor(request):
    return render(request,'Admin/edit-doctor.html')

def edit_employee(request):
    return render(request,'Admin/edit-employee.html')

def edit_expense(request):
    return render(request,'Admin/edit-expense.html')

def edit_holiday(request):
    return render(request,'Admin/edit-holiday.html')

def edit_invoice(request):
    return render(request,'Admin/edit-invoice.html')

def edit_leave_type(request):
    return render(request,'Admin/edit-leave-type.html')

def edit_leave(request):
    return render(request,'Admin/edit-leave.html')

def edit_patient(request):
    return render(request,'Admin/edit-patient.html')

def edit_profile(request):
    return render(request,'Admin/edit-profile.html')

def edit_provident_fund(request):
    return render(request,'Admin/edit-provident-fund.html')

def edit_role(request):
    return render(request,'Admin/edit-role.html')

def edit_salary(request):
    return render(request,'Admin/edit-salary.html')

def edit_schedule(request):
    return render(request,'Admin/edit-schedule.html')

def edit_tax(request):
    return render(request,'Admin/edit-tax.html')

def email_settings(request):
    return render(request,'Admin/email-settings.html')

def employees(request):
    return render(request,'Admin/employees.html')

def error_404(request):
    return render(request,'Admin/error-404.html')

def error_500(request):
    return render(request,'Admin/error-500.html')

def expense_report(request):
    return render(request,'Admin/expense-reports.html')

def expenses(request):
    return render(request,'Admin/expenses.html')

def form_basic_inputs(request):
    return render(request,'Admin/form-basic-inputs.html')

def form_horizontal(request):
    return render(request,'Admin/form-horizontal.html')

def form_input_groups(request):
    return render(request,'Admin/form-inputs-groups.html')

def form_vertical(request):
    return render(request,'Admin/form-vertical.html')

def gallery(request):
    return render(request,'Admin/gallery.html')

def holidays(request):
    return render(request,'Admin/holidays.html')

def inbox(request):
    return render(request,'Admin/inbox.html')

def incoming_call(request):
    return render(request,'Admin/incoming-call.html')

def invoice_reports(request):
    return render(request,'Admin/invoice-reports.html')

def invoice_settings(request):
    return render(request,'Admin/invoice-settings.html')

def invoice_view(request):
    return render(request,'Admin/invoice-view.html')

def invoices(request):
    return render(request,'Admin/invoices.html')

def leave_type(request):
    return render(request,'Admin/leave-type.html')

def leaves(request):
    return render(request,'Admin/leaves.html')

def login(request):
    return render(request,'Admin/login.html')

def localisation(request):
    return render(request,'Admin/localisation.html')

def lock_screen(request):
    return render(request,'Admin/lock-screen.html')

def mail_view(request):
    return render(request,'Admin/mail-view.html')

def notification_settings(request):
    return render(request,'Admin/notifications-settings.html')

def patients(request):
    return render(request,'Admin/patients.html')

def profile(request):
    return render(request,'Admin/profile.html')


def provident_fund(request):
    return render(request,'Admin/provident-fund.html')

def payments(request):
    return render(request,'Admin/payments.html')

def register(request):
    return render(request,'Admin/register.html')

def roles_permissions(request):
    return render(request,'Admin/roles-permissions.html')

def salary_settings(request):
    return render(request,'Admin/salary-settings.html')

def settings(request):
    return render(request,'Admin/settings.html')

def salary_view(request):
    return render(request,'Admin/salary-view.html')

def salary(request):
    return render(request,'Admin/salary.html')

def schedule(request):
    return render(request,'Admin/schedule.html')

def tables_basics(request):
    return render(request,'Admin/tables-basics.html')

def tables_datatables(request):
    return render(request,'Admin/tables-datatables.html')

def tabs(request):
    return render(request,'Admin/tabs.html')

def taxes(request):
    return render(request,'Admin/taxes.html')

def theme_settings(request):
    return render(request,'Admin/theme-settings.html')

def typography(request):
    return render(request,'Admin/typography.html')

def uikit(request):
    return render(request,'Admin/uikit.html')