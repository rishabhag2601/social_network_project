from django.urls import path
from .views import SignupView, LoginView, SendFriendRequestView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('send-friend-request/', SendFriendRequestView.as_view(), name='send_friend_request'),
]
