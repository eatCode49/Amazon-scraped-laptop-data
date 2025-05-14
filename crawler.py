from bs4 import BeautifulSoup
import pandas as pd

df_dict = {"Title": [1, 2], "Price": [3, 4], "Links": [4, 5]}
for i in range(2, 493):
    with open(f"data/laptop_{i}.html", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    name = soup.find("h2").text  # We got title here
    try:
        price = soup.find(class_="a-offscreen") # We got price here
        if price is None:
            price = BeautifulSoup("Null", "html.parser")
    except Exception as e:
        print(e)

    a_link = soup.find("a", href=True)  # Ensure the <a> tag has an href attribute
    link = a_link["href"]

    # If the link starts with "/", prepend the base URL (example: "https://www.amazon.com")
    if link.startswith("/"):
        link = "https://www.amazon.com" + link

    df_dict["Links"].append(link)
    df_dict['Title'].append(name)
    df_dict['Price'].append(price.text)
    df = pd.DataFrame(df_dict)
    df.to_csv("Laptop Data.csv", index=True)
print("data frame created succesfully")