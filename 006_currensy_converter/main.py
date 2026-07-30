import requests
import json


def get_country_codes()->list[dict[str, str]]:

    response = requests.get(url = fr"https://api.frankfurter.dev/v2/currencies")
    text_response: str = response.text
    json_object = json.loads(text_response)
    # print(json_object)

    return json_object


def fetch_currency_rate(base_currency: str,
                        date_: str, 
                        quote_currency: str)->tuple[dict[str, str|float], dict[str, str]]|None:
    
    country_codes_list: list[dict[str, str]] = get_country_codes()

    try:

        response = requests.get(url = fr"https://api.frankfurter.dev/v2/rates?base={base_currency}&date={date_}")
        text_response: str = response.text
        json_object: list[dict[str, str|float]]= json.loads(text_response)

    except Exception as e:

        print(f'Error: {e}')
        print(country_codes_list)
        print(f'Please re-enter a valid base currency code from the above list')
        main()

    else:
        for dct, dct2 in zip(json_object, country_codes_list):

            if quote_currency in dct.values():

                print(f'Date: {dct['date']}')
                print(f'Base Currency Code: {dct['base']}')
                print(f'Target Currency Code: {dct['quote']}')
                # print(f'Base Currency Price: {} 1/-')
                print(f'Target Currency Price: {dct2['symbol']} {dct['rate']}/-')
                
                return (dct, dct2)
                
            else:
                pass

        print(f'{country_codes_list}')
        print(f'Please re-enter the details and use the quote currency code from the above given list.')
        main()


def main()->None:

    base_currency: str = input('Please provide your base currency code >> ').upper()
    date_: str = input('Please provide the date [YYYY-MM-DD] of rate you want to check >> ')
    quote_currency: str = input('Please provide the currency you want to quote to >> ').upper()

    if base_currency != quote_currency:
        fetch_currency_rate(base_currency, date_, quote_currency)
    else:
        print('Base currency code cannot be same as target currency price.')
    


if __name__ == '__main__':
    main()




