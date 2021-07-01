import pprint
data = [{'name': 'maksim','total': 10000, 'amount': 3456},
        {'name': 'bakyt','total': 100000, 'amount': 345600},
        {'name': 'thor','total': 5600, 'amount': 3400},
        {'name': 'steve','total': 1000000, 'amount': 500000},
        {'name': 'john','total': 9870, 'amount': 9870},
        {'name': 'sue','total': 12345, 'amount': 1234},
        {'name': 'almaz','total': 10000, 'amount': 9999},
        {'name': 'alex','total': 1000, 'amount': 250},
        {'name': 'alex1', 'total': 1000, 'amount': 45},
        {'name': 'alex2', 'total': 1000, 'amount': 25000000000000},

        ]

MIN_SUM = 50
BANK_AMOUNT = 100000000

def withdrawal(data,bank_amount):
    report = []
    for info in data:
        user_report = {}
        amount = info['amount']
        if amount < MIN_SUM:
            user_report[info['name']] = False
            user_report['reason'] = 'введена сумма меньше минимальной'
            print('вы не можете')
        else:
            if bank_amount >= amount:
                if info['total'] >= amount:
                    info['total'] -= amount
                    bank_amount -= amount
                    user_report[info['name']] = True
                else:
                    user_report[info['name']] = False
                    user_report['reason'] = 'Недостаточно средств'
            else:
                user_report[info['name']] = False
                user_report['reason'] = 'банкомат не может выдать деньги'
        report.append(user_report)
    global BANK_AMOUNT
    BANK_AMOUNT = bank_amount
    return data, report
pprint.pprint(withdrawal(data,BANK_AMOUNT))



