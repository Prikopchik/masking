import json
from datetime import datetime

def mask_card_number(card_number):
    first_parts = ''
    last_parts = ''
    
    if len(card_number) >= 6:
        first_parts = card_number[:6]
        card_number = card_number[6:]
    
    if len(card_number) >= 4:
        last_parts = card_number[-4:]
        card_number = card_number[:-4]
    
    masked_middle = '*' * len(card_number)
    
    masked_number = first_parts + '' + masked_middle + '' + last_parts
    masked_number = ' '.join([masked_number[i:i+4] for i in range(0, len(masked_number), 4)])
    return masked_number



def mask_account_number(account_number):
    return '**' + account_number[-4:]

def print_last_transactions(transactions):
    transaction_name_from = ""
    transaction_name_to = ""
    for transaction in transactions:
        if 'date' in transaction:
            transaction['date'] = datetime.fromisoformat(transaction['date'])

    transactions_with_date = [transaction for transaction in transactions if 'date' in transaction]

    transactions_with_date.sort(key=lambda x: x['date'], reverse=True)

    for transaction in transactions_with_date[:6]:
        if transaction['state'] == 'EXECUTED':
            print(transaction['date'].strftime('%d.%m.%Y'))
            print(transaction['description'])
            if 'from' in transaction:
                masked_from = transaction['from']
                masked_to =transaction['to']
                while masked_from[0].isdigit() != True:
                        transaction_name_from += masked_from[0]
                        masked_from = masked_from[1:]
                while masked_to[0].isdigit() != True:
                        transaction_name_to += masked_to[0]
                        masked_to = masked_to[1:]
                if transaction_name_from == ("Счет "):
                    masked_from = mask_account_number(masked_from)
                else:
                    masked_from = mask_card_number(masked_from)
                if transaction_name_to == ("Счет "):
                    masked_to = mask_account_number(masked_to)
                else:
                    masked_to = mask_card_number(masked_to)
                print(transaction_name_from, masked_from + ' -> ' + transaction_name_to, masked_to)
            else:
                print('Счет ',mask_account_number(transaction['to']))
            transaction_name_from = ""
            transaction_name_to = ""
            print(transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['name'])
            print()

with open('operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print_last_transactions(data)