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
image_1 = open('carlos_1.jpg', 'rb')
image_2 = open('carlos_2.jpg', 'rb')
image_3 = open('carlos_3.png', 'rb')

response = client.compare_faces(
    SourceImage={
        'Bytes': image_1.read()
    },
    TargetImage={
        'Bytes': image_2.read()
    },
    SimilarityThreshold=70
)

pprint(response)

image_1.close()
image_2.close()
image_3.close()

# CODE END OMIT
