# Тест для рецензирования
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket(browser, request):
    browser.get(link)
    browser.implicitly_wait(4)
    add_to_basket = browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket")
    assert add_to_basket.text in ["Ajouter au panier", "Добавить в корзину", "Add to basket", "Añadir al carrito"], \
        "Текст кнопки не соответсвует языкам fr, ru, en, es"

    time.sleep(2)
