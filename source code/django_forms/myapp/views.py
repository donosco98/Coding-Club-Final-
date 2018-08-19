from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,Snippetform
from .models import Snippet
from django.contrib.auth.decorators import login_required
from paytm.payments import PaytmPaymentPage
from paytm import Checksum
from paytm.payments import VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def contact(request):
    book=Snippet.objects.all()

    return render(request,'myapp/home.html',{'book':book } ,)

@login_required
def page(request):
    return redirect('http://127.0.0.1:8000/list/')



@login_required
def Snippet_details(request):
    form=Snippetform(request.POST)
    title1 = request.POST.get('book_title')
    if request.method=='POST':


        if form.is_valid():
            print("********")
            form.save()




    form=Snippetform()

    return render(request,'myapp/form.html',{'form':form,'title1':title1 } ,)

def payment(request):
    # provide your unique order id
    # if you don't have your unique order id then
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    cust_id = "payment_maker@email.com"
    data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': cust_id
            }
    return PaytmPaymentPage(data_dict)

@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db
        #SAVE THIS ORDER ID TO DB FOR TRANSACTION HISTORY
        return JsonResponse(resp['paytm'])
    else:
        return HttpResponse("Verification Failed")
    return HttpResponse(status=200)

@login_required
def price_increase(request,id):
        print("gsg")
        book=Snippet.objects.get(pk=id)
        book.price+=50
        book.save()
        return redirect('http://127.0.0.1:8000/list/'+str(id))

@login_required
def price_decrease(request,id):
        print("gsg")
        book=Snippet.objects.get(pk=id)
        book.price-=50
        book.save()
        return redirect('http://127.0.0.1:8000/list/'+str(id))


@login_required
def detail(request,id):
    book=Snippet.objects.get(pk=id)
    return render(request,'myapp/detail.html',{'text':book})
    return redirect('http://127.0.0.1:8000/list/')

@login_required
def homes(request):
    return redirect('http://127.0.0.1:8000/list/')

@login_required
def home(request,id):
    return redirect('http://127.0.0.1:8000/list/')

def login(request):

    return render(request,'myapp/login.html')
