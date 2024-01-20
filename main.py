from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_settings)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[9]")
def click_cookie():
    cookie_button.click()

five_min = time.time() + 60*5   # 5 minutes from now
timeout = time.time() + 5
while True:
    # test = 0
    # if test == 5 or time.time() > five_min:
    #     break
    # test = test - 1
    click_cookie()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_in_shop = driver.find_elements(By.CSS_SELECTOR, "#store div")
        item_name = [item.get_attribute("id") for item in items_in_shop]
        items_prices = [item.text.split("-") for item in items]
        new_price_list = []
        for n in range(len(items_prices)-1):
            new_price_list.append(items_prices[n][1].strip().replace(",", ""))
        new_name_list = []
        for n in item_name:
            if len(n) == 0:
                item_name.remove(n)

        money = driver.find_element(By.ID, "money").text.replace(",", "")

        affordable_items = []
        for cost in new_price_list:
            if int(money) > int(cost):
                affordable_items.append(int(cost))

        most_expensive = max(affordable_items)
        index = affordable_items.index(most_expensive)
        driver.find_element(By.ID, f"{item_name[index]}").click()

        timeout = time.time() + 5









