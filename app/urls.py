from app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_view
from .forms import LoginForm , MyPasswordChangeForm , MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    path('paymentdone/', views.payment_done, name='paymentdone'),   
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),  
    path('buy/', views.buy_now, name='buy-now'),  
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'), 
    path('Readingglasses/',views.Readingglasses,name='Readingglasses'),
    path('Readingglasses/<slug:data>', views.Readingglasses, name='readingdata'),
    path('Goggles/',views.Goggles, name='Goggles'),
    path('Goggles/<slug:data>', views.Goggles, name='gogglesdata'),
    path('Sunglasses/',views.Sunglasses, name='Sunglasses'),
    path('Sunglasses/<slug:data>', views.Sunglasses, name='sunglassesdata'),
    path('Contactlenses/',views.Contactlenses, name='Contactlenses'),
    path('Contactlenses/<slug:data>', views.Contactlenses, name='Contactlensesdata'),   
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html/', authentication_form=LoginForm),name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    # path('checkout/', views.checkout.as_view(), name='checkout'), 
    # path('checkout/',views.checkout, name='checkout'), 
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'), 
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class= MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)