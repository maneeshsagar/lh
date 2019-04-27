# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import datetime
from django.db import models
import psycopg2

class Labours(models.Model):
    l_name=models.CharField(max_length=70)
    l_con_no=models.CharField(max_length=10)
    l_pass=models.CharField(max_length=20)
    l_id_no=models.CharField(max_length=50)
    l_addr=models.CharField(max_length=100)
    pres=models.IntegerField(default=0)

class Employers(models.Model):
    e_name=models.CharField(max_length=70)
    e_con_no=models.CharField(max_length=10)
    e_mail=models.CharField(max_length=50)
    e_pass=models.CharField(max_length=20)
    e_id_no=models.CharField(max_length=50)

class Feed(models.Model):
    e_con_no=models.CharField(max_length=10)
    l_con_no=models.CharField(max_length=10)
    comment=models.CharField(max_length=500)