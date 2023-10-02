# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # The home page
    path("homepage/", views.homepage, name="homepage"),
    path("", views.login, name="login"),
    # path('bot/', bot.send_help_message , name='bot'),
    path("signOut/" , views.signOut , name="signOut"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    ######3333333333=======================================================================================broker
    path("createBroker/", views.createBroker, name="createBroker"),
    path("showBroker/", views.showBroker, name="showBroker"),
    path("deleteBroker/<int:id>", views.deleteBroker, name="deleteBroker"),
    path("updateBroker/<int:id>", views.updateBroker, name="updateBroker"),
    ######3333333333=======================================================================================user
    path("createUser/", views.createUser, name="createUser"),
    path("showUser/", views.showUser, name="showUser"),
    path("deleteUser/<int:id>", views.deleteUser, name="deleteUser"),
    path("updateUser/<int:id>", views.updateUser, name="updateUser"),
    ######3333333333=======================================================================================strategy
    path("createStrategy/", views.createStrategy, name="createStrategy"),
    path("showStrategy/", views.showStrategy, name="showStrategy"),
    path("deleteStrategy/<int:id>", views.deleteStrategy, name="deleteStrategy"),
    path("updateStrategy/<int:id>", views.updateStrategy, name="updateStrategy"),
    path("showStrategy/changeStatus", views.changeStatus, name="changeStatus"),
    # =====================================================================================================trading account
    path(
        "createTradingAccount/", views.createTradingAccount, name="createTradingAccount"
    ),
    # path('saveTradingAccount/',views.saveTradingAccount, name='saveTradingAccount'),
    path("showTradingAccount/", views.showTradingAccount, name="showTradingAccount"),
    # path('update_saveTradingAccount/',views.update_saveTradingAccount, name='update_saveTradingAccount'),
    path(
        "deleteTradingAccount/<int:id>",
        views.deleteTradingAccount,
        name="deleteTradingAccount",
    ),
    path(
        "updateTradingAccount/<int:id>",
        views.updateTradingAccount,
        name="updateTradingAccount",
    ),
    # =========================================================================================================ticker
    # path('ticker',views.ticker,name='ticker'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
