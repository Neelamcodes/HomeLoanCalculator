#home down payment code:
price=10**6
ten_down=price*0.10
twenty_down=price*0.20

good_credit= True
bad_credit=False
high_income=True
has_criminal_record=False

if good_credit and not has_criminal_record:
    print(f'You need to put down ${ten_down} '
          f'You are eligible for loan')
elif bad_credit:
    print(f'You need to put down ${twenty_down}')
else:
    print('try again next time')