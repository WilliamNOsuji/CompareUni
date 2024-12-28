from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection as ChromiumRemoteConnection
import time
import csv

AUTH = 'brd-customer-hl_367ac3bc-zone-compareuni:u5wtbyk6sr12'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    options = ChromeOptions()
    driver = webdriver.Remote(command_executor=sbr_connection, options=options)
    
    try:
        print('Connected! Navigating...')
        driver.get('https://www.etsmtl.ca/programmes-formations/baccalaureats')
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        
        # Define the column headers for the CSV file
        headers = ['Program Name', 'Credits', 'Session d\'admission et dates limites', 'Cycle', 'Contingentement', 'Régime des études', 'Langue d\'enseignement', 'Stages', 'Grade']

        # Open the CSV file for writing
        with open('program_details.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

            # Collect all program elements
            program_elements = driver.find_elements(By.CSS_SELECTOR, '.c-projects-search__results .c-search-results__item.-show')
            
            # Iterate through each program element
            for index in range(len(program_elements)):
                # Recollect the program elements to avoid stale element reference
                program_elements = driver.find_elements(By.CSS_SELECTOR, '.c-projects-search__results .c-search-results__item.-show')
                element = program_elements[index]

                # Click on the link within the program element
                link = element.find_element(By.CSS_SELECTOR, '.c-search-result__title a')
                link.click()
                print(f'Clicked on the link for program {index + 1}')
                time.sleep(2)  # Wait for the page to load

                # Extract the general information of the program
                program_name = driver.find_element(By.CSS_SELECTOR, '.o-title-1').text
                credits = driver.find_element(By.XPATH, "//div[contains(text(), 'Crédits')]/following-sibling::div").text
                print(credits)
                session_admission = driver.find_element(By.XPATH, "//div[contains(text(), \"Session d'admission et dates limites\")]/following-sibling::div").text
                cycle = driver.find_element(By.XPATH, "//div[contains(text(), 'Cycle')]/following-sibling::div").text
                contingentement = driver.find_element(By.XPATH, "//div[contains(text(), 'Contingentement')]/following-sibling::div").text
                regime_etudes = driver.find_element(By.XPATH, "//div[contains(text(), 'Régime des études')]/following-sibling::div").text
                langue_enseignement = driver.find_element(By.XPATH, "//div[contains(text(), \"Langue d'enseignement\")]/following-sibling::div").text
                stages = driver.find_element(By.XPATH, "//div[contains(text(), 'Stages')]/following-sibling::div").text
                grade = driver.find_element(By.XPATH, "//div[contains(text(), 'Grade')]/following-sibling::div").text

                # Write the extracted information to the CSV file
                writer.writerow([program_name, credits, session_admission, cycle, contingentement, regime_etudes, langue_enseignement, stages, grade])
                print(f'Stored information for program {index + 1}')

                # Navigate back to the search results page
                driver.back()
                time.sleep(2)  # Wait for the page to load

    finally:
        driver.quit()

if __name__ == '__main__':
    main()