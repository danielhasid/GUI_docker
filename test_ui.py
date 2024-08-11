import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_main_page(chrome_driver):
    temp_list = ['Kika', 'Lychee', 'Kimba']

    menu_name_list = []
    driver = chrome_driver
    action = ActionChains(driver)


    driver.find_element(By.XPATH,"//li/a[@href = '#menu']").click()
    time.sleep(5)
    menu_list = driver.find_elements(By.XPATH,"//div[@class = 'inner']/ul/li/a")

    menu_name_list =[menu.text for menu in menu_list[1::]]
    print(menu_name_list)
    assert temp_list == menu_name_list


    driver.find_element(By.XPATH,f"//div[@class = 'inner']/ul/li/a[text()='Kika']").click()
    driver.find_element(By.XPATH,'//input[@id="name"]').send_keys('Kika')
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys(f"Kika@tipalti.com")
    driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys(f"Hello My name is Kika")
    # driver.find_element(By.XPATH,"//input[@type='submit']").click()
    driver.find_element(By.XPATH, "//li/a[@href = '#menu']").click()
