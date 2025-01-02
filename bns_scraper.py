from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
from tqdm import tqdm

def fetch_section_content_safari(section_number, driver):
    """Fetch content using Selenium for JavaScript-rendered pages."""
    url = f"https://devgan.in/bns/section/{section_number}/"
    print(f"Fetching content for Section {section_number} from {url}")
    try:
        driver.get(url)
        
        # Wait for the page to load and locate the <a> and <table> tags
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )

        # Scrape <a> tags (links)
        a_tags = driver.find_elements(By.TAG_NAME, "a")
        links = [a.get_attribute("href") for a in a_tags]

        # Scrape <table> tags (tables)
        tables = driver.find_elements(By.TAG_NAME, "table")
        table_data = []
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            table_rows = []
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                cols_data = [col.text for col in cols]
                table_rows.append(cols_data)
            table_data.append(table_rows)

        print(f"Successfully fetched content for Section {section_number}")
        return {"tables": table_data}
    
    except Exception as e:
        print(f"Error fetching Section {section_number}: {e}")
        return None

def scrape_all_sections_safari():
    """Scrape content using Safari WebDriver and store in a JSON file."""
    # Initialize Safari WebDriver
    driver = webdriver.Safari()

    sections_to_scrape = range(1, 359)
    bns_data = []

    for section_number in tqdm(sections_to_scrape, desc="Scraping Sections"):
        content = fetch_section_content_safari(section_number, driver)
        if content:
            bns_data.append({
                "section_number": section_number,
            
                "tables": content["tables"]
            })

    driver.quit()

    # Save data to JSON
    output_dir = "output"
    output_file = os.path.join(output_dir, "bns_sections.json")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_file, "w") as json_file:
        json.dump(bns_data, json_file, indent=4)
    print(f"Scraping complete. Data saved to {output_file}")

if __name__ == "__main__":
    scrape_all_sections_safari()
