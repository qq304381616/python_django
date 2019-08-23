from django.conf.urls import url

from . import view
from . import viewHtml

from django.conf.urls import *
from . import view,testdb

urlpatterns = [
    url(r'^$', view.hello),
    url('hello/', viewHtml.hello),
    url(r'^testdbAdd$', testdb.testdbAdd),
    url(r'^testdbFind$', testdb.testdbFind),
    url(r'^testdbUpdate$', testdb.testdbUpdate),
    url(r'^testdbDel$', testdb.testdbDel),
]
