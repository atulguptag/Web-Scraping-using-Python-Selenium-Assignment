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
    "https://www.designtechproducts.com/articles/3d-printing-packaging#:~:text=3D%20printing%2C%20with%20its%20inherent,environment%20friendly%20material%20in%20packaging.&text=3D%20packaging%20has%20opened%20up,important%20constraints%20is%20the%20cost.",
    "https://www.stratasys.co.in/industries-and-applications/3d-printing-applications/packaging/",
    "https://www.alexanderdanielsglobal.com/blog/3d-printing-in-the-packaging-industry/",
    "https://www.3dnatives.com/en/3d-printing-sustainable-packaging-corporate-goals-consumer-demands-211220214/",
    "https://zortrax.com/applications/packaging-design/",
    "https://www.prescouter.com/2017/02/3d-printing-disrupting-packaging/",
    "https://www.weareamnet.com/blog/impact-3d-printing-packaging-supply-chain/",
    "https://replique.io/2023/08/24/6-reasons-why-the-packaging-industry-should-shift-to-3d-printing/",
    "https://amfg.ai/2020/08/17/how-3d-printing-transforms-the-food-and-beverage-industry/",
    "https://www.packagingconnections.com/blog-entry/3d-printing-packaging.htm-0",
    "https://www.divbyz.com/blog/3d-printed-packaging-solutions",
    "https://www.packcon.org/index.php/en/articles/118-2022/328-3d-printing-in-the-packaging-industry",
    "https://nexa3d.com/industries/packaging/",
    "https://lekac.com/production/3-ways-3d-printing-is-disrupting-the-packaging-industry",
    "https://www.javelin-tech.com/3d/process/packaging-design/",
    "https://www.cossma.com/production/article/3d-printed-packaging-36939.html",
    "https://textilevaluechain.in/news-insights/transforming-consumer-experience-3d-printed-packaging-industry-is-the-new-big-thing-in-the-market-and-will-it-cross-us-3-billion-by-2033",
    "https://www.objective3d.com.au/resource/blog/developing-sustainable-packaging-solutions-with-3d-printing-technology/",
    "https://medium.com/@sindiajohn0246/3d-printed-packaging-market-key-drivers-and-challenges-2023-2033-ba372b4d151e",
    "https://ieeexplore.ieee.org/document/7887895",
    "https://quickparts.com/3d-printing-for-the-packaging-industry/",
    "https://www.packagingstrategies.com/articles/104099-podcast-the-role-of-3d-printing-in-sustainable-packaging",
    "https://www.health-care-it.com/company/910976/news/3408203/shaping-the-future-3d-printed-packaging-market-set-to-double-to-us-2-560-million-by-2033-with-a-7-8-cagr",
    "https://ijaers.com/detail/applications-and-prospects-of-3d-printing-in-the-packaging-industry/",
    "https://www.packagingdevelopments.com/blog/3d-printing-within-the-packaging-process-a-hindrance-or-a-help/",
    "https://www.packagingdigest.com/digital-printing/3d-printing-s-future-in-packaging-is-promising",
    "https://theuniquegroup.com/impact-3d-printing-packing-industry/",
    "https://www.liquidpackagingsolution.com/news/3d-printing-the-future-of-packaging",
    "https://www.jabil.com/blog/3d-printing-trends-show-positive-outlook.html",
    "https://replique.io/2023/08/24/6-reasons-why-the-packaging-industry-should-shift-to-3d-printing/",
    "https://www.startus-insights.com/innovators-guide/top-10-packaging-industry-trends-innovations-in-2021/",
    "https://www.printweek.in/features/various-packaging-trends-for-industry-advancements-57740",
    "https://pakfactory.com/blog/future-of-packaging-technology-design-in-the-next-10-years-and-beyond/",
    "https://www.mdpi.com/2673-687X/3/1/6",
    "https://www.printweek.in/news/deconstructing-growth-in-3dprinted-packaging-market-42523",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9818434/",
    "https://www.beautypackaging.com/issues/2020-03-01/view_features/digital-3d-printing-inspire-new-designs/",
    "https://www.researchgate.net/publication/368978658_Analysis_of_the_Application_and_Exploration_of_3D_Printing_Technology_Used_in_the_Future_Takeaway_Packaging",
    "https://www.thecustomboxes.com/blog/3d-printing-technology-and-packaging-industry/",
    "https://siliconsemiconductor.net/article/118244/Breakthroughs_and_opportunities_in_3D_packaging",
    "https://www.food.gov.uk/research/introduction-3d-printing-technologies-in-the-food-system-for-food-production-and-packaging"
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
        content = ["Content Not Found"]

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
    # sleep(3)

# Convert data to DataFrame
df = pd.DataFrame(scraped_data)

# Save DataFrame to Excel file
excel_filename = "./task4_data.xlsx"
df.to_excel(excel_filename, index=False)

print("Data scraped from multiple sites and saved to", excel_filename)

# Close the WebDriver
driver.quit()
