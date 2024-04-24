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
    "https://www.genengnews.com/topics/artificial-intelligence/laboratory-automation-reaches-every-stage-of-drug-development/",
    "https://www.azolifesciences.com/article/How-Important-is-Lab-Automation-to-Drug-Discovery.aspx",
    "https://www.ddw-online.com/advances-in-laboratory-automation-for-drug-discovery-649-200604/",
    "https://frontlinegenomics.com/automation-in-drug-discovery/",
    "https://www.pharmaadvancement.com/pharma-news/lab-automation-market-what-is-in-the-store-now-future/",
    "https://www.ddw-online.com/media/32/06.spr.advances-in-laboratory-automation-for-drug-discovery.pdf",
    "https://newsstand.joomag.com/en/research-report-global-lab-automation-in-drug-discovery-market/0993469001489486111",
    "https://lifesciences.danaher.com/us/en/library/lab-automation-drug-discovery.html",
    "https://www.biocompare.com/Editorial-Articles/612020-Automated-Drug-Discovery-2-0/",
    "https://kaloramainformation.com/product/lab-automation-markets-2nd-edition-systems-key-companies-forecasts-and-trends/",
    "https://healthcare-in-europe.com/en/news/21st-century-lab-automation.html",
    "https://pharmaceuticalmanufacturer.media/pharmaceutical-industry-insights/how-lab-automation-is-helping-drug-research/",
    "https://www.labiotech.eu/interview/arctoris-automation-drug-discovery/",
    "https://www.news-medical.net/whitepaper/20230206/Automation-as-a-drug-discovery-accelerator-in-the-pharmaceutical-industry.aspx",
    "https://www.htworld.co.uk/news/research-news/harnessing-automation-will-unlock-the-full-potential-of-drug-discovery-labs-digi23/",
    "https://www.biospace.com/article/biotech-investing-big-on-lab-automation-study/",
    "https://pittcon.org/analysis-automation-technologies-pharmaceutical-research/",
    "https://www.pharma-iq.com/pre-clinical-discovery-and-development/whitepapers/how-to-automate-the-data-lifecycle-to-make-lab-work-more-efficient-2",
    "https://www.biocompare.com/Editorial-Articles/612020-Automated-Drug-Discovery-2-0/#:~:text=Automation%20in%20drug%20discovery%20and,benefits%20offered%20by%20laboratory%20automation.",
    "https://www.ddw-online.com/how-end-to-end-laboratory-automation-and-ai-are-accelerating-drug-discovery-17751-202207/",
    "https://www.nature.com/articles/nrd.2017.232",
    "https://automata.tech/blog/investigating-laboratory-automation-in-early-drug-discovery/",
    "https://paa-automation.com/application/drug-discovery/",
    "https://paa-automation.com/applications/",
    "https://www.technologynetworks.com/drug-discovery/articles/transforming-drug-discovery-using-ai-and-automation-338301",
    "https://www.mckinsey.com/industries/life-sciences/our-insights/from-bench-to-bedside-transforming-r-and-d-labs-through-automation",
    "https://www.astrazeneca.com/r-d/our-technologies/ilab.html",
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
        image_urls = [element.get_attribute("src")
                      for element in image_elements]
    except NoSuchElementException:
        image_urls = ["Image URL Not Found"]

    # Store the scraped data in a structured format
    data = {
        "Title": title,
        "Content": content,
        "Image URLs": image_urls,
    }
    scraped_data.append(data)
    sleep(3)

# Convert data to DataFrame
df = pd.DataFrame(scraped_data)

# Save DataFrame to Excel file
excel_filename = "./task3_data.xlsx"
df.to_excel(excel_filename, index=False)

print("Data scraped from multiple sites and saved to", excel_filename)

# Close the WebDriver
driver.quit()
