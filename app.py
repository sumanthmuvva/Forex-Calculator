from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    pair = request.form.get('pair')
    initial_funds = float(request.form.get('initial_funds'))  # initial funds in USD
    leverage = int(request.form.get('leverage'))  # leverage
    pips = float(request.form.get('pips'))

    # Calculate trade size based on initial funds and leverage
    trade_size = initial_funds * leverage

    # Adjust the pip value based on the pair
    if 'JPY' in pair:
        pip_value = 0.01 * (trade_size / pips)
    else:
        pip_value = 0.0001 * trade_size 

    # Calculate profit or loss in USD
    profit_or_loss = pips * pip_value

    # Margin used is equivalent to the initial funds
    margin_used = initial_funds

    results = {
        'trade_size': trade_size,
        'pip_value': pip_value,
        'profit_or_loss': profit_or_loss,
        'profit_per_pip': pip_value,  
        'margin_used': margin_used,
    }
    return jsonify(results)  # This returns a JSON response

if __name__ == '__main__':
    app.run(debug=True)
