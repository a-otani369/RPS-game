from flask import Flask, render_template, request
import random

app = Flask(__name__)

hands = ["グー", "チョキ", "パー"]

def judge(player, computer):
    if player == computer:
        return "引き分け"
    elif (player == "グー" and computer == "チョキ") or \
         (player == "チョキ" and computer == "パー") or \
         (player == "パー" and computer == "グー"):
        return "勝ち！"
    else:
        return "負け..."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    player_hand = None
    computer_hand = None

    if request.method == "POST":
        player_hand = request.form["hand"]
        computer_hand = random.choice(hands)
        result = judge(player_hand, computer_hand)

    return render_template("index.html", result=result,
                           player_hand=player_hand,
                           computer_hand=computer_hand,
                           hands=hands)

if __name__ == "__main__":
    app.run(debug=True)

