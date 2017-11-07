#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT START OMIT
import boto3
from pprint import pprint
# IMPORT END OMIT

client = boto3.client('rekognition')

# CODE START OMIT
with open('ex04_image_2.jpg', 'rb') as image_file:
    response = client.recognize_celebrities(
        Image={
            'Bytes': image_file.read()
        }
    )

    pprint(response)

# CODE END OMIT
