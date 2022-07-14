from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def landing(request):
    return render(

        request,
        'survey/index.html',
    )
def submit(request):
    if request.method == 'POST':
        print("post 성공")
        print(request.POST)
        x = request.POST.get('service', "")
        print("Zxc"+x)
        x = request.POST.get('fname', "")
        print("ss"+x)
        return redirect('/')
