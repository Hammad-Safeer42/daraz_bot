# Imports stealth
from selenium_stealth import stealth
# Python's built in time module
import time
# Python's built-in random module
import random
# imports webdriver
from selenium import webdriver
# WebDriverWait waits for the element to be present on the page and acts upon it
from selenium.webdriver.support.wait import WebDriverWait
# Select is used for elements in the dropdown manu
from selenium.webdriver.support.ui import Select
# NoSuchElementException occurs when the element is not present to be selected
from selenium.common.exceptions import NoSuchElementException
# Defined conditions to use with WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Selecting elements using By
from selenium.webdriver.common.by import By
# Keys is used to mimick key presses within Selenium
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()

opt.add_argument('--user-data-dir=/path/to/your/custom/profile')

opt.add_argument('--disable-blink-features=PasswordImport')
opt.add_argument('--disable-blink-features=PasswordGeneration')




# Configurations for selenium driver
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--profile-directory=Person 4")
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("disable-popup-blocking")
driver = webdriver.Chrome(options=opt)
# Calls and configure Selenium stealth using OpenGL
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
#REPLACE LINK WITH YOUR DESIRED PRODUCT LINK FROM DARAZ
driver.get("https://www.daraz.pk/products/air-pro-tws-earbuds-wireless-buds-airpods_pro-i12-noise-cancellation-woofer-bluetooth-headset-i362285107-s2151997301.html?spm=a2a0e.home.flashSale.3.35e34076EuiucS")
foundButton = False


# Wait for the "Add to Cart" button to be clickable
addToCartButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pdp-button-text"))
)
addToCartButton.click()

time.sleep(2)

iframe_selector = 'iframe.login-iframe[src="//member.daraz.pk/user/pure-login"]'
iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
)


# Switch to the iframe
driver.switch_to.frame(iframe_element)



# Now you can interact with elements inside the iframe
time.sleep(2)
# Wait for the email input field to be clickable and visible
email_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Please enter your Phone Number or Email"]'))
)
# Enter the email address
email_address = 'xyz@gmail.com'   #put your daraz mail
# Types in each character at a random interval, makes input more human-like
for i in email_address:
    email_input.send_keys(i)
    time.sleep(random.uniform(0, 0.05))


 #passworrd imput
pass_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Please enter your password"]'))
)
# Enter the email address
password = 'password'  #replace with actual daraz password
# Types in each character at a random interval, makes input more human-like
for i in password:
    pass_input.send_keys(i)
    time.sleep(random.uniform(0, 0.05))


time.sleep(1)

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'next-btn.next-btn-primary.next-btn-large'))
)

# Click the button
next_button.click()

# When you're done interacting with elements inside the iframe, switch back to the main content
driver.switch_to.default_content()

try:
    addToCartButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pdp-button-text"))
    )
    addToCartButton.click()
except:
    print("already in cart")

time.sleep(2)

# Wait for the cart element to be clickable
cart_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'cart-icon'))
)

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView(true);", cart_element)

# Click on the cart element
cart_element.click()

print("cart open")


# Wait for the checkbox element to be present
print("check boxx selected")



button_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'next-btn.next-btn-primary.next-btn-large.checkout-order-total-button.automation-checkout-order-total-button-button'))
)

# Click on the button
button_element.click()
print("heee")
time.sleep(1)


button_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'next-btn.next-btn-normal.next-btn-medium.place-order-btn'))
)


# Scroll the button into view
driver.execute_script("arguments[0].scrollIntoView(true);", button_element)

# Click on the button
button_element.click()
print("proceedd")


time.sleep(1)
payment_method_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'automation-payment-method-item-103'))
)

# Click the button
payment_method_button.click()

time.sleep(2)




card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'creditCard'))
)
# Enter the email address
card_num = '1222 1233 1231 1223'
card_name = 'ENTER NAME'
expiry = '0625'
cvv = '123'
phoneNumber = '03123456789'

# Types in each character at a random interval, makes input more human-like
for i in card_num:
    card.send_keys(i)
    time.sleep(random.uniform(0, 0.05))

time.sleep(1)

card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'cardName'))
)
# Enter the email address

# Types in each character at a random interval, makes input more human-like
for i in card_name:
    card.send_keys(i)
    time.sleep(random.uniform(0, 0.05))


card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'expiryDate'))
)
# Enter the email address

# Types in each character at a random interval, makes input more human-like
for i in expiry:
    card.send_keys(i)
    time.sleep(random.uniform(0, 0.05))



time.sleep(3)
card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'cvv'))
)
# Enter the email address

# Types in each character at a random interval, makes input more human-like
for i in cvv:
    card.send_keys(i)
    time.sleep(random.uniform(0, 0.05))


phon_num = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'phoneNo'))
)
# Enter the email address

# Types in each character at a random interval, makes input more human-like
for i in phoneNumber:
    phon_num.send_keys(i)
    time.sleep(random.uniform(0, 0.05))


time.sleep(1)
button_class_name = "next-btn.next-btn-primary.next-btn-large.automation-btn-place-order.btn-place-order"

# Wait for the button to be present in the DOM
button_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, button_class_name))
)

# Scroll the button into view
driver.execute_script("arguments[0].scrollIntoView(true);", button_element)

# Wait for the button to be clickable
button_element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, button_class_name))
)

# Click on the button
button_element.click()


time.sleep(5)

# waits for confirmation (60 seconds)
time.sleep(60)
# Quits driver
driver.quit()
