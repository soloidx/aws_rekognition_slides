#!/usr/bin/env bash
# small hack to run the test inside the presentation
cd code/ex01/

# START OMIT
pip install awscli --upgrade
pip install boto3
aws configure
# END OMIT
