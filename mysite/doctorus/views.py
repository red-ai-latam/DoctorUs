from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils import timezone
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.response import TemplateResponse
from django import template

import uuid
import subprocess
import socket
import datetime
from threading import Thread
import datetime
import time
#from .models import Odometry
#from .models import Motherboard
#from .models import Construction
#from .models import Energy
#from .models import Report
#from .models import Components
#from .models import Tower
from itertools import chain
from operator import attrgetter
import os
from subprocess import check_output
import json


from collections import defaultdict
import datetime
from pprint import pprint

from google.cloud import datastore
import google.cloud.exceptions

from docx import Document

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


class IndexView(generic.ListView):

    template_name = 'doctorus/index.html'
    context_object_name = 'query'

    
    def get_queryset(self):
    
        '''
        queryset = {'latest_report': Report.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:1], 
                    
                    'latest_report_list': Report.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5],

                    'latest_component_list': Components.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5],

                    'latest_construction_list': Construction.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5],

                    'latest_energy_list': Energy.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5],

                    'latest_motherboard_list': Motherboard.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5],

                    'latest_odometry_list': Odometry.objects.filter(
                            pubDate__lte=timezone.now()
                        ).order_by('-pubDate')[:5]



                    }
    
        '''

        queryset = {}
        
        return queryset
	

