from config import dp, executor
from handlers import add_item, commands, orders, products
from db import db_main
import logging

commands.register_commands(dp)
add_item.register_fsm_add(dp)
products.register_handlers_send_products(dp)
orders.register_handlers_fsm_order(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=db_main.sql_create)
#
