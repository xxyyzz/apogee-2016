from django.conf.urls import patterns, url
from lacuna.views import *
urlpatterns = [
    url(r'^$', home),
    url(r'^status/$', status),
    url(r'^login/$', user_login),
    url(r'^storyline/$', storyline),
    url(r'^leaderboard/$', leaderboard),
    url(r'^dvm/getlevel/$', dvm_level_get),
    url(r'^informals/getlevel/$', informals_level_get),
    url(r'^informals/verifylevel/$', informals_level_verify),
    url(r'^dvm/chesspuzzle/$', dvm1verify),
    url(r'^dvm/qrcode/$', dvm2verify),
    url(r'^dvm/filterpuzzle/$', dvm3verify),
    url(r'^dvm/brainfuck/$', dvm4verify),
    url(r'^dvm/directionalist/$', dvm5verify),
    url(r'^dvm/mapcoordinates/$', dvm6verify),
    url(r'^dvm/magicsquare/$', dvm7verify),
    url(r'^dvm/unzipthemystery/$', dvm8verify),
    url(r'^dvm/onetwotheree/$', dvm9verify),
    url(r'^dvm/poster/$', dvm10verify),
    url(r'^dvm/colourmatch/$', dvm11verify),
    url(r'^dvm/dancingman/$', dvm12verify),
]
