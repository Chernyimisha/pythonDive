# У вас есть банковская карта с начальным балансом равным 0 у.е.
# Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых
# необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
# Пополнение счета:
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
# Снятие средств:
# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств
# начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
# Завершение работы:
# Функция exit() завершает работу с банковским счетом. Перед завершением,
# если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
# Проверка кратности суммы:
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному
# множителю MULTIPLICITY. Реализуйте программу для управления банковским счетом,
# используя библиотеку decimal для точных вычислений.

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount: float) -> bool:
    if amount % MULTIPLICITY == 0:
        return True
    else:
        print('Сумма должна быть кратной 50 у.е.')


def deposit(amount):
    global bank_account
    global operations
    if check_multiplicity(amount) is True:
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')


def withdraw(amount):
    global bank_account
    global operations
    comission = decimal.Decimal(amount * PERCENT_REMOVAL)
    if comission < MIN_REMOVAL:
        comission = MIN_REMOVAL
    elif comission > MAX_REMOVAL:
        comission = MAX_REMOVAL
    withdraw_sum = decimal.Decimal(amount + comission)
    if check_multiplicity(amount) is True:
        if withdraw_sum < bank_account:
            bank_account -= withdraw_sum
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {comission:.0f} у.е.. Итого {bank_account:.0f} у.е.')
        else:
            operations.append(
                f'Недостаточно средств. Сумма с комиссией {withdraw_sum:.0f} у.е. На карте {bank_account} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {withdraw_sum:.0f} у.е. На карте {bank_account} у.е.')


def exit():
    global bank_account
    global operations
    if bank_account > RICHNESS_SUM:
        richness_comission = bank_account * RICHNESS_PERCENT
        bank_account -= richness_comission
        operations.append(f'Вычтен налог на богатство {0.1}% в сумме {richness_comission} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)



