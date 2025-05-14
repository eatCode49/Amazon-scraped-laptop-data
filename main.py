from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Firefox()
query = "laptop"
file_num = 0
for i in range(1,18):
    driver.get(f'https://www.amazon.com/s?k=laptop&page={i}&xpid=KfhuPXgybYQRs&crid=8T6T89G4KCZF&qid=1746786024&sprefix=laptop%2Caps%2C452&ref=sr_pg_{i}')
    time.sleep(4)
    elements = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"Item found: {len(elements)}")
    for element in elements:
        with open(f"data/{query}_{file_num}.html" , "w", encoding="utf-8") as file:
            file.write(element.get_attribute("outerHTML"))
            file_num += 1
driver.close()