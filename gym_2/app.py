from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    advice = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        sex = request.form['sex']
        if height > 0:
            bmi = weight / (height ** 2)
            if bmi < 16:
                category = "Extremely Underweight"
                advice = "Add extra calories to your meals and do some exercise to increase your appetite! 🥙"
            elif bmi >= 16 and bmi < 18.5:
                category = "Underweight"
                advice = "Eat more high-protein meats in your food! 🥩"
            elif bmi >= 18.5 and bmi < 25:
                category = "Healthy"
                advice = "You are healthy! 🎉"
            elif bmi >= 25 and bmi < 30:
                category = "Overweight"
                advice = "Eat more healthy food! 🍎"
            elif bmi >= 30:
                category = "Extremely Overweight"
                advice = "Eat a balanced diet and do some exercise! 💪"
    
    return render_template('index.html', bmi=bmi, category=category, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
