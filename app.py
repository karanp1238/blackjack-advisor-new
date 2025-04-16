import streamlit as st

def blackjack_advisor(player_cards, dealer_card):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    if len(player_cards) == 2 and player_cards[0] == player_cards[1]:
        pair = player_cards[0]
        if pair == 'A' or pair == '8':
            return "Split"
        elif pair == '10':
            return "Stand"
        elif pair == '9':
            return "Split" if dealer_card not in ['7', '10', 'A'] else "Stand"
        elif pair == '7':
            return "Split" if dealer_card in ['2', '3', '4', '5', '6', '7'] else "Hit"
        elif pair == '6':
            return "Split" if dealer_card in ['2', '3', '4', '5', '6'] else "Hit"
        elif pair == '5':
            return "Double or Hit" if dealer_card in ['2', '3', '4', '5', '6', '7', '8', '9'] else "Hit"
        elif pair == '4':
            return "Split" if dealer_card in ['5', '6'] else "Hit"
        elif pair in ['2', '3']:
            return "Split" if dealer_card in ['2', '3', '4', '5', '6', '7'] else "Hit"

    if 'A' in player_cards:
        other = [card for card in player_cards if card != 'A'][0]
        total = 11 + card_value(other)
        if total >= 19:
            return "Stand"
        elif total == 18:
            if dealer_card in ['2', '7', '8']:
                return "Stand"
            elif dealer_card in ['3', '4', '5', '6']:
                return "Double or Hit"
            else:
                return "Hit"
        elif total <= 17:
            if dealer_card in ['4', '5', '6']:
                return "Double or Hit"
            else:
                return "Hit"

    total = sum(card_value(c) for c in player_cards)
    if total >= 17:
        return "Stand"
    elif total in [13, 14, 15, 16]:
        return "Stand" if dealer_card in ['2', '3', '4', '5', '6'] else "Hit"
    elif total == 12:
        return "Stand" if dealer_card in ['4', '5', '6'] else "Hit"
    elif total in [10, 11]:
        return "Double or Hit"
    else:
        return "Hit"

# Streamlit UI
st.title("Blackjack Advisor - LuckyHands")

card1 = st.selectbox("Your First Card", ['2','3','4','5','6','7','8','9','10','J','Q','K','A'])
card2 = st.selectbox("Your Second Card", ['2','3','4','5','6','7','8','9','10','J','Q','K','A'])
dealer = st.selectbox("Dealer's Upcard", ['2','3','4','5','6','7','8','9','10','J','Q','K','A'])

if st.button("Get Advice"):
    result = blackjack_advisor([card1, card2], dealer)
    st.success(f"Recommended Move: **{result}**")
