# Generate the updated Streamlit Blackjack Advisor code that supports full-hand evaluation (multi-card input)

final_app_code = """
import streamlit as st

# Convert card string to value
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# Determine if hand is soft or hard and compute total
def evaluate_hand(cards):
    values = [card_value(c) for c in cards]
    total = sum(values)
    num_aces = cards.count('A')

    # Reduce Ace from 11 to 1 if bust
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1

    is_soft = 'A' in cards and total <= 21 and any(v == 11 for v in values)
    return total, is_soft

# Decision engine based on total, soft/hard, and dealer upcard
def get_strategy(total, is_soft, dealer_card):
    dealer_val = card_value(dealer_card)

    # Soft totals
    if is_soft and total <= 21:
        if total >= 19:
            return "Stand"
        elif total == 18:
            if dealer_val in [2, 7, 8]:
                return "Stand"
            elif dealer_val in [3, 4, 5, 6]:
                return "Double or Hit"
            else:
                return "Hit"
        elif total <= 17:
            if dealer_val in [4, 5, 6]:
                return "Double or Hit"
            else:
                return "Hit"

    # Hard totals
    if not is_soft:
        if total >= 17:
            return "Stand"
        elif total in [13, 14, 15, 16]:
            return "Stand" if dealer_val in [2, 3, 4, 5, 6] else "Hit"
        elif total == 12:
            return "Stand" if dealer_val in [4, 5, 6] else "Hit"
        elif total in [10, 11]:
            return "Double or Hit"
        else:
            return "Hit"

    return "Stand"

# Streamlit App
st.title("♠️ Blackjack Advisor – Full Strategy Mode")

st.markdown("Enter your full hand (e.g., `10, A`, `2, 3, 6`) and the dealer's upcard to get real-time advice based on full basic strategy.")

# Input Section
player_hand_input = st.text_input("Your Cards (comma-separated):", "A, 6")
dealer_card = st.selectbox("Dealer's Upcard:", ['2','3','4','5','6','7','8','9','10','J','Q','K','A'])

# Handle Submit
if st.button("🧠 Get Strategy Advice"):
    player_cards = [c.strip().upper() for c in player_hand_input.split(',') if c.strip()]
    valid_cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    if all(c in valid_cards for c in player_cards) and dealer_card in valid_cards:
        total, is_soft = evaluate_hand(player_cards)
        strategy = get_strategy(total, is_soft, dealer_card)

        st.success(f"**Hand Total:** {total} ({'Soft' if is_soft else 'Hard'})")
        st.info(f"**Recommended Move:** {strategy}")
    else:
        st.error("Please enter only valid cards (2–10, J, Q, K, A). Separate them with commas.")
"""

# Save to file for user to upload into Streamlit
file_path = "/mnt/data/app.py"
with open(file_path, "w") as f:
    f.write(final_app_code)

file_path
