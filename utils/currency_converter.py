# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 21/09/2019
def convert_currency_to_knuts(amount, currency):
    """
    Converts currencies to knuts
    :param amount:
    :param currency:
    :return:
    """
    converion_table_to_knuts = {
        'USD': 73,
        'SIC': 29,
        'GAL': 493
    }
    dollars_to_knuts = amount * converion_table_to_knuts.get(currency)
    return dollars_to_knuts


def convert_g_s_k_price_to_knuts(galleons, sickles):
    galleons_to_knuts = convert_currency_to_knuts(galleons, 'GAL')
    sickles_to_knuts = convert_currency_to_knuts(sickles, 'SIC')
    return galleons_to_knuts + sickles_to_knuts


def convert_back_to_g_s_k(initial_knuts):
    galleons = initial_knuts // 493
    galleons_to_knuts = convert_currency_to_knuts(galleons, 'GAL')
    remaining_knuts = initial_knuts - galleons_to_knuts
    sickles = remaining_knuts // 29
    knuts = convert_currency_to_knuts(sickles, 'SIC')
    return {
        'galleons': galleons,
        'sickles': sickles,
        'knuts': remaining_knuts - knuts
    }

