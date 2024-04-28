import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.
from myapp.models import *
import random


def login(request):
    return render(request, 'index1.html')

def login_post(request):
    un=request.POST['textfield']
    ps=request.POST['textfield2']
    log=Login.objects.filter(username=un,password=ps)
    if log.exists():
        logid=log[0].id
        request.session['lid']=logid
        if log[0].usertype == 'admin':
            return HttpResponse("<script>alert('login sucsess');window.location='/admin_home'</script>")
        elif log[0].usertype == 'staff':
            return HttpResponse("<script>alert('login sucsess');window.location='/staff_home'</script>")
        elif log[0].usertype == 'employee':
            return HttpResponse("<script>alert('login sucsess');window.location='/deliverey_home'</script>")
        else:
            return HttpResponse("<script>alert('invalid user');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('invalid user');window.location='/'</script>")
def admin_home(request):
    return render(request,'admin/adminindex1.html')
def logout(request):
    request.session['lid']=''
    return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")

def forgot_password(request):
    return render(request,'forgotpassword.html')

def forgot_password_post(request):
    emil=request.POST['textfield']
    log=Login.objects.filter(username=emil)
    if log.exists():
        paswrd=log[0].password
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("smartfuddonation@gmail.com", "smart@789")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "smartfuddonation@gmail.com"
        msg['To'] = id
        msg['Subject'] = "Your Password is"
        body = "Your Password is:- - " + str(paswrd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password has been send please check your emnail');window.location='/'</script>")

def add_category(request):
    if   request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        return render(request,'admin/category.html')

def add_category_post(request):
    cat=request.POST['textfield']
    obj=Category()
    obj.name=cat
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/admin_home'</script>")

def view_category(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Category.objects.all()
        return render(request,'admin/view_category.html',{'data':data})

def edit_category(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Category.objects.get(id=id)
        return render(request,'admin/edit_category.html',{'data':data})

def edit_category_post(request,id):
    nam=request.POST['textfield']
    Category.objects.filter(id=id).update(name=nam)
    return HttpResponse("<script>alert('edited');window.location='/view_category'</script>")
def delete_category(request,id):
    Category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete');window.location='/view_category'</script>")

def add_subcategory(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Category.objects.all()
        return render(request,'admin/sub_category.html',{'data':data})

def add_subcategory_post(request):
    cat=request.POST['select']
    name=request.POST['textfield']
    obj=Sub_category()
    obj.CATEGORY_id=cat
    obj.name=name
    obj.save()
    return HttpResponse("<script>alert('delete');window.location='/view_category'</script>")
def view_subcategory(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Sub_category.objects.all()
        return render(request,'admin/view_subcategory.html',{'data':data})

def edit_subcategory(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Category.objects.all()
        obj=Sub_category.objects.get(id=id)
        return render(request,'admin/edit_sub_category.html',{'data':data,'obj':obj})

def edit_subcategory_post(request,id):
    cat = request.POST['select']
    name = request.POST['textfield']
    Sub_category.objects.filter(id=id).update(CATEGORY=cat,name=name)
    return HttpResponse("<script>alert('delete');window.location='/view_subcategory'</script>")
def delete_subcategory(request,id):
    Sub_category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete');window.location='/view_subcategory'</script>")
def add_product(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Sub_category.objects.all()
        return render(request, 'admin/Add Product.html',{'data':data})

def add_product_post(request):
    print(request.FILES)
    print(request.POST)
    ap = request.POST['textfield']
    asc = request.POST['select2']
    aimg = request.FILES['fileField']
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs=FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\"+date+'.jpg',aimg)
    path="/media/photos/"+date+'.jpg'
    aprice = request.POST['textfield2']
    pr=Product()
    pr.P_name=ap
    pr.P_sub_category=asc
    pr.P_image=path
    pr.Price=aprice
    pr.save()
    return HttpResponse("<script>alert('product added');window.location='/admin_home'</script>")
def view_product(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        viewP=Product.objects.all()
        return render(request,'admin/View Product.html',{"datap":viewP})

def edit_product(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Product.objects.get(id=id)
        data1 = Sub_category.objects.all()
        return render(request,'admin/Edit Product.html',{'data':data,'data1':data1})

def edit_product_post(request,id):
    try:
        ap = request.POST['textfield']
        asc = request.POST['select2']
        aimg = request.POST['fileField']
        date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\" + date + '.jpg', aimg)
        path = "/media/photos/" + date + '.jpg'
        aprice = request.POST['textfield2']
        Product.objects.filter(id=id).update(P_name=ap,SUB_CATEGORY=asc,P_image=path,Price=aprice)

        return HttpResponse("<script>alert('Edited');window.location='/view_product'</script>")
    except Exception as e:
        ap = request.POST['textfield']
        asc = request.POST['select2']
        aprice = request.POST['textfield2']
        Product.objects.filter(id=id).update(P_name=ap, SUB_CATEGORY=asc,Price=aprice)

        return HttpResponse("<script>alert('Edited');window.location='/view_product'</script>")


def delete_product_post(request,id):
    Product.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_product'</script>")

def add_stock(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:

        return render(request,'admin/Add Stock.html',{'id':id})

def add_stock_post(request,id):
    q=request.POST['textfield3']
    obj=Stock()
    obj.PRODUCT_id=id
    obj.S_quantity=q
    obj.save()
    return HttpResponse("<script>alert('add stock');window.location='/admin_home'</script>")


def view_stock(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        viewS = Stock.objects.filter(PRODUCT_id=id)
        return render(request,'admin/View Stock.html',{"datas":viewS})

def edit_stock(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:

        data=Stock.objects.get(id=id)
        return render(request,'admin/Edit Stock.html',{'data':data})

def edit_stock_post(request,id):
    tq = request.POST['textfield3']
    Stock.objects.filter(id=id).update(S_quantity=tq)
    return HttpResponse("<script>alert('update stock');window.location='/view_product'</script>")
def delete_stock(request,id):
    Stock.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete stock');window.location='/view_product'</script>")

def add_staff(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        return render(request,'admin/Add Staff.html')

def add_staff_post(request):
    nm=request.POST['textfield']
    img=request.FILES['fileField']
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\" + date + '.jpg',img)
    path = "/media/photos/" + date + '.jpg'
    phn=request.POST['textfield3']
    addrss=request.POST['textarea']
    mail=request.POST['textfield4']
    gen=request.POST['RadioGroup1']
    rd=random.randint(0000,9999)
    log=Login.objects.filter(username=mail)
    if log.exists():
        return HttpResponse("<script>alert('this user already exists');window.location='/admin_home'</script>")
    else:
        lo=Login()
        lo.username=mail
        lo.password=rd
        lo.usertype='staff'
        lo.save()

        data=Staff()
        data.E_name=nm
        data.E_address=addrss
        data.E_image=path
        data.E_phn=phn
        data.E_email=mail
        data.gender=gen
        data.LOGIN=lo
        # try:
        #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
        #
        #     gmail.ehlo()
        #
        #     gmail.starttls()
        #
        #     gmail.login('vvrr2731@gmail.com', 'ajay1490')
        #
        # except Exception as e:
        #     print("Couldn't setup email!!" + str(e))
        #
        # msg = MIMEText("Your OTP is " + otpvalue)
        #
        # msg['Subject'] = 'Verification'
        #
        # msg['To'] = email
        #
        # msg['From'] = 'vvrr2731@gmail.com'
        #
        # try:
        #
        #     gmail.send_message(msg)
        #
        # except Exception as e:
        #
        #     print("COULDN'T SEND EMAIL", str(e))
        data.save()
        return HttpResponse("<script>alert('update stock');window.location='/admin_home'</script>")

def view_staff(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        viewSF=Staff.objects.all()
        return render(request,'admin/View Staff.html',{"datasf":viewSF})

def edit_staff(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Staff.objects.get(id=id)
        return render(request,'admin/Edit Staff.html',{'data':data})
def edit_staff_post(request,id):
    try:
        nm = request.POST['textfield']
        img = request.FILES['fileField']
        date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\" + date + '.jpg', img)
        path = "/media/photos/" + date + '.jpg'
        phn = request.POST['textfield3']
        addrss = request.POST['textarea']
        mail = request.POST['textfield4']
        gen=request.POST['RadioGroup1']
        Staff.objects.filter(id=id).update(E_name=nm,E_image=path,E_address=addrss,E_phn=phn,E_email=mail,gender=gen)
        return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")
    except Exception as e:
        nm = request.POST['textfield']
        phn = request.POST['textfield3']
        addrss = request.POST['textarea']
        mail = request.POST['textfield4']
        gen = request.POST['RadioGroup1']
        Staff.objects.filter(id=id).update(E_name=nm,E_address=addrss, E_phn=phn, E_email=mail,gender=gen)
        return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")

def delete_staff_post(request,id):
    Staff.objects.get(id=id).delete()
    return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")

def view_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        viewcm=Complaint.objects.all()
        return render(request,'admin/View Complaint.html',{"datacmp":viewcm})

def sent_reply(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        return render(request,'admin/Sent Reply.html',{'id':id})

def sent_reply_post(request,id):
    reply=request.POST['textarea']
    Complaint.objects.filter(id=id).update(Cmplt_reply=reply,Reply_date=datetime.datetime.now().strftime('%Y-%m-%d'))
    return HttpResponse("<script>alert('reply has been send');window.location='/view_complaint'</script>")

def view_rating(request):
    viewrat=Rating.objects.all()
    arr = []
    for i in viewrat:
        a = float(i.Rating)

        fs = "/media/star/full.jpg"
        hs = "/media/star/half.jpg"
        es = "/media/star/empty.jpg"
        arr = []

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]


        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]

        else:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]

        arr.append({"rating": ar,
                    "user":i.CUSTOMER.C_name,
                    "date":i.R_date,
                    "product":i.PRODUCT.P_name,
                    "pimage":i.PRODUCT.P_image,
                    })

    return render(request, 'admin/view_raiting.html', {"data":arr})


# def view_report(request):
#     #SHOULD CREATE A TABLE NAMED "report"
#     return render(request,'admin/View Report.html')

def view_order(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Cart.objects.all()
        return render(request,'admin/view_order.html',{'data':data})

def view_order_by_date(request):
    srch=request.POST['textfield']
    data=Cart.objects.filter(ORDER__O_date__lte=srch)
    return render(request,'admin/view_order.html',{'data':data})
def add_employe(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        return render(request,'admin/Add mployee.html')

def add_employe_post(request):
    nm=request.POST['textfield']
    img=request.FILES['fileField']
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\" + date + '.jpg',img)
    path = "/media/photos/" + date + '.jpg'
    phn=request.POST['textfield3']
    addrss=request.POST['textarea']
    mail=request.POST['textfield4']
    gen=request.POST['RadioGroup1']
    rd=random.randint(0000,9999)
    log=Login.objects.filter(username=mail)
    if log.exists():
        return HttpResponse("<script>alert('this user already exists');window.location='/admin_home'</script>")
    else:
        lo=Login()
        lo.username=mail
        lo.password=rd
        lo.usertype='employee'
        lo.save()

        data=Employee()
        data.E_name=nm
        data.E_address=addrss
        data.E_image=path
        data.E_phn=phn
        data.E_email=mail
        data.gender=gen
        data.LOGIN_id=lo
        # try:
        #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
        #
        #     gmail.ehlo()
        #
        #     gmail.starttls()
        #
        #     gmail.login('vvrr2731@gmail.com', 'ajay1490')
        #
        # except Exception as e:
        #     print("Couldn't setup email!!" + str(e))
        #
        # msg = MIMEText("Your OTP is " + otpvalue)
        #
        # msg['Subject'] = 'Verification'
        #
        # msg['To'] = email
        #
        # msg['From'] = 'vvrr2731@gmail.com'
        #
        # try:
        #
        #     gmail.send_message(msg)
        #
        # except Exception as e:
        #
        #     print("COULDN'T SEND EMAIL", str(e))
        data.save()
        return HttpResponse("<script>alert('update stock');window.location='/admin_home'</script>")

def view_employe(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        viewSF=Employee.objects.all()
        return render(request,'admin/View Employee.html',{"datasf":viewSF})

def edit_employe(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Employee.objects.get(id=id)
        return render(request,'admin/Edit Employee.html',{'data':data})
def edit_employe_post(request,id):
    try:
        nm = request.POST['textfield']
        img = request.FILES['fileField']
        date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Mottuz\Downloads\HarithaTraders\HarithaTraders\media\photos\\" + date + '.jpg', img)
        path = "/media/photos/" + date + '.jpg'
        phn = request.POST['textfield3']
        addrss = request.POST['textarea']
        mail = request.POST['textfield4']
        gen=request.POST['RadioGroup1']
        Employee.objects.filter(id=id).update(E_name=nm,E_image=path,E_address=addrss,E_phn=phn,E_email=mail,gender=gen)
        return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")
    except Exception as e:
        nm = request.POST['textfield']
        phn = request.POST['textfield3']
        addrss = request.POST['textarea']
        mail = request.POST['textfield4']
        gen = request.POST['RadioGroup1']
        Employee.objects.filter(id=id).update(E_name=nm,E_address=addrss, E_phn=phn, E_email=mail,gender=gen)
        return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")

def delete_employe_post(request,id):
    Employee.objects.get(id=id).delete()
    return HttpResponse("<script>alert('update Employee');window.location='/view_staff'</script>")


# ==============================Android================================================================================


def andro_log(request):
    username=request.POST['u']
    password = request.POST['p']
    alog=Login.objects.filter(username=username,password=password)
    if alog.exists():

        lid=alog[0].id
        type=alog[0].usertype

        return JsonResponse({'status':"ok",'type':type,'lid':lid})
    else:
        return JsonResponse({'status': "none"})

def andro_register(request):
    name=request.POST['name']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    email=request.POST['email']
    phone=request.POST['phone']
    pasrd=request.POST['password']
    print(pin,"pinn")
    log=Login.objects.filter(username=email)
    if log.exists():
        return JsonResponse({"status":"no"})
    else:
        log=Login()
        log.username=email
        log.password=pasrd
        log.usertype='customer'
        log.save()

        reg=Customer()
        reg.C_name=name
        reg.C_place=place
        reg.C_post=post
        reg.c_pin=pin
        reg.C_email=email
        reg.C_phn=phone
        reg.LOGIN=log
        reg.save()
        return JsonResponse({"status": "ok"})


def andro_view_category(request):
    data=Category.objects.all()
    ary=[]
    for i in data:
        ary.append({
            "id":i.id,
            "cat":i.name
        })
    return JsonResponse({"status":"ok","data":ary})

def andro_view_subcategory(request):
    cid=request.POST['catid']
    data=Sub_category.objects.filter(CATEGORY=cid)
    ary=[]
    for i in data:
        ary.append({
            "id":i.id,
            "cat":i.name
        })
    return JsonResponse({"status": "ok", "data": ary})


def andro_view_product(request):
    subcatid=request.POST['subcatid']
    data=Product.objects.filter(SUB_CATEGORY=subcatid)
    ary=[]
    for i in data:
        stock = Stock.objects.get(PRODUCT=i)
        ary.append({
            "id":i.id,
            "pnam":i.P_name,
            "amount":i.Price,
            "image":i.P_image,
            "stock": stock.S_quantity
        })

    return JsonResponse({"status": "ok", "data": ary})

def andro_place_order(request):
    number=request.POST['number']
    lid=request.POST['lid']
    pid=request.POST['pid']
    valu=request.POST['value']
    pr=Product.objects.get(id=pid)
    st = Stock.objects.get(PRODUCT=pid)
    if float(number) > float(st.S_quantity):
        return JsonResponse({"status": "full"})

    obj=Order()
    obj.O_date=datetime.datetime.now().date()
    obj.o_time=datetime.datetime.now().strftime("%H:%M:%S")
    obj.O_status='order'
    obj.o_delivery=valu
    obj.o_delivery_boy='pending'
    obj.CUSTOMER=Customer.objects.get(LOGIN_id=lid)
    obj.save()

    crt=Cart()
    crt.PRODUCT_id=pid
    crt.Cart_quantity=number
    crt.Cart_price=int(pr.Price)*int(number)
    crt.ORDER=obj
    crt.save()
    return JsonResponse({"status":"ok"})
def andro_payoffline(request):
    lid=request.POST['uid']
    pid=request.POST['pid']
    proamount=request.POST['proamount']
    obj = Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='order')
    for i in obj:
        q = Cart.objects.filter(ORDER=i)
        for j in q:
            cartquantity = j.Cart_quantity
            stockquantity = Stock.objects.get(PRODUCT=j.PRODUCT).S_quantity
            upqnty = int(stockquantity) - int(cartquantity)
            Stock.objects.filter(PRODUCT=pid).update(S_quantity=upqnty)
    obj1 = Order.objects.get(CUSTOMER__LOGIN=lid, O_status='order')

    data = Payment()
    data.ORDER = obj1
    data.Pay_type = 'offline'
    data.Pay_status = 'pending'
    data.pay_date = 'pending'
    data.pay_amount = proamount
    data.save()
    Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='order').update(O_status='offline')

    return JsonResponse({"status": "ok"})
def android_online_payment(request):
    lid = request.POST['uid']
    cartamount = request.POST['amount']
    obj = Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='order')
    for i in obj:
        q = Cart.objects.filter(ORDER=i)
        for j in q:
            cartquantity = j.Cart_quantity
            stockquantity = Stock.objects.get(PRODUCT=j.PRODUCT).S_quantity
            upqnty = int(stockquantity) - int(cartquantity)
            Stock.objects.filter(PRODUCT=j.PRODUCT).update(S_quantity=upqnty)
    obj1 = Order.objects.get(CUSTOMER__LOGIN=lid, O_status='order')

    data = Payment()
    data.ORDER = obj1
    data.Pay_type = 'online'
    data.Pay_status = 'pending'
    data.pay_date = 'pending'
    data.pay_amount = cartamount
    data.save()
    Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='order').update(O_status='paid')

    return JsonResponse({"status": "ok"})

def andro_add_rate(request):
    rat=request.POST['rate']
    lid=request.POST['lid']
    pid=request.POST['pid']
    obj=Rating()
    obj.CUSTOMER=Customer.objects.get(LOGIN_id=lid)
    obj.Rating=rat
    obj.R_date=datetime.datetime.now().date()
    obj.PRODUCT_id=pid
    obj.save()
    return JsonResponse({"status":"ok"})

def andro_send_complaint(request):
    lid=request.POST['lid']
    com=request.POST['complaint']
    data=Complaint()
    data.Cmplnt=com
    data.Cmplnt_date=datetime.datetime.now().date()
    data.Cmplt_reply='pending'
    data.Reply_date='pending'
    data.CUSTOMER=Customer.objects.get(LOGIN_id=lid)
    data.save()
    return JsonResponse({"status":"ok"})

def adro_view_complaint(request):
    lid=request.POST['lid']
    data=Complaint.objects.filter(CUSTOMER=Customer.objects.get(LOGIN_id=lid))
    ary=[]
    for i in data:
        ary.append({
            "id":i.id,
            "com":i.Cmplnt,
            "cdate":i.Cmplnt_date,
            "rpl":i.Cmplt_reply,
            "rdate":i.Reply_date
        })
    return JsonResponse({"status": "ok", "data": ary})

def andro_add_to_cart(request):
    number = request.POST['number']
    lid = request.POST['lid']
    pid = request.POST['pid']
    st = Stock.objects.get(PRODUCT=pid)
    if float(number) > float(st.S_quantity):
        return JsonResponse({"status": "full"})
    obj=Order.objects.filter(CUSTOMER=Customer.objects.get(LOGIN_id=lid),O_status='addtocart')
    if obj.exists():
        data=Cart.objects.filter(ORDER_id=obj[0],PRODUCT_id=pid)
        if data.exists():
            qt=int(data[0].Cart_quantity)+int(number)
            if float(qt) > float(st.S_quantity):
                return JsonResponse({"status": "full"})
            amt=int(data[0].PRODUCT.Price)*int(number)
            pric=int(data[0].Cart_price)+int(amt)
            Cart.objects.filter(ORDER_id=obj[0], PRODUCT_id=pid).update(Cart_quantity=qt,Cart_price=pric)
            return JsonResponse({"status":"ok"})
        else:
            crt=Cart()
            crt.PRODUCT_id=pid
            crt.ORDER_id=obj[0].id
            crt.Cart_quantity=number
            crt.Cart_price=int(crt.PRODUCT.Price)*int(number)
            crt.save()
            return JsonResponse({"status": "ok"})
    else:
        pr = Product.objects.get(id=pid)
        obj1 = Order()
        obj1.O_date = datetime.datetime.now().date()
        obj1.o_time = datetime.datetime.now().strftime("%H:%M:%S")
        obj1.O_status = 'addtocart'
        obj1.CUSTOMER = Customer.objects.get(LOGIN_id=lid)
        obj1.save()

        crt1 = Cart()
        crt1.PRODUCT_id = pid
        crt1.Cart_quantity = number
        crt1.Cart_price = int(pr.Price) * int(number)
        crt1.ORDER= obj1
        crt1.save()
        return JsonResponse({"status": "ok"})


def andro_cartview(request):
    lid=request.POST['lid']
    data=Cart.objects.filter(ORDER__CUSTOMER__LOGIN=lid,ORDER__O_status='addtocart')
    sum=0
    for i in data:
        sum=sum+int(i.Cart_price)
    print(sum, "qttttttttt")

    ary=[]
    for j in data:
        ary.append({
            "id":j.PRODUCT.id,
            "cid":j.id,
            "name":j.PRODUCT.P_name,
            "prize":j.PRODUCT.Price,
            "photo":j.PRODUCT.P_image,
            "quantity":j.Cart_quantity
        })

    return JsonResponse({"status":"ok","data":ary,"sum":sum})

def andro_delete(request):
    id=request.POST['cart_id']
    Cart.objects.get(id=id).delete()
    return JsonResponse({'status': "ok"})

def andro_update_order(request):
    lid=request.POST['lid']
    val=request.POST['value']
    obj=Order.objects.filter(CUSTOMER__LOGIN=lid,O_status='addtocart')
    for i in obj:
        q = Cart.objects.filter(ORDER=i)
        for j in q:
            cartquantity = j.Cart_quantity
            stockquantity = Stock.objects.get(PRODUCT=j.PRODUCT).S_quantity
            upqnty = int(stockquantity)- int(cartquantity)
            Stock.objects.filter(PRODUCT=j.PRODUCT).update(S_quantity=upqnty)
    Order.objects.filter(CUSTOMER__LOGIN=lid,O_status='addtocart').update(o_delivery=val)
    return JsonResponse({"status":"ok"})

def andro_view_approved_orders(request):
    lid=request.POST['lid']
    data=Cart.objects.filter(ORDER__CUSTOMER__LOGIN=lid,ORDER__O_status='approve')
    ary=[]
    for i in data:
        ary.append({
            "id":i.id,
            "pname":i.PRODUCT.P_name,
            "amount":i.Cart_price,
            "image":i.PRODUCT.P_image,
            "oid":i.ORDER.id
        })
    return JsonResponse({"status":"ok",'data':ary})

def andro_offline(request):
    lid=request.POST['uid']
    cartamount=request.POST['cartamount']

    obj = Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='addtocart')
    for i in obj:
        q = Cart.objects.filter(ORDER=i)
        for j in q:
            cartquantity = j.Cart_quantity
            stockquantity = Stock.objects.get(PRODUCT=j.PRODUCT).S_quantity
            upqnty = int(stockquantity) - int(cartquantity)
            Stock.objects.filter(PRODUCT=j.PRODUCT).update(S_quantity=upqnty)
    obj1 = Order.objects.get(CUSTOMER__LOGIN=lid, O_status='addtocart')

    data=Payment()
    data.ORDER=obj1
    data.Pay_type='offline'
    data.Pay_status='pending'
    data.pay_date='pending'
    data.pay_amount=cartamount
    data.save()
    Order.objects.filter(CUSTOMER__LOGIN=lid, O_status='addtocart').update(O_status='paid')


    return JsonResponse({"status":"ok"})


def andro_view_order_history(request):
    lid=request.POST['lid']
    date=datetime.datetime.now().date()
    print(date)
    data= Cart.objects.filter(Q(ORDER__CUSTOMER__LOGIN__lt=lid) & Q(ORDER__O_date__lte=date)
)
    ary=[]
    for i in data:
        ary.append({
            "id":i.id,
            "pname":i.PRODUCT.P_name,
            "quantity":i.Cart_quantity,
            "date":i.ORDER.O_date,
            "image":i.PRODUCT.P_image,
            "amount":i.Cart_price,
            "proid":i.PRODUCT.id
        })
    return JsonResponse({"status": "ok", 'data': ary})


def andro_view_delivery_status(request):
    lid=request.POST['lid']
    data = Cart.objects.filter(ORDER__CUSTOMER__LOGIN=lid)

    ary = []
    for i in data:
        ary.append({
            "id": i.id,
            "pname": i.PRODUCT.P_name,
            "quantity": i.Cart_quantity,
            "dstatus": i.ORDER.o_delivery_boy,
            "image": i.PRODUCT.P_image,

        })
    return JsonResponse({"status": "ok", 'data': ary})




# =========================Staff ============================================================================================
def staff_home(request):
    return render(request,'staff/staff_home.html')

def staff_view_stock(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Stock.objects.all()
        return render(request,'staff/View Stock.html',{'data':data})

def staff_view_orders(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Cart.objects.filter(ORDER__O_status='paid')
        return render(request,'staff/view_order.html',{'data':data})

def staff_view_employee(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Employee.objects.all()
        return render(request,'staff/View Employee.html',{'data':data,'id':id})
def allocate_employee(request,id):
    em=request.POST['select']
    data=Allocate()
    data.ORDER_id=id
    data.EMPLOYEE_id=em
    data.save()
    return HttpResponse("<script>alert('update Employee');window.location='/staff_view_orders'</script>")

def view_customers(request):
    data=Customer.objects.all()
    return render(request,'staff/view_customer.html',{'data':data})

def staff_changepassword(request):
    return render(request,'staff/change password.html')
def staff_changepassword_post(request):
    cpass=request.POST['textfield']
    npass=request.POST['textfield2']
    rpass=request.POST['textfield3']
    log=Login.objects.filter(id=request.session['lid'],password=cpass)
    if log.exists():
        if npass == rpass:
            Login.objects.filter(id=request.session['lid']).update(password=rpass)

            return HttpResponse("<script>alert('update the password');window.location='/staff_home'</script>")
        else:
            return HttpResponse("<script>alert('check your password');window.location='/staff_home'</script>")
    else:
        return HttpResponse("<script>alert('invalid user');window.location='/staff_home'</script>")

def staff_view_profile(request):
    data=Staff.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'staff/view profile.html',{'data':data})


# =========================delivery =======================================================================================
def deliverey_home(request):
    return render(request,'deliveryboy/delivery_home.html')

def view_allocation(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Allocate.objects.filter(EMPLOYEE__LOGIN=request.session['lid'])
        print("alocation",data)
        return render(request,'deliveryboy/view allocation.html',{'data':data})

def deliver_view_product(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        data=Cart.objects.filter(ORDER=id)
        return render(request,'deliveryboy/deliver_viewproduct.html',{'data':data})

def update_delivery_status(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('logout sucessfull');window.location='/'</script>")
    else:
        return render(request,'deliveryboy/update_delivery_status.html',{'id':id})

def update_delivery_status_post(request,id):
    stus=request.POST['RadioGroup1']
    Order.objects.filter(id=id).update(o_delivery_boy=stus)
    return HttpResponse("<script>alert('update status');window.location='/view_allocation'</script>")

def deli_changepassword(request):
    return render(request,'deliveryboy/change password.html')
def deli_changepassword_post(request):
    cpass=request.POST['textfield']
    npass=request.POST['textfield2']
    rpass=request.POST['textfield3']
    log=Login.objects.filter(id=request.session['lid'],password=cpass)
    if log.exists():
        if npass == rpass:
            Login.objects.filter(id=request.session['lid']).update(password=rpass)

            return HttpResponse("<script>alert('update the password');window.location='/deliverey_home'</script>")
        else:
            return HttpResponse("<script>alert('check your password');window.location='/deliverey_home'</script>")
    else:
        return HttpResponse("<script>alert('invalid user');window.location='/deliverey_home'</script>")