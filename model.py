import re
import sys

class SnackVendingMachine:
    def __init__(self):
        self.products = {
            "Снікерс": {"price": 22, "quantity": 3},
            "Чіпси": {"price": 40, "quantity": 5},
            "Твікс": {"price": 20, "quantity": 2},
            "Скітлс": {"price": 25, "quantity": 6},
            "Шоколадка": {"price": 30, "quantity": 4},
            "Крекери": {"price": 27, "quantity": 3},
            "Баунті": {"price": 19, "quantity": 5},
            "Мармеладки": {"price": 36, "quantity": 1},
            "Крендельки": {"price": 23, "quantity": 7},
            "Арахіс": {"price": 16, "quantity": 4},
            "Марс": {"price": 25, "quantity": 2},
            "Зефірки": {"price": 29, "quantity": 5}
        }
        self.balance = 0
        self.sales_log = []

    def display_products(self):
        print("Доступні товари та їх ціни:")
        for product, info in self.products.items():
            print(f"{product} - {info['price']} грн (Кількість: {info['quantity']})")

    def select_products(self):
        while True:
            selected_products_input = input("Виберіть товари (введіть 0 для виходу): ")
            if selected_products_input == '0':
                sys.exit("Дякуємо за використання автомата зі снеками!")
            selected_products = [product.capitalize() for product in re.split(',|\s', selected_products_input)]
            if all(product in self.products and self.products[product]["quantity"] > 0 for product in selected_products):
                return selected_products
            else:
                print("Один або декілька товарів відсутні або закінчилися. Спробуйте ще раз.")

    def process_payment(self):
        while True:
            try:
                payment_amount = float(input("Введіть суму оплати (або введіть 0 для виходу): "))
                if payment_amount == 0:
                    sys.exit("Дякуємо за використання автомата зі снеками!")
                elif payment_amount >= 0:
                    return payment_amount
                else:
                    print("Будь ласка, введіть коректну суму.")
            except ValueError:
                print("Будь ласка, введіть числове значення.")

    def complete_transaction(self, selected_products, payment_amount):
        total_price = sum(self.products[product]["price"] for product in selected_products)
        if payment_amount >= total_price:
            change = payment_amount - total_price
            self.balance += total_price
            for product in selected_products:
                self.products[product]["quantity"] -= 1
                self.sales_log.append({"product": product, "price": self.products[product]["price"]})
            print(f"Ваші товари {', '.join(selected_products)} готові! Здача: {change} грн")
        else:
            print("Недостатньо коштів для оплати товарів. Транзакція скасована.")

    def run(self):
        while True:
            self.display_products()
            selected_products = self.select_products()
            payment_amount = self.process_payment()
            self.complete_transaction(selected_products, payment_amount)


if __name__ == "__main__":
    vending_machine = SnackVendingMachine()
    vending_machine.run()
