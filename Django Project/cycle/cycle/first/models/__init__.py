from operator import imod
from django.db import models
from location_field.models.plain import PlainLocationField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from django.conf import settings
from django.db.models.signals import pre_save
import os
from PIL import Image

from .user import *
from .cyclepost import *