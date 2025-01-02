# BNS Web Scraping

This project is designed to scrape content from the [devgan.in](https://devgan.in) website. The script extracts information from the sections of the website and saves it into a JSON file. The data includes links (`<a>` tags) and table contents (`<table>` tags) for each section.

## Features

- Scrapes content from 358 sections of the website.
- Extracts all links (`<a>` tags) and table data (`<table>` tags).
- Saves the scraped data into a structured JSON format.
- Uses Selenium WebDriver with Safari for rendering JavaScript-based content.

## Requirements

- Python 3.8+
- Selenium WebDriver
- Safari WebDriver (pre-installed on macOS)

### Install Dependencies

Before running the script, make sure to install the required dependencies:

```bash
pip install -r requirements.txt
