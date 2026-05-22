from flask import Flask, render_template, request, jsonify
from math_engine import calculate_finite_differences
from input_sanitizer import sanitize_function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    inputs = {}
    
    if request.method == 'POST':
        func_str = request.form.get('function', '').strip()
        
        try:
            func_str = sanitize_function(func_str)
            x_val = float(request.form.get('x_value'))
            h_val = float(request.form.get('h_value'))
            
            inputs = {'function': func_str, 'x_value': x_val, 'h_value': h_val}
            
            # FIX: We only pass the 3 required arguments to the math engine
            results = calculate_finite_differences(func_str, x_val, h_val)
        except ValueError as e:
            results = {"success": False, "error": str(e)}
            inputs = {'function': func_str, 'x_value': request.form.get('x_value', ''), 'h_value': request.form.get('h_value', '')}
        
    return render_template('index.html', results=results, inputs=inputs)

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "Invalid JSON"})
        
    func_str = data.get('function', '').strip()
    try:
        func_str = sanitize_function(func_str)
        x_val = float(data.get('x_value'))
        h_val = float(data.get('h_value'))
        
        results = calculate_finite_differences(func_str, x_val, h_val)
        return jsonify(results)
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)})
    except Exception as e:
        return jsonify({"success": False, "error": "An error occurred."})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)