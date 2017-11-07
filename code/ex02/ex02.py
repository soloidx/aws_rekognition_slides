#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT START OMIT
import boto3
from pprint import pprint
# IMPORT END OMIT

# CLIENT START OMIT
client = boto3.client('rekognition')
# CLIENT END OMIT

# CODE START OMIT
with open('ex02_image.jpg', 'rb') as image_file:
    response = client.detect_labels(
        Image={
            'Bytes': image_file.read()
        },
        MaxLabels=10,
        MinConfidence=50
    )

    pprint(response)

# CODE END OMIT
