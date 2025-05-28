from selenium import webdriver
from selenium.webdriver.common.by import By

def test_baidu_search():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("软件测试")
    driver.find_element(By.ID, "su").click()
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    test_baidu_search()
