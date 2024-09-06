from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps ["platformName"] = "Android"
# desired_caps ["udid"] = "emulator-5554"
desired_caps ["udid"] = "de372c98"
desired_caps ["deviceName"] = "device"
desired_caps ["appPackage"] = "org.owline.kasirpintarpro"
desired_caps ["appActivity"] = "org.owline.kasirpintarpro.SplashScreen"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

