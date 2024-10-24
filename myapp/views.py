from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def fun1(request):
    return HttpResponse("Hiiii")
def fun2(request):
    return HttpResponse('<h1>good morning</h1>')
def fun3(request):
    return render(request,'new.html',{"name":"meethu"})
def fun4(request):
    context = {
        'fruits':["apple","orange","grape"]
    }
    return render(request,'fruit.html',context)
def fun5(request):
    item=[
        {'name':"Laptop","price":200,"quantity":10},
        {'name':'phone','price':100,'quantity':5},
        {'name':'TV','price':300,'quantity':15}
    ]
    return render(request,'item.html',{'items':item})
def fun6(request):
    list=[
        {'name':'Laptop','price':'$999.99','stock':'In Stock'},
        {'name':'Smartphone','price':'$599.99','stock':'Out of Stock'},
        {'name':'Tablet','price':'$299.99','stock':'In Stock'},
        {'name':'Headphones','price':'$149.99','stock':'In Stock'}
    ]
    return render(request,'product_list.html',{'list':list})
def fun7(request):
    data=usermodel.objects.all()
    return render(request,'all.html',{'data1':data})
def fun8(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=usermodel()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
    return render(request,'add_user.html')
def fun9(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        b=Book()
        b.book_id=id
        b.title=title
        b.author=author
        b.published_date=date
        b.isbn=isbn
        b.save()
    return render(request,'add_book.html')
def fun10(request):
    data=Book.objects.all()
    return render(request,'display_book.html',{'display':data})
def fun11(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        emp=Employee()
        emp.emp_id=id
        emp.name=name
        emp.age=age
        emp.phone=phone
        emp.save()
        return redirect('fun11')
    return render(request,'add_employee.html')
def fun12(request):
    data=Employee.objects.all()
    return render(request,'display_employee.html',{'emp':data})
def fun13(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('des')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        pro=Product()
        pro.name=name
        pro.description=description
        pro.price=price
        pro.quantity=quantity
        pro.save()
        return redirect('product_table')
    return render(request,'add_product.html')
def fun14(request):
    value=Product.objects.all()
    return render(request,'product_view.html',{'product':value})
def fun15(request,id):
    value=Employee.objects.get(emp_id=id)
    value.delete()
    return redirect('fun11')
def fun16(request,id):
    value=Employee.objects.filter(emp_id=id)
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        emp=Employee()
        emp.emp_id=id
        emp.name=name
        emp.age=age
        emp.phone=phone
        emp.save()
        return redirect('fun11')
    return render(request,'update_employee.html',{'employee':value})
def cus_add(request):
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('dob')
        cus=Customer()
        cus.first_name=f_name
        cus.last_name=l_name
        cus.email=email
        cus.phone_number=phone
        cus.address=address
        cus.date_of_birth=date
        cus.save()
        return redirect('display_customer')
    return render(request,'add_customer.html')
def cus_display(request):
    value=Customer.objects.all()
    return render(request,'display_customer.html',{'customer':value})
def cus_update(request,id):
    update=Customer.objects.get(id=id)
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('dob')
        update.first_name=f_name
        update.last_name=l_name
        update.email=email
        update.phone_number=phone
        update.address=address
        update.date_of_birth=date
        update.save()
        return redirect('display_customer')
    return render(request,'update_customer.html',{'update':update})
def cus_delete(request,id):
    value=Customer.objects.get(id=id)
    value.delete()
    return redirect('display_customer')
def blog_add(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        blog=Post()
        blog.title=title
        blog.content=content
        blog.author=author
        blog.save()
        return redirect('blog_display')
    return render(request,'add_blogpost.html')
def blog_display(request):
    values=Post.objects.all()
    return render(request,'display_blogpost.html',{'blog':values})
def blog_update(request,id):
    blog=Post.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        blog.title=title
        blog.content=content
        blog.author=author
        blog.save()
        return redirect('blog_display')
    return render(request,'update_blogpost.html',{'blog':blog})

def product_table(request):
    value=product_for_user.objects.all()
    return render(request,'product_table.html',{'pro':value})
def add_productForUser(request):
    data=user_product.objects.all()
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        add=product_for_user()
        add.product_id=id
        add.product_name=name
        add.users=user_product.objects.get(user_id=request.POST.get('user_id'))
        add.save()
    return render(request,'add_product_for_user.html',{'data1':data})




def publisher_table(request):
    publish=Publisher.objects.all()
    return render(request,'publisher_table.html',{'publisher':publish})
def publisher_book(request):
    publish=Book_publisher.objects.all()
    return render(request,'publisher_book_table.html',{'book':publish})
def add_publisher_book(request):
    data=Publisher.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        p=Book_publisher()
        p.title=title
        p.publication_date=date
        p.isbn=isbn
        p.publisher=Publisher.objects.get(id=request.POST.get('publisher_id'))
        p.save()
        return redirect('publisher_book')
    return render(request,'book_publisher_Add.html',{'dataa':data})
def delete_publisher(request,id):
    data=Publisher.objects.get(id=id)
    data.delete()
    return redirect('publisher_table')
def update_publisherr(request,id):
    data=Publisher.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        data.name=name
        data.address=address
        data.email=email
        data.save()
        return redirect('publisher_table')
    return render(request,'update_publisher.html',{'dataa':data})
def update_book_publisher(request,id):
    data=Publisher.objects.all()
    data1=Book_publisher.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        data1.title=title
        data1.publication_date=date
        data1.isbn=isbn
        data1.publisher=Publisher.objects.get(id=request.POST.get('aaaa'))
        data1.save()
        return redirect('publisher_book')
    return render(request,'book_publisher_update.html',{'data':data,'data1':data1})
def delete_book_publisher(request,id):
    obj=Book_publisher.objects.get(id=id)
    obj.delete()
    return redirect('publisher_book')


def displayCourses(request):
    display=Course.objects.all()
    return render(request,'display_courses.html',{'disp':display})
def addStudent(request):
    data=Course.objects.all()
    if request.method == 'POST':
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        e_mail=request.POST.get('email')
        phone_no=request.POST.get('phone')
        obj=Student()
        obj.first_name=f_name
        obj.last_name=l_name
        obj.email=e_mail
        obj.phone_number=phone_no
        obj.course=Course.objects.get(id=request.POST.get('course'))
        obj.save()
        return redirect('displayStudents')
    return render(request,'add_student.html',{'data':data})
def displayStudents(request):
    display=Student.objects.all()
    return render(request,'display_students.html',{'disp':display})
def displaySpecificStudent(request,id):
    data=Student.objects.get(id=id)
    return render(request,'display_specific_student.html',{'specific':data})
def updateStudent(request,id):
    data=Student.objects.get(id=id)
    dataa=Course.objects.all()
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        data.first_name=fname
        data.last_name=lname
        data.email=email
        data.phone_number=phone
        data.course=Course.objects.get(id=request.POST.get('course'))
        data.save()
        return redirect('displayStudents')
    return render(request,'update_student.html',{'data':data,'dataa':dataa})
def deleteStudent(request,id):
    dele=Student.objects.get(id=id)
    dele.delete()
    return redirect('displayStudents')
def specificCourse(request,id):
    c=Course.objects.get(id=id)
    data=Student.objects.filter(course=c)
    return render(request,'display_specific_course.html',{'dataa':data,'cc':c})



def add_organizer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj=Organizer()
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_add_organizer.html')
def add_event(request):
    org_names=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj=Event()
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_add_event.html',{'org_list':org_names})
def display_organizer(request):
    org=Organizer.objects.all()
    return render(request,'em_display_organizer.html',{'org':org})
def display_event(request):
    eve=Event.objects.all()
    return render(request,'em_display_event.html',{'event':eve})
def update_organizer(request,id):
    obj=Organizer.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_update_organizer.html',{'obj':obj})
def update_event(request,id):
    orgg=Organizer.objects.all()
    obj=Event.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_update_event.html',{'obj':obj,'organize':orgg})
def delete_organizer(request,id):
    dlt=Organizer.objects.get(id=id)
    dlt.delete()
    return redirect('display_organizer')
def delete_event(request,id):
    dlt=Event.objects.get(id=id)
    dlt.delete()
    return redirect('display_event')
        