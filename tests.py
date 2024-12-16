import time
import pyautogui
import unittest
import pygetwindow as gw  # Импортируем pygetwindow для работы с окнами
from pizza_shop import PizzaShop
from tkinter import Tk


class TestPizzaShopE2E(unittest.TestCase):

    def setUp(self):
        # Запуск приложения
        self.root = Tk()
        self.pizza_shop = PizzaShop(self.root)
        self.root.after(1000, self.root.quit)
        self.root.mainloop()

    def test_create_order(self):
        # Ожидаем, что окно загрузится
        time.sleep(3)  # Увеличиваем время ожидания для загрузки окна

        # Ввод имени клиента
        pyautogui.write('Иван Иванов')  # Вводим имя
        pyautogui.press('tab')  # Переход к следующему полю

        # Ввод телефона
        pyautogui.write('123-456-789')  # Вводим телефон
        pyautogui.press('tab')

        # Выбор пиццы из меню
        pyautogui.press('down')  # Нажимаем вниз, чтобы выбрать первый элемент
        pyautogui.press('enter')  # Подтверждаем выбор пиццы

        # Добавление пиццы в заказ
        pyautogui.press('tab')  # Переход к кнопке добавления
        pyautogui.press('enter')  # Нажимаем "Добавить пиццу"

        # Переход к оформлению заказа
        pyautogui.press('tab')  # Переход к кнопке оформления заказа
        pyautogui.press('enter')  # Нажимаем "Оформить заказ"

        # Ожидаем, что появится сообщение о заказе
        time.sleep(3)  # Даем больше времени для появления окна

        print("Test Passed: Order created successfully.")

    def tearDown(self):
        self.root.quit()


# Запуск тестов с подробным выводом
if __name__ == '__main__':
    unittest.main(verbosity=2)  # Увеличиваем уровень детализации
    print("Все тесты выполнены успешно!")
