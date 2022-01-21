from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from mainGUI import bookingID, surname, selectedLocations
import csv
from datetime import datetime

locationValues = {
    'Albury': '17',
    'Armidale': '18',
    'Auburn': '112',
    'Ballina': '19',
    'Bankstown': '20',
    'Batemans Bay': '21',
    'Bathurst': '22',
    'Bega': '23',
    'Blacktown': '26',
    'Blue Mountains': '27',
    'Bondi Junction': '28',
    'Botany': '29',
    'Broken Hill': '30',
    'Brookvale': '77',
    'Burwood': '31',
    'Casino': '34',
    'Castle Hill': '35',
    'Cessnock': '36',
    'Chatswood': '37',
    'Coffs Harbour': '39',
    'Cooma': '40',
    'Cootamundra': '42',
    'Corrimal': '43',
    'Cowra': '44',
    'Deniliquin': '45',
    'Dubbo': '46',
    'Eden': '47',
    'Engadine': '381',
    'Erina': '49',
    'Finley': '51',
    'Forbes': '53',
    'Glen Innes': '56',
    'Gosford': '57',
    'Goulburn': '58',
    'Grafton': '59',
    'Griffith': '60',
    'Gunnedah': '61',
    'Hay': '62',
    'Haymarket': '161',
    'Hornsby': '63',
    'Hurstville': '64',
    'Inverell': '66',
    'Kempsey': '67',
    'Kiama': '68',
    'Leeton': '69',
    'Lightning Ridge': '71',
    'Lismore': '72',
    'Lithgow': '73',
    'Liverpool': '74',
    'Macarthur': '32',
    'Maclean': '75',
    'Maitland': '76',
    'Marrickville': '79',
    'Miranda': '81',
    'Mittagong': '82',
    'Moree': '83',
    'Moruya': '84',
    'Mount Druitt': '85',
    'Mudgee': '86',
    'Murwillumbah': '87',
    'Muswellbrook': '88',
    'Nambucca Heads': '89',
    'Narooma': '91',
    'Narrabri': '92',
    'Narrandera': '93',
    'Nelson Bay': '94',
    'Newcastle': '95',
    'Nowra': '98',
    'Nyngan': '99',
    'Orange': '100',
    'Parkes': '102',
    'Parramatta': '103',
    'Penrith': '104',
    'Port Macquarie': '105',
    'Queanbeyan': '106',
    'Raymond Terrace': '107',
    'Revesby': '382',
    'Richmond': '108',
    'Rockdale': '109',
    'Roselands': '421',
    'Ryde': '96',
    'Silverwater': '241',
    'Singleton': '113',
    'Springwood': '114',
    'Tamworth': '116',
    'Taree': '117',
    'Tenterfield': '118',
    'Toronto': '281',
    'Toukley': '122',
    'Tuggerah': '140',
    'Tumut': '123',
    'Tuncurry': '54',
    'Tweed Heads': '124',
    'Ulladulla': '125',
    'Wagga Wagga': '127',
    'Walgett': '128',
    'Wallsend': '129',
    'Warners Bay': '130',
    'Warrawong': '126',
    'Warriewood': '131',
    'Wauchope': '132',
    'Wellington': '133',
    'Wentworth': '134',
    'West Wyalong': '135',
    'Wetherill Park': '136',
    'Wollongong': '137',
    'Wynyard': '139',
    'Yass': '141',
    'Young': 142
}

allAvailabilities = []

def LoadWebpage():
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    global driver, wait
    webpage = r"http://www.myrta.com/viewtest"
    driver = webdriver.Chrome(options = chromeOptions)
    wait = WebDriverWait(driver, 10)
    driver.get(webpage)
    # html = driver.page_source
    print("Loaded")


def Login(loginID, surname):
    idText = driver.find_element(By.ID, "widget_input_bookingId")
    idText.send_keys(loginID)
    surnameText = driver.find_element(By.ID, "widget_input_familyName")
    surnameText.send_keys(surname)

    submitButtons = driver.find_elements(By.CLASS_NAME, "dijitButtonNode")
    submitButtons[0].submit()


def PressChangeLocation():
    submitButtons2 = driver.find_elements(By.CLASS_NAME, "dijitButtonNode")
    # print(submitButtons2)
    wait.until(EC.element_to_be_clickable(submitButtons2[1])).click()


def ClickInDropDown(value):
    submitButtons3 = driver.find_elements(By.CLASS_NAME, "dijitCheckBoxInput")
    # print(submitButtons3)
    wait.until(EC.element_to_be_clickable(submitButtons3[1])).click()
    locationDropDown = Select(wait.until(EC.element_to_be_clickable(driver.find_element(By.NAME, "locationSelect"))))
    # print(locationDropDown.get_attribute("outerHTML"))
    # wait.until(EC.element_to_be_clickable(locationDropDown)).select_by_value('17')
    # wait.until(EC.element_to_be_clickable(locationDropDown)).send_keys(Keys.ARROW_DOWN)
    locationDropDown.select_by_value(value)
    buttonClick = driver.find_element(By.CLASS_NAME, 'rms_nextButton').find_element(By.CLASS_NAME,
                                                                                    'dijitButtonNode').click()


def FindAvailabilities():
    earliestAvailableButton = driver.find_element(By.ID, 'getEarliestTime')
    earliestAvailableButton.click()
    # available = driver.find_elements(By.CLASS_NAME, "available")
    # print(len(available))
    # parentClass = available[0].find_element(By.XPATH, '..').get_attribute('class')
    # print(parentClass)
    # date = driver.find_element(By.CLASS_NAME, parentClass).find_element(By.CLASS_NAME, 'd').get_attribute("innerHTML")
    availableDates = driver.find_elements(By.CLASS_NAME, "available")
    currentLocation = driver.find_element(By.ID, 'rms_testLocationName').find_element(By.TAG_NAME,
                                                                                      'strong').get_attribute(
        "innerHTML")
    if (len(availableDates) >= 1):
        for availableDate in availableDates:
            parentClass = availableDate.find_element(By.XPATH, '..').get_attribute('class')
            date = driver.find_element(By.CLASS_NAME, parentClass).find_element(By.CLASS_NAME, 'd').get_attribute("innerHTML")
            timeAvailable = availableDate.get_attribute('innerHTML')
            print(f"{currentLocation} - {date} on {timeAvailable}")
            allAvailabilities.append([currentLocation, date, timeAvailable])
    else:
        print(f"{currentLocation} - None available")
        allAvailabilities.append([currentLocation, "0/0", "00:00"])


def GoBackButton():
    anotherLocationButton = driver.find_element(By.ID, 'anotherLocationLink')
    anotherLocationButton.click()


def FindAllAvailabilities():
    #print(selectedLocations)
    for selectedLocation in selectedLocations:
        ClickInDropDown(locationValues[selectedLocation])

        FindAvailabilities()
        print('\n\n\n\n')
        GoBackButton()


def ExportAvailabilities():
    allAvailabilities.insert(0, ["Location", "Date", "Time"])

    with open('Availabilities.csv', mode='w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerows(allAvailabilities)


LoadWebpage()

Login(bookingID, surname)

PressChangeLocation()

FindAllAvailabilities()

ExportAvailabilities()

print("Done All Checks")
driver.close()
