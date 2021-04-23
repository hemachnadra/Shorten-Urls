from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
import random,string
from .models import Url as model_url
from .forms import Url as form_url
from .models import Url



# Create your views here.
def generate_random_string(request):
    data = model_url.objects.all()
    form = form_url()
    random_str=''
    alpha_numaric=string.ascii_letters+string.digits
    for x in range(10):
        random_str=random_str+random.choice(alpha_numaric)

    if request.method=="POST":
        form=form_url(request.POST)
        if form.is_valid():
            
            url=form.cleaned_data['url']

            ex_url="https://www.google.com"

            index_no=url.find('.')
            http_=ex_url[:11]

            
            if http_!=url[:index_no]:

                url=http_+url[index_no:]

            url_exist = data.filter(url=url).exists()
            if not url_exist:
                slug = ''.join(random_str)
                new_url = model_url(url=url, slug=slug)
                new_url.save()
            
    context={
        'form':form,
        'data':data,
    }

    return render(request,'index.html',context)


def delete(request,url):
    data1=model_url.objects.get(url=url)
    data1.delete()
    return redirect('/')

    


    


