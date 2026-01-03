# Ticket system logic
tickets = 100 
while True:
    
    n = input('Enter tickets you want to buy: ')
    n = int(n)

    if tickets-n < 0:
        print('Tickets are not available . Try Again')
        continue

    tickets -= n
    print(f'Tickets left : {tickets}')

    if tickets == 0:
        print('Tickets are sold out')
        break
