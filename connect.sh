#!/bin/bash
# This script creates a de-attached run of tweets.py

nohup python tweets.py > /dev/null 2>/dev/null & 
