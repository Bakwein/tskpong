from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('home', home, name='home'),
    path('friend', friend, name='friend'),
    path('profile', profile, name='profile'),
    path('chats', chats, name='chats'),
    path('main', main, name='main'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('tester', tester, name='tester'),
    path('get_gamers/', get_gamers, name='get_gamers'), 
    path('get_all_gamers/', get_all_gamers, name='get_all_gamers'), 
    path('create/', create_gamer, name='create_gamer'),  
    path('login_view/', login_view, name='login_view'),  
    path('addform', addform, name="addform"),
    path('addfriend/', addfriend, name="addfriend"),
    path('get_all_friend/', get_all_friend, name="get_all_friend"),
    path('game', game, name="game"),
    path('gameai',gameai, name="gameai"),
    path('tictactoe', tictactoe, name="tictactoe"),
    path('get_message/', get_message, name="get_message"),
    path('addmessage/', addmessage, name="addmessage"),
    path('block_chat/', block_chat, name="block_chat"),
    path('block_controls/', block_controls, name="block_controls"),
    path('postMatchHistory/', postMatchHistory, name="postMatchHistory"),
    path('addMatchHistory/', addMatchHistory, name="addMatchHistory"),
    path('getGameHistory/', getGameHistory, name="getGameHistory"),
    path('showmatch/', showmatch, name="showmatch"),
    path('registerkey/', registerkey, name="registerkey"),
    path('create_user/', create_user, name="create_user"),
    path('tournament', tournament, name="tournament"),
    path('createTournament/', createTournament, name="createTournament"),
    path('getTournaments/', getTournaments, name="getTournaments"),
    path('infotournaments', infotournaments, name="infotournaments"),
    path('addplayer', addplayer, name="addplayer"),
    path('my_test/', my_test, name="my_test"),
    path('get_all_player/', get_all_player, name="get_all_player"),
    path('create_match/', create_match, name="create_match"),
    path('starttournament/', starttournament, name="starttournament"),
    path('oauth/callback', oauth_callback, name="oauth_callback"),
    path('updateMatchHistory/', updateMatchHistory, name="updateMatchHistory"),
    path('endtournament/', endtournament, name="endtournament"),
    path('login_key/', login_key, name="login_key"),
    path('oauth/login_key/', login_key, name="login_key"),
    path('userprofile', userprofile, name="userprofile"),
    path('get_user/', get_user, name="get_user"),


]