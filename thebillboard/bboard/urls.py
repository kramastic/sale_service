from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from bboard.views import (
    AddAdv,
    DeleteAdv,
    EditAdv,
    GetAdvByCategory,
    GetAllAdvView,
    LoginUser,
    MyAdv,
    RegisterUser,
    ShowAdv,
)

urlpatterns = [
    path("", GetAllAdvView.as_view(), name="main"),
    path("category/<str:cat>/", GetAdvByCategory.as_view(), name="by_category"),
    path("adv/<int:pk>/", ShowAdv.as_view(), name="show_adv"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="main"), name="logout"),
    path("create/", AddAdv.as_view(), name="add_adv"),
    path("user_<int:pk>/", MyAdv.as_view(), name="my_adv"),
    path("edit_adv/<int:pk>", EditAdv.as_view(), name="edit_adv"),
    path("del_adv/<int:pk>", DeleteAdv.as_view(), name="del_adv"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
