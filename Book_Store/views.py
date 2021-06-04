from django.shortcuts import render
from Book_Store.forms import RegistrationForm,StoreRegistrationForm
from django.contrib.auth.models import auth
from django.contrib import messages
from Book_Store.models import StoreBook
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
	return render(request,'index.html')
def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html' )
    else:
        form = RegistrationForm()
    return render(request,'SignUp.html',{'form': form})
def Store_User(request):
    if request.method == 'POST':
        form = StoreRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html' )
    else:
        form = StoreRegistrationForm()
    return render(request,'Store_USer.html',{'form': form})
def login(request):
	if request.method == 'POST':
		Username=request.POST['Username']
		password=request.POST['Password']
		user=auth.authenticate(username=Username,password=password)
		if user is not None:
			auth.login(request,user)
			return render(request, 'index.html')
		else:
			messages.info(request,'Invalid Credentials')
			msg='Invalid Credentials'
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return render(request,'index.html')
def AddNewBook(request):
	Storeuser=request.user
	if request.method == 'POST':
		Author=request.POST['Author']
		Book=request.POST['Book']
		Quantity=request.POST['Quantity']
		if int(Quantity)<= 1:
			messages.info(request,'invalid Credentials')
			msg='Invalid Credentials'
			return render(request,'AddNewBook.html',{'msg':msg,'Storeuser':Storeuser})
		else:
			first_name=request.user.first_name
			last_name=request.user.last_name
			temp = StoreBook(Storeuser=request.user,Book=Book,Author=Author,
			Quantity=Quantity,first_name= first_name,last_name=last_name)
			temp.save()
			return render(request, 'index.html')
	else:
		return render(request,'AddNewBook.html',{'Storeuser':Storeuser})
def view_Stores(request):
	Storebook=get_user_model().objects.filter(is_staff=True)
	return render(request, 'view_Stores.html',{'Storebook':Storebook})
def info(request,user_name):
	BookInStore=StoreBook.objects.filter(Storeuser=user_name)
	Store_record=get_user_model().objects.get(username=user_name)
	print(BookInStore)
	Store=Store_record.first_name+' '+Store_record.last_name
	print(Store)
	if BookInStore is None:
		msg="The store have not Inserted any Book to database."
		return render(request,'BookInStore.html',{'msg':msg,'Store':Store})
	else:
		return render(request,'BookInStore.html',{'BookInStore':BookInStore,'Store':Store})
def get_book(request,id):
	#BookInStore=StoreBook.objects.get(id=id)
	return render(request,'index.html')
def getbook(request,id):
	BookInStore=StoreBook.objects.get(id=id)
	Storeuser=BookInStore.Storeuser
	Author=BookInStore.Author
	Book=BookInStore.Book
	Quantity=BookInStore.Quantity
	if Quantity==0:
		msg='Sorry Currently Book is out of stock'
		return render(request,'msg.html',{'msg':msg})
	if request.method == 'POST' and Quantity != 0:
		StoreBook.objects.filter(id=id).update(Quantity=Quantity-1)
		return render(request,'index.html')
	return render(request,'get_book.html',{'Storeuser':Storeuser,
'Author':Author,'Book':Book,'Quantity':Quantity})
def Update_list(request):
	BookInStore=StoreBook.objects.filter(Storeuser=request.user)
	return render(request,'Update_list.html',{'BookInStore':BookInStore})
def Update_record(request,id):
	BookInStore=StoreBook.objects.get(id=id)
	Storeuser=BookInStore.Storeuser
	Author=BookInStore.Author
	Book=BookInStore.Book
	Quantity=BookInStore.Quantity
	if request.method == 'POST':
		Quantity=request.POST['Quantity']
		StoreBook.objects.filter(id=id).update(Quantity=Quantity)
		BookInStore=StoreBook.objects.filter(Storeuser=request.user)
		return render(request,'Update_list.html',{'Storeuser':Storeuser,'BookInStore':BookInStore})
	else:
		return render(request,'Update_record.html',{'Storeuser':Storeuser,
	'Author':Author,'Book':Book,'Quantity':Quantity})
def Delete_book(request):
	BookInStore=StoreBook.objects.filter(Storeuser=request.user)
	return render(request,'Delete_book.html',{'BookInStore':BookInStore})
def Delete_record(request,id):
	BookInStore=StoreBook.objects.get(id=id)
	Storeuser=BookInStore.Storeuser
	Author=BookInStore.Author
	Book=BookInStore.Book
	Quantity=BookInStore.Quantity
	if request.method == 'POST':
		StoreBook.objects.filter(id=id).delete()
		return render(request,'index.html')
	return render(request,'Delete_Confirm.html',{'Storeuser':Storeuser,
'Author':Author,'Book':Book,'Quantity':Quantity})
