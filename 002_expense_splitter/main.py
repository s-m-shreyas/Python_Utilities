# This functions calculates the split amount, as per the share.

def calculate_split(total_amount: float,
                    currency: str,
                    number_of_person: int|None = None,
                    share: dict[str, float]|None = None)->None:

    
    if share is None:
        if number_of_person is None or number_of_person < 1:
                raise ValueError("Number of people must be greater than one.")
        share_value: float = total_amount/number_of_person
        print(f'Calculating Share for each person...')
        print(f'Share for each person -> {currency} {share_value:,.02f}')
    else:
        if sum(tuple((share.values())))>100:
            raise ValueError('Sum of shares cannot be more than 100%')
        for name, share_percent in share.items():
            share_val = share_percent/100
            share_amount = total_amount*share_val
            print(f'{name} has a share amount of {share_amount:,.02f}')

def main():
    
    while True:
        share: str = input('Please press Y if you have to split percent wise >> ').upper()
        if share != 'Y':
            try:
                total_amount: float = float(input('Please enter the total amount to be splitted >> '))
                number_of_person: int = int(input('Please enter the number of person sharing >> '))
            except ValueError as e:
                print(f'Error: {e}')
            else:
                currency: str = input('Please enter the currency code >> ').upper()
                calculate_split(total_amount, currency, number_of_person) 
        else:
            # percent-wise split branch (inside main)
            try:
                total_amount = float(input('Please enter the total amount to be splitted >> '))
            except ValueError as e:
                print(f'Error: {e}')
                continue

            currency = input('Please enter the currency code >> ').upper()
            share_holders: dict[str, float] = {}

            add_share_holder = 'Y'
            while add_share_holder == 'Y':
                try:
                    share_holder = input('Please enter the name of the share holder >> ').strip().capitalize()
                    share_percent = float(input('Please enter the share (%) >> '))
                except ValueError as e:
                    print(f'Error: {e}')
                else:
                    share_holders[share_holder] = share_percent

                add_share_holder = input('Press Y to add another share holder >> ').upper()

            if share_holders:
                calculate_split(total_amount, currency, share=share_holders)
            else:
                print('No share-holders provided; nothing to calculate.')
        


          

if __name__ == "__main__":
    main()

    