import os
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import csv 
import time 
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright
import playwright

target_url_linkedin = "https://www.linkedin.com/jobs/"
def run(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)
        page = browser.new_page()


        page.goto(url)
        
# def process_url(url):


run(target_url_linkedin)