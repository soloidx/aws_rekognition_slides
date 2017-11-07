#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT START OMIT
import boto3
from pprint import pprint
# IMPORT END OMIT

client = boto3.client('rekognition')

# CODE START OMIT
with open('ex05_image_2.jpg', 'rb') as image_file:
    response = client.detect_moderation_labels(
        Image={
            'Bytes': image_file.read()
        },
        MinConfidence=40
    )

    pprint(response)

# CODE END OMIT
