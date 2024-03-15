from main import mask_card_number, mask_account_number


def test_mask_card_number():
    assert mask_card_number('1234567890123456') == '1234 56** **** 3456'
    assert mask_card_number('1111222233334444') == '1111 22** **** 4444'
    assert mask_card_number('') == ''

def test_mask_account_number():
    assert mask_account_number('1234567890') == '**7890'
    assert mask_account_number('9876543210') == '**3210'
    assert mask_account_number('') == '**'
