from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the window size
driver.maximize_window()

# URLs to scrape
urls = [
    "https://www.monolithai.com/blog/4-ways-ai-is-changing-the-packaging-industry",
    "https://mitsubishisolutions.com/the-role-of-artificial-intelligence-in-smart-packaging-lines/",
    "https://thedatascientist.com/how-artificial-intelligence-is-revolutionizing-the-packaging-industry/",
    "https://packagingeurope.com/comment/ai-and-the-future-of-packaging/9665.article",
    "https://www.sttark.com/blog/ai-powered-custom-packaging-a-creative-revolution",
    "https://dragonflyai.co/resources/blog/how-ai-and-iot-are-transforming-packaging-design",
    "https://sustainability-in-packaging.com/sustainability-in-packaging-europe/ai-and-sustainable-packaging",
    "https://becominghuman.ai/the-role-of-artificial-intelligence-in-the-packaging-industry-c08b58b2f475",
    "https://www.industrialpackaging.com/blog/ai-packaging-is-artificial-intelligence-the-future-of-packaging-design",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10418964/",
    "https://www.designerpeople.com/blog/ai-packaging-design/",
    "https://www.springfieldsolutions.co.uk/insights/blog/ai-packaging",
    "https://interbrandspackaging.com/en/2023/05/26/artificial-intelligence-in-sustainable-packaging/",
    "https://www.whatpackaging.co.in/features/ai-in-packaging-industry-to-hit-usd-537528-mn-by-2032-57671",
    "https://www.packworld.com/trends/operational-excellence/article/22869386/ai-in-packaging-to-reach-6-billion-by-the-end-of-2033",
    "https://www.packaginginsights.com/news/ai-in-packaging-how-artificial-intelligence-is-driving-the-packaging-industry-forward.html",
    "https://www.packagingdigest.com/packaging-design/how-to-use-and-not-use-ai-for-package-design",
    "https://www.monolithai.com/blog/packaging-sustainability-eu-and-ai",
    "https://packagingguruji.com/ai-for-packaging-design/",
    "https://www.arka.com/pages/ai-packaging-design",
    "https://chaseandassoc.com/how-artificial-intelligence-ai-in-the-packaging-industry-is-making-advancements/",
    "https://pollthepeople.app/ai-for-packaging/",
    "https://robopacusa.com/how-ai-is-revolutionizing-the-packaging-industry/",
    "https://www.pickfu.com/blog/ai-packaging-design/",
    "https://www.globaltrademag.com/ai-in-the-packaging-market-to-hit-5375-28-mn-by-2032/"
]

# List to store scraped data
scraped_data = []

for url in urls:
    # Open the webpage
    driver.get(url)

    # Extract relevant information
    title = driver.find_element(By.TAG_NAME, "h1").text

    # Extract text content
    content_elements = driver.find_elements(By.TAG_NAME, "p")
    content = ''.join([element.text for element in content_elements])

    # Extract image URLs
    image_elements = driver.find_elements(By.TAG_NAME, "img")
    image_urls = [element.get_attribute("src") for element in image_elements]

    # Store the scraped data in a structured format
    data = {
        "Title": title,
        "Content": content,
        "Image URLs": image_urls,
    }
    scraped_data.append(data)
    sleep(2)

# Convert data to DataFrame
df = pd.DataFrame(scraped_data)

# Save DataFrame to Excel file
excel_filename = "./task_data.xlsx"
df.to_excel(excel_filename, index=False)

print("Data scraped from multiple sites and saved to", excel_filename)

# Close the WebDriver
driver.quit()
