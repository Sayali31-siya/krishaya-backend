import pandas as pd
from chatbot import chatbot_reply

# Load crop data
data = pd.read_csv("Mergedcrops.csv")

def chatbot_reply(question):
    # Simple parsing (you’ll upgrade later)
    if "tomato" in question.lower() and "karnataka" in question.lower() and "april" in question.lower():
        filtered = data[
            (data["State"].str.contains("Karnataka", case=False)) &
            (data["Commodity"].str.contains("Tomato", case=False)) &
            (data["Month"].str.contains("April", case=False))
        ]
        if not filtered.empty:
            avg_price = filtered["Modal Price"].mean()
            return f"The average price of Tomato in April (Karnataka) is ₹{int(avg_price)}"
        else:
            return "Sorry, I couldn't find that info."
    return "I’m still learning! Ask me about crop prices by location and month."

