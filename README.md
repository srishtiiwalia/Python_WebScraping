# Medium Web Scraping using Python

## Overview
This project demonstrates how to perform **web scraping using Python** to extract data from articles published on **Medium**.  
The goal is to collect structured information from web pages and store it for further analysis.

---

## Objective
- Scrape content from Medium articles
- Extract useful information such as:
  - Article title
  - Author name
  - Publication date
  - Reading time / claps (if available)
  - Article text or links
- Understand how websites are structured using HTML

---

## Tools & Libraries Used
- **Python**
- **Requests** – to send HTTP requests
- **BeautifulSoup (bs4)** – to parse HTML content
- **Pandas** – to store and organize scraped data

---

## Approach
1. Send a request to the Medium article URL
2. Parse the HTML content using BeautifulSoup
3. Identify relevant HTML tags and classes
4. Extract required information from the page
5. Store the extracted data in a structured format (DataFrame / CSV)

---

## Output
- Successfully extracted article data from Medium
- Data stored in tabular format for easy analysis
- Can be extended to scrape multiple articles

---

## Challenges Faced
- Medium uses dynamic and frequently changing HTML structures
- Some content may not be accessible due to restrictions
- Required careful inspection of HTML elements

---

## What I Learned
- Basics of web scraping and HTML structure
- How to use BeautifulSoup for parsing web pages
- Handling missing or inconsistent data
- Ethical considerations in web scraping

---

## Limitations
- Scraping depends on Medium’s page structure
- JavaScript-rendered content may not be fully accessible using requests
- Not suitable for large-scale scraping

---

## Future Improvements
- Automate scraping for multiple Medium articles
- Use Selenium for dynamic content
- Add error handling and logging
- Perform text analysis on scraped articles

---

## Disclaimer
This project is for **educational purposes only**.  
Web scraping should always comply with a website’s **terms of service and robots.txt** rules.
