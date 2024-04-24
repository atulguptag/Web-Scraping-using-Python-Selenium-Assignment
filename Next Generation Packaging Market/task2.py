import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.common.exceptions import NoSuchElementException

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the window size
driver.maximize_window()

# URLs to scrape
urls = [
    "https://www.dhl.com/global-en/home/insights-and-innovation/thought-leadership/trend-reports/next-generation-advanced-packaging.html#:~:text=With%20a%20current%20market%20size,49.3%20billion%20USD%20by%202032.",
    "https://www.parispackagingweek.com/en/2022/10/31/next-generation-packaging-technologies-enabling-circularity-future-market-insights/",
    "https://isig.ac.cd/alumni/blogs/20158/Next-Generation-Packaging-Market-Key-Trends-Shaping-the-Global-Industry",
    "https://lot.dhl.com/glossary/next-generation-packaging/",
    "https://www.thegpstime.com/next-generation-packaging-market/",
    "https://www.automation.com/en-us/articles/2016-2/next-generation-packaging-market-growth-is-led-by",
    "https://plantesetparfums.wordpress.com/2015/09/13/next-generation-packaging-market-trends/",
    "https://www.whatech.com/og/markets-research/materials-chemicals/786942-next-generation-packaging-market-worth-usd-77-08-million-by-2029-at-a-cagr-of-6-1-says-exactitude-consultancy",
    "https://whattheythink.com/news/102777-next-generation-packaging-market-surpass-us-44-million-2027/",
    "https://faithbudy.com/read-blog/2119_next-generation-packaging-market-by-emerging-trends-business-strategies-technolo.html",
    "https://www.packagingtoday.co.uk/news/newsglobal-next-generation-packaging-market-to-surpass-us-44-million-by-2027-8187695",
    "https://www.supplychainbrain.com/blogs/1-think-tank/post/39400-next-generation-packaging-brings-reliability-and-visibility-to-supply-chains",
    "https://www.globalreporterjournal.com/article/686821428-next-generation-packaging-market-is-projected-to-surpass-us-44-803-billion-by-2029-at-a-cagr-of-6-85",
    "https://www.mckinsey.com/~/media/mckinsey/industries/paper%20and%20forest%20products/our%20insights/winning%20with%20new%20models%20in%20packaging/no-ordinary-disruption-winning-with-new-models-in-packaging-2030-vf.ashx",
    "https://www.brandsgroup.com.au/next-generation-packaging/",
    "https://techbullion.com/rising-demand-from-various-end-use-industries-to-bolster-growth-of-next-generation-packaging-market/",
    "https://go.gale.com/ps/i.do?id=GALE%7CA735150557&sid=sitemap&v=2.1&it=r&p=AONE&sw=w&userGroupName=anon%7E5068a346&aty=open-web-entry",
    "https://www.yolegroup.com/product/monitor/advanced-packaging-market-monitor/",
    "https://nofima.com/projects/nano-functional-packaging/",
    "https://www.taiwannews.com.tw/news/5012843",
    "https://www.ifco.com/5-trends-shaping-sustainable-packaging-in-2024/",
]

# List to store scraped data
scraped_data = []

for url in urls:
    # Open the webpage
    driver.get(url)

    # Extract relevant information
    try:
        title = driver.find_element(By.TAG_NAME, "h1").text
    except NoSuchElementException:
        try:
            title = driver.find_element(By.TAG_NAME, "h2").text
        except NoSuchElementException:
            try:
                title = driver.find_element(By.TAG_NAME, "h3").text
            except NoSuchElementException:
                title = "Title Not Found"

    # Extract text content
    content_elements = driver.find_elements(By.TAG_NAME, "p")
    try:
        content = ''.join([element.text for element in content_elements])
    except NoSuchElementException:
        content = "Content Not Found"

    # Extract image URLs
    image_elements = driver.find_elements(By.TAG_NAME, "img")
    try:
        image_urls = [element.get_attribute("src") for element in image_elements]
    except NoSuchElementException:
        image_urls = ["Image URL Not Found" ]
    
    # Store the scraped data in a structured format
    data = {
        "Title": title,
        "Content": content,
        "Image URLs": image_urls,
    }
    scraped_data.append(data)
    print(json.dumps(scraped_data, indent=4))
    sleep(2)

# Convert data to DataFrame
df = pd.DataFrame(scraped_data)

# Save DataFrame to Excel file
excel_filename = "./task2_data.xlsx"
df.to_excel(excel_filename, index=False)

print("Data scraped from multiple sites and saved to", excel_filename)

# Close the WebDriver
driver.quit()
