from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json
    months = int(data["months"])
    goal = float(data["goal"])

    results = []

    total_saved = 0

    for i in range(months):

        income = float(data["income"][i])
        food = float(data["food"][i])
        transport = float(data["transport"][i])
        rent = float(data["rent"][i])
        fun = float(data["fun"][i])
        shopping = float(data["shopping"][i])

        expense = food+transport+rent+fun+shopping
        savings = income-expense

        saving_rate = round((savings/income)*100,2)

        if saving_rate >= 30:
            advice="Excellent saving habit"
        elif saving_rate >=15:
            advice="Good but can improve"
        else:
            advice="Reduce unnecessary expenses"

        total_saved += savings

        results.append({
            "month":i+1,
            "income":income,
            "food":food,
            "transport":transport,
            "rent":rent,
            "fun":fun,
            "shopping":shopping,
            "total_expense":expense,
            "savings":savings,
            "saving_rate":saving_rate,
            "advice":advice
        })

    goal_status = "On Track" if total_saved>=goal else "Behind Goal"

    return jsonify({
        "results":results,
        "goal":goal,
        "total_saved":total_saved,
        "goal_status":goal_status
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
