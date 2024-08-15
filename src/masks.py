def get_mask_card_number(card_num: str) -> str | None:
    """the card number as input and returns its mask"""
    if card_num.isdigit() and len(card_num) == 16:
        return f"{card_num[:4]} {card_num[4:6]} {"*" * 2} {"*" * 4} {card_num[12:]}"
    else:
        return None


def get_mask_account(acc_num: str) -> str | None:
    """the account number as input and returns its mask"""
    if acc_num.isdigit() and len(acc_num) == 20:
        return f"{"*" * 2} {acc_num[-4::]}"
    else:
        return None
