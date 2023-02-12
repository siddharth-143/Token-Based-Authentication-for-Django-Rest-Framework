from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserchangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, UserLogoutView, CsvFilesList
from . import function_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserchangePasswordView.as_view(), name='changepassword'), 
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'), 
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'), 
    path('logout/', UserLogoutView.as_view(), name='logout'), 
    path('csvlist/', view=CsvFilesList.as_view(), name='csv-list'),
    path('upload/', view=function_view.upload_csv, name='upload_csv'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
