import os

import string
import math
import time

from selene import be, have, command
from selene.support.shared import browser



def test_fill_form():
    # Открываем страницу demoqa
    browser.open("/automation-practice-form")

    # Заполняем поля формы
    browser.element("#firstName").should(be.blank).type("Test")
    browser.element("#lastName").should(be.blank).type("User")
    browser.element("#userEmail").should(be.blank).type("test_example@gmail.com")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").should(be.blank).type("9999999999")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="2000"]').click()
    browser.element('.react-datepicker__month-select>[value="1"]').click()
    browser.element('.react-datepicker__day--022').click()
    browser.element("#subjectsInput").type("Computer Science").press_enter()

    # Удаляем рекламу на странице
    ads = browser.all('[id^=google_ads_][id$=container__]').should(have.size_less_than_or_equal(3)).perform(command.js.remove)

    # Кликаем по всем чек-боксам в форме
    checkboxes = browser.elements(".custom-checkbox label")
    for checkbox in checkboxes:
        checkbox.click()
        checkbox.click()
        checkbox.click()

    # Загружаем картинку в форме
    browser.element('#uploadPicture').set_value(r"C:\Users\maxim\OneDrive\Рабочий стол\task\photo.jpeg")
    # Заполянем оставшиеся поля
    time.sleep(5)
    browser.element("#currentAddress").should(be.blank).type("It's my address")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element('#submit').press_enter()

    # Проверяем регистрацию пользователя
    browser.all(".table-responsive td:nth-child(2)").should(have.texts(
        "Test User",
        "test_example@gmail.com",
        "Male",
        "9999999999",
        "22 February,2000",
        "Computer Science",
        "Sports, Reading, Music",
        "photo.jpeg",
        "It's my address",
        "NCR Delhi"
    ))
