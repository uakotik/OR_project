import re
import sys

class SnackVendingMachine:
    def __init__(self):
        self.total_snacks = 240
        self.products = {
            "Снікерс": {"price": 22, "quantity": 20, "sales": 0},
            "Чіпси": {"price": 40, "quantity": 20, "sales": 0},
            "Твікс": {"price": 20, "quantity": 20, "sales": 0},
            "Скітлс": {"price": 25, "quantity": 20, "sales": 0},
            "Шоколадка": {"price": 30, "quantity": 20, "sales": 0},
            "Крекери": {"price": 27, "quantity": 20, "sales": 0},
            "Баунті": {"price": 19, "quantity": 20, "sales": 0},
            "Мармеладки": {"price": 36, "quantity": 20, "sales": 0},
            "Крендельки": {"price": 23, "quantity": 20, "sales": 0},
            "Арахіс": {"price": 16, "quantity": 20, "sales": 0},
            "Марс": {"price": 25, "quantity": 20, "sales": 0},
            "Зефірки": {"price": 29, "quantity": 20, "sales": 0}
        }
        self.sales_log = []
        self.total_revenue = 0
        self.total_sales = 1

    def display_stock(self, week_start=True):
        print("Стан запасів:")
        for product, info in self.products.items():
            if week_start:
                info["quantity"] = int(self.total_snacks * (info["sales"]) / self.total_sales)
                if info["quantity"] == 0: info["quantity"] = 20
            print(f"{product} - Запас: {info['quantity']}, Продажі за тиждень: {info['sales']}")

    def update_sales(self):
        self.total_sales = 0
        for product, info in self.products.items():
            while True:
                sales_input = input(f"Введіть кількість проданих одиниць товару '{product}' за тиждень (або q для виходу): ")
                if sales_input.lower() == 'q':
                    sys.exit("Дякуємо за використання автомата зі снеками!")
                try:
                    sales = int(sales_input)
                    if 0 <= sales <= info["quantity"]:
                        self.products[product]["sales"] = sales
                        self.total_sales += sales
                        break
                    else:
                        print(f"Будь ласка, введіть значення в межах від 0 до {info['quantity']}.")
                except ValueError:
                    print("Будь ласка, введіть ціле число.")

    def complete_transaction(self):
        total_transaction_revenue = 0
        for product in self.products:
            transaction_revenue = self.products[product]["price"] * self.products[product]["sales"]
            total_transaction_revenue += transaction_revenue
            self.products[product]["quantity"] = int(self.total_snacks * 0.01 * self.products[product]["sales"])
            self.sales_log.append({"product": product, "price": self.products[product]["price"], "sales": self.products[product]["sales"]})
            print(f"{product} - Продано: {self.products[product]['sales']} од., Сума: {transaction_revenue} грн")
        self.total_revenue += total_transaction_revenue
        print(f"Транзакція завершена. Запаси оновлені. Загальна виручка: {self.total_revenue} грн")
        print(f"Загальна кількість проданого товару за тиждень: {self.total_sales} од.")

    def run(self):
        while True:
            self.display_stock(week_start=True)
            self.update_sales()
            self.complete_transaction()


if __name__ == "__main__":
    vending_machine = SnackVendingMachine()
    vending_machine.run()
