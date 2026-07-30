import requests
import json


def get_country_codes()->list[str]:
    response = requests.get(url = fr"https://api.frankfurter.dev/v2/rates?base=USD")
    text_response: str = response.text
    json_object = json.loads(text_response)
    country_codes_available: list[str] | None = [dct['quote'] for dct in json_object]
    return country_codes_available


def fetch_currency_rate(base_currency: str,
                        date_: str, 
                        quote_currency: str)->dict[str, str | float]|None:
    
    country_codes_list: list[str] = get_country_codes()

    try:
        response = requests.get(url = fr"https://api.frankfurter.dev/v2/rates?base={base_currency}&date={date_}")
        text_response: str = response.text
        json_object = json.loads(text_response)

        # country_codes_available: list[str] | None = [dct['quote'] for dct in json_object]

    except Exception as e:
        print(f'Error: {e}')
        print(country_codes_list)
        print(f'Please re-enter a valid base currency code from the above list')
        main()

    else:
        for dct in json_object:
            if quote_currency in dct.values():
                return dct
            else:
                pass

        print(f'{country_codes_list}')
        print(f'Please re-enter the details and use the quote currency code from the above given list.')
        main()


def main()->None:
    base_currency: str = input('Please provide your base currency code >> ').upper()
    date_: str = input('Please provide the date [YYYY-MM-DD] of rate you want to check >> ')
    quote_currency: str = input('Please provide the currency you want to quote to >> ').upper()
    fetched_currency_rate: dict[str, str | float] | None = fetch_currency_rate(base_currency, date_, quote_currency)
    print(fetched_currency_rate)


if __name__ == '__main__':
    main()




