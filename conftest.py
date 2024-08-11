from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def chrome_driver():
    global driver
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("detach", True)
    # chromepath = Service("C:/ChromeDriver/chromedriver.exe")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get("https://qa-tipalti-assignment.tipalti-pg.com/index.html")
    yield driver
    driver.close()