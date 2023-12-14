
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout


from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    



@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Add your registration validation logic here
        # For example, check if the username is unique and the password is strong enough.

        try:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # You may want to perform additional actions here, such as sending a welcome email.

            return JsonResponse({
                'username': user.username,
                'status': True,
                'message': 'Registration successful!',
            }, status=201)  # HTTP 201 Created for successful resource creation
        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Registration failed. {str(e)}',
            }, status=400)  # HTTP 400 Bad Request for registration failure

    else:
        return JsonResponse({
            'status': False,
            'message': 'Invalid request method. Use POST to register.',
        }, status=405)  # HTTP 405 Method Not Allowed for other request methods
