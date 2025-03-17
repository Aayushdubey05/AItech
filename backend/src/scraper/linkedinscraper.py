import os
import sys 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import csv 
import time 
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright
import playwright

target_url_linkedin = "https://www.linkedin.com/"
def run(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= True)
        page = browser.new_page()


        page.goto(url)
        print("Opened linkedin.com")

        jobs_link = page.query_selector("a[href*='/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs']")

        if jobs_link:
            jobs_link.click()
            page.wait_for_load_state("domcontentloaded")
            print("Navigated to the Jobs Page....")

            #Detected the Sign-up pop to avoid that here is the code 
            time.sleep(4)
            try:
                first = page.query_selector(".top-level-modal-container")
                print("Accessed First")
                second = first.query_selector(".modal")
                print("Accessed Second")
                third = second.query_selector(".modal__overlay")
                print("accessed Third")
                section = third.query_selector(".modal__wrapper")
                print("accessed Forth")
                close_btn = section.wait_for_selector(".modal__dismiss")

                if close_btn:
                    close_btn.click()
                    print("Sign-In Popup Closed")
            except Exception:
                print("Signup pop up is not detected ")


            #Waiting for job listing to be loaded 
            page.wait_for_selector(".jobs-search__results-list")
            print("Jobs Loaded...")

            job_list = page.query_selector(".jobs-search__results-list")
            jobs_item = job_list.query_selector_all("li")

            print(f"Total number of jobs found: {len(jobs_item)}")

            jobs_for_autojob = []
            for data_reference_id in jobs_item:
                job_class = data_reference_id.query_selector('.base-card')

                #Extracting the Job links for each job 
                job_link = data_reference_id.query_selector('a')
                job_href = job_link.get_attribute('href') if job_link else 'No link Found'

                jobs_for_autojob.append({
                    'class': job_class,
                    'link': job_href
                })

        else:
            print("Jobs link not found!")

    return jobs_for_autojob
# def process_url(url):


jobs = run(target_url_linkedin)
for job in jobs:
    print(f"Class: {job['class']}\nLink: {job['link']}\n{'-'*50}")