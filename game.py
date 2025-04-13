from telebot import TeleBot, types, apihelper
import keyboards as kb
from models import User
from service import GameService


class CallbackHandler:
    MAIN_TEXT = (
        "Ваши коины: {coins}\n\n"
        "Текущий доход коинов в 10 секунд: {level}\n"
        "Пассивный доход от друзей: {invited}\n\n"
        "[Стоимость следующего уровня: {price}]"
    )

    def __init__(self, bot: TeleBot):
        """Создание обработчика колбеков для основного функционала игры.

        Args:
            bot (TeleBot): объект бота
        """
        # TODO: описать функцию
        ...

    def handle_main_menu(self, call: types.CallbackQuery):
        """Обработка главного игрового меню."""

        # TODO: описать функцию
        ...

    def handle_update_info(self, call: types.CallbackQuery):
        """Обработка кнопки "обновить", которая редактирует главное меню, актуализируя данные."""

        # TODO: описать функцию
        ...

    def handle_friends_list(self, call: types.CallbackQuery):
        """Отображение списка друзей и пригласительного года при нажатии на кнопку "список друзей"."""

        # TODO: описать функцию
        ...

    def handle_back_to_main(self, call: types.CallbackQuery):
        """Возвращает пользователя в главное меню при нажатии кнопки "назад" в списке друзей."""

        # TODO: описать функцию
        ...

    def handle_upgrade_level(self, call: types.CallbackQuery):
        """Обработка улучшения уровня на кпноку "повысить уровень"."""

        # TODO: описать функцию
        ...
