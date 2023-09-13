from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Edwin',
        'class': 'PBP E',
        'jumlah_angkatan': '4'
    }

    return render(request, "main.html", context)
