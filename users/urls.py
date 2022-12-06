from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
    PasswordResetView,
)

from .views import SignUpView


urlpatterns = [
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='registration/password_change_dn.html'
        ),
        name='password_change_done',
    ),

    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='registration/password_change_frm.html'
        ),
        name='password_change_form'
    ),

    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_dn.html',
        ),
        name='password_reset_done',
    ),

    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset_frm.html',
        ),
        name='password_reset_form',
    ),

    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_cnfrm.html',
        ),
        name='password_reset_confirm',
    ),

    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_cmplt.html',
        ),
        name='password_reset_complete',
    ),

    path('signup/', SignUpView.as_view(), name='signup'),
]
