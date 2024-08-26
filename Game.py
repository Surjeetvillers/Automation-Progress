from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get("http://rgs2rgs-operator.pariplaydev.com/")


#Login Page
Username = driver.find_element(By.ID, value="username")
Username.send_keys("PariplayAdmin")
Password = driver.find_element(By.ID, value="password")
Password.send_keys("9!d9Mxt!Z*n8Db")
sleep(2)
signup = driver.find_element(By.ID,value="bLogin")
signup.click()

#Clicking on Search Box
sleep(8)
GameBox = driver.find_element(By.ID, value="gameCode_flexselect").click()

#Navigate to Game
GameBox1 = driver.find_element(By.ID,value="gameCode_flexselect")
GameBox1.send_keys("GoFlamesGo 96 / PP_HTML5_GoFlamesGo96_Mobile")
GameBox1.send_keys(Keys.ENTER)

#Selecting Regulation and Filling details for the Game
sleep(2)
Regulation = driver.find_element(By.ID,value="regulationTypeId")
Regulation.send_keys("DotCom")
Debug_mode = driver.find_element(By.ID,value="isDebugMode")
Debug_mode.click()

#Launching the Game
sleep(3)
Launch = driver.find_element(By.ID,value="play-real-btn")
Launch.click()

#Clicking Okay and entering the Game
sleep(20)
canvas = driver.find_element(By.ID,value="the-canvas")
Canvas_dimension = canvas.size
print(Canvas_dimension)

Canvas_x = Canvas_dimension["width"]
Canvas_y = Canvas_dimension["height"]
center_x = Canvas_x/2
center_y = Canvas_y/2

button_x = (center_x/3)*1
button_y = (center_y/3)*3
print(button_x)
print(button_y)

sleep(8)
action = ActionChains(driver)
action.move_to_element(canvas).move_by_offset(button_x,button_y).click().perform()

#Closing Replay Pop-up
# delay = 5
# try:
#     myElem = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,"popup-button-1")))
#     print ("Page is ready!")
# except TimeoutException:
#     print ("Loading took too much time!")
# # sleep(20)
# # Pop_Up_Close = driver.find_element(By.ID,value="popup-button-1")
# # Pop_Up_Close.click()

# #confirming the close Pop-up
# sleep(15)
# Pop_up_confirm = driver.find_element(By.ID,value="popup-button-1")
# Pop_up_confirm.click()

