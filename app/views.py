from django.shortcuts import render, HttpResponseRedirect, reverse
from .utils import *
from random import randint
from .models import *
import sys
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def forgotPage(request):
    return render(request, "app/forget_pass.html")

def service1(request):
    return render(request, 'app/service-1.html')


def service2(request):
    return render(request, 'app/service-2.html')


def service3(request):
    return render(request, 'app/service-3.html')


def service4(request):
    return render(request, 'app/service-4.html')


def service5(request):
    return render(request, 'app/service-5.html')


def Profile(request):
    return render(request, 'app/user_profile.html')


def order(request):
    return render(request, 'app/view_order.html')


def provider_order(request):
    return render(request, 'app/provider_view.html')


def aboutus(request):
    return render(request, 'app/aboutus.html')


def con(request):
    return render(request, 'app/contact-us.html')


def our_service(request):
    all_service = Service_detail.objects.all()
    if all_service:
        return render(request, 'app/our_service.html', {'all_service': all_service})
    else:
        return HttpResponseRedirect(reverse('login'))


def registerPage(request):
    services = Service_detail.objects.filter().order_by('id')
    sub_services = Sub_service.objects.filter().order_by('id')
    return render(request, "app/register.html", {'services': services, 'sub_services': sub_services})


def registration(request):
    try:
        if request.POST['role'] == 'user':
            role = request.POST['role']
            name = request.POST['name']
            password = request.POST['password']
            cpassword = request.POST['confirmpassword']
            email = request.POST['email']
            address = request.POST['address']
            contact = request.POST['contno']
            gender = request.POST['gender']
            city_id = request.POST['city']
            state_id = request.POST['state']
            country_id = request.POST['country']

            c_user = User.objects.filter(email=email)
            if c_user:
                message = "This user is alery exist"
                return render(request, "app/register.html", {'message': message})
            else:
                if password == cpassword:
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newcust = Customer.objects.create(user_id=newuser, name=name,
                                                             address=address, contact=contact,
                                                             gender=gender, city_id=city_id,
                                                             state_id=state_id,
                                                             country_id=country_id)
                    email_subject = "Service Hub : Account Vericication"
                    sendmail(email_subject, 'mail_template', email, {
                        'name': name, 'otp': otp, 'link': 'http://localhost:8000/enterprise/user_verify/'})
                    return render(request, 'app/login.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/register.html', {'message': message})
        else:
            if request.POST['role'] == 'serviceprovider':
                role = request.POST['role']
                name = request.POST['name1']
                password = request.POST['password1']
                cpassword = request.POST['confirmpassword1']
                email = request.POST['email1']
                address = request.POST['address1']
                contact = request.POST['contno1']
                gender = request.POST['gender1']
                city_id = request.POST['city1']
                state_id = request.POST['state1']
                country_id = request.POST['country1']
                service = request.POST['service']
                prof_img = request.FILES['image']
                fs = FileSystemStorage()
                # fs.save(prof_img.name,prof_img)
                user = User.objects.filter(email=email)
                if user:
                    message = "This user is alery exist"
                    return render(request, "app/register.html", {'message': message})
                else:
                    if password == cpassword:
                        otp = randint(100000, 9999999)
                        newuser = User.objects.create(
                            email=email, password=password, role=role, otp=otp)
                        newprovider = Service_provider.objects.create(user_id=newuser, name=name,
                                                                      address=address, contact=contact,
                                                                      gender=gender, city_id=city_id,
                                                                      state_id=state_id,
                                                                      country_id=country_id,
                                                                      service=service, profile_img=prof_img)
                        email_subject = "A2Z Service: Account Vericication"
                        sendmail(email_subject, 'mail_template', email, {
                            'name': name, 'otp': otp, 'link': 'http://localhost:8000/enterprise/user_verify/'})
                        return render(request, 'app/login.html', {'newprovider': newprovider})
                    else:
                        message = "Password and confirm password doesn't match"
                        return render(request, 'app/register.html', {'message': message})
    except User.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'app/register.html', {'message': message})


def LoginPage(request):
    return render(request, "app/login.html")


def login_evaluation(request):
    if request.POST['role'] == 'user':
        email = request.POST['email']
        password = request.POST['password']
        user1 = User.objects.filter(email=email)
        print(user1)
        if user1[0]:
            if user1[0].password == password and user1[0].role == 'user':
                customer = Customer.objects.filter(user_id=user1[0])
                request.session['email'] = user1[0].email
                request.session['name'] = customer[0].name
                request.session['role'] = user1[0].role
                request.session['id'] = user1[0].id
                # return render(request,"app/homepage.html")
                # return render(request,"app/user_list.html")
                return HttpResponseRedirect(reverse('view_profile'))
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})

    else:
        if request.POST['role'] == 'serviceprovider':
            email = request.POST['email']
            password = request.POST['password']
            user1 = User.objects.filter(email=email)
            print(user1)
            if user1[0]:
                if user1[0].password == password and user1[0].role == 'serviceprovider':
                    pro = Service_provider.objects.filter(user_id=user1[0])
                    request.session['email'] = user1[0].email
                    request.session['name'] = pro[0].name
                    request.session['role'] = user1[0].role
                    request.session['id'] = user1[0].id
                    return HttpResponseRedirect(reverse('view_profile'))
                else:
                    message = "Your password is incorrect or user doesn't exist"
                    return render(request, "app/login.html", {'message': message})
            else:
                message = "user doesn't exist"
                return render(request, "app/login.html", {'message': message})



def forgotPassword(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)

        if user:
            if user.email == email:
                otp = randint(100000, 9999999)
                user.otp = otp
                user.save()
                email_subject = "This is your new OTP"
                sendmail(email_subject, 'mail_template', email, {'otp': otp})
                return render(request, 'app/passverfication.html', {'email': email})
            else:
                message = 'This email does not match'
                return render(request, "app/forget_pass.html", {'message': message})
        else:
            message = 'This email is not available'
            return render(request, "app/forget_pass.html", {'message': message})
    except:
        message = 'This email is not available'
        return render(request, "app/forget_pass.html", {'message': message})


def ResetPassword(request):
    otp = request.POST['otp']
    newPassword = request.POST['newpass']
    confirmPassword = request.POST['confirmpass']
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
        if confirmPassword == newPassword and str(user.otp) == otp:
            user.password = newPassword
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            message = "Either password and confirm password doesn't match or you have entered a wrong otp"
            return render(request, "app/passverification.html", {'message': message})
    except:
        message = "Ivalid request"
        return render(request, "app/passverification.html", {'message': message})


def Homepage(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'serviceprovider':
            all_user = Customer.objects.all()
            return render(request, 'app/homepage.html', {'all_user': all_user})
    else:
        return HttpResponseRedirect(reverse('login'))


def logout(request):
    del request.session['email']
    del request.session['role']
    del request.session['name']
    return HttpResponseRedirect(reverse('login'))


def Service_list(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'user':
            all_service = Service_detail.objects.all()
            return render(request, 'app/service_list.html', {'all_service': all_service})
    else:
        return HttpResponseRedirect(reverse('login'))


def sub_cat(request, pk):
    print("Pk ------------------------->", pk)
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'user':
            all_subcat = AllInfo.objects.filter(Service_id=pk).select_related('sub_id')
            print("All_Sub_Cat", all_subcat)
            for cat in all_subcat:
                print("SubCategory :", cat.sub_id)
            return render(request, "app/service-2.html", {'all_subcat': all_subcat, 'service_id': pk})
    else:
        return HttpResponseRedirect(reverse('login'))


def feedbacks(request):
    return render(request, "app/feedback.html")


def getfeedback(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']

        review = request.POST['review']
        newfeed = feedback.objects.create(username=username, email=email, review=review)
        if newfeed:

            return render(request, "app/successfullregister.html")
        else:
            return render(request, "app/feedback.html")


def booking1(request):
    # print("USER SESSION --------->",request.session['id'])
    service_id = request.POST['service_id']
    subname = request.POST['subcat']
    orderdate = request.POST['appdate']
    ordertime = request.POST['apptime']
    return render(request, "app/service-3.html",
                  {'subname': subname, 'orderdate': orderdate, 'ordertime': ordertime, 'service_id': service_id})


def finalbooking(request):
    # print('this is request ---->', request.POST['subcat'])
    subname = Sub_service.objects.get(id=request.POST['subcat'])
    user_id = User.objects.get(id=request.session['id'])
    service_id = Service_detail.objects.get(id=request.POST['service_id'])
    Orderdate = request.POST['appdate']
    ordertime = request.POST['apptime']
    username = request.POST['username']
    address = request.POST['address']
    mobile = request.POST['mobile']
    pincode = request.POST['pincode']
    email = request.POST['email']
    print("service_id -----------", service_id.id)
    print("subname -----------", subname.id)
    print("user_id", user_id.id)
    service = request.POST['service_id']
    print("value-----", service)

    #service_provider_assign = Service_provider.objects.get(service=request.POST['service_id'])
    service_provider_assign = Service_provider.objects.get(service=request.POST['service_id'])

    print("ID : -------------", service_provider_assign.id)
    newbooking = Order.objects.create(email=email, Sub_id=subname, user_id=user_id, Service_id=service_id,
                                           Orderdate=Orderdate, ordertime=ordertime, username=username, address=address,
                                           mobile=mobile, pincode=pincode,
                                           service_provider_assign=service_provider_assign)
    last_order = Order.objects.all().last()
    print("ID : ------------", last_order.id)

    email_subject = "Service Hub : Order placed successfully"
    sendmail(email_subject, 'ordermail', email,
             {'orderid': last_order.id, 'username': username, 'address': address, 'mobile': mobile,
              'Orderdate': Orderdate, 'ordertime': ordertime, 'pincode': pincode})
    print("orderid")
    return render(request, "app/service-4.html", {'newbooking': newbooking})


def view_profile(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'user':

            all_user = User.objects.get(id=request.session['id'])
            print(all_user.id)
            all_cust = Customer.objects.get(user_id=request.session['id'])
            print(all_cust.user_id)

            return render(request, 'app/user_profile.html', {'all_user': all_user, 'all_cust': all_cust})
        else:

            if request.session['role'] == 'serviceprovider':
                all_user = User.objects.get(id=request.session['id'])
                print(all_user.id)
                all_provider = Service_provider.objects.get(user_id=request.session['id'])
                s_id = all_provider.service
                print("s_id-------------", s_id)
                s_detail = Service_detail.objects.get(id=s_id)
                print(all_provider.user_id)
                return render(request, 'app/provider_profile.html',
                              {'all_user': all_user, 'all_provider': all_provider, 's_detail': s_detail})


def show_order(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'user':

            all_order = Order.objects.filter(user_id=request.session['id'])

            return render(request, 'app/view_order.html', {'all_order': all_order})
        else:

            if request.session['role'] == 'serviceprovider':
                s_id = Service_provider.objects.get(user_id=request.session['id'])
                print("s_id--->", s_id.user_id)
                all_provider = Order.objects.filter(service_provider_assign=s_id)
                # print("All_provider----->",all_provider)

                return render(request, 'app/provider_view.html', {'all_provider': all_provider})


def delete(request, oid):
    order = Order.objects.filter(id=oid)
    order.delete()

    return HttpResponseRedirect(reverse('show_order'))


def update_status(request, oid):
    order = Order.objects.filter(id=oid).update(status="confirm")

    return HttpResponseRedirect(reverse('show_order'))



