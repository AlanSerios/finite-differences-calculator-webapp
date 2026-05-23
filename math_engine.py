import sympy as sp
import numpy as np

def calculate_finite_differences(func_str, x_val, h_val):
    try:
        x = sp.symbols('x')
        from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
        transformations = standard_transformations + (implicit_multiplication_application,)
        expr = parse_expr(func_str, local_dict={'e': sp.E, 'pi': sp.pi}, transformations=transformations)
        f = sp.lambdify(x, expr, 'numpy')
        
        # 1. ADVANCED FEATURE: Calculate the EXACT analytical derivative
        f_prime_expr = sp.diff(expr, x)
        f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
        exact_diff = float(f_prime(x_val))
        
        # Evaluate mathematical steps
        fx = float(f(x_val))
        fx_plus_h = float(f(x_val + h_val))
        fx_minus_h = float(f(x_val - h_val))
        
        # Core Calculations
        forward_diff = (fx_plus_h - fx) / h_val
        backward_diff = (fx - fx_minus_h) / h_val
        central_diff = (fx_plus_h - fx_minus_h) / (2 * h_val)
        
        # 2. Graph Plotting Data (Balanced domain to show the whole graph without breaking Y-axis scaling)
        domain = max(abs(h_val) * 20, 10.0)  # Standard bounds of +/- 10
        x_coords = np.linspace(float(x_val) - domain, float(x_val) + domain, 500)
        
        y_fx = []
        y_tangent = []
        y_secant = []
        
        for val in x_coords:
            try:
                y_fx.append(float(f(float(val))))
                y_tangent.append(float(exact_diff * (val - x_val) + fx))
                y_secant.append(float(central_diff * (val - x_val) + fx))
            except (ValueError, TypeError, ZeroDivisionError, OverflowError):
                y_fx.append(None)
                y_tangent.append(None)
                y_secant.append(None)
        
        graph_data = {
            "x_points": [round(float(val), 2) for val in x_coords],
            "y_fx": [round(float(val), 4) if val is not None else None for val in y_fx],
            "y_tangent": [round(float(val), 4) if val is not None else None for val in y_tangent],
            "y_secant": [round(float(val), 4) if val is not None else None for val in y_secant],
            "target_x": round(float(x_val), 2),
            "target_y": round(float(fx), 4)
        }
        
        return {
            "success": True,
            "function_latex": sp.latex(expr),
            "exact_derivative": round(exact_diff, 6),
            "fx": round(fx, 6),
            "fx_plus_h": round(fx_plus_h, 6),
            "fx_minus_h": round(fx_minus_h, 6),
            "x_plus_h": round(x_val + h_val, 6),
            "x_minus_h": round(x_val - h_val, 6),
            "forward": round(forward_diff, 6),
            "backward": round(backward_diff, 6),
            "central": round(central_diff, 6),
            "graph_data": graph_data,
            "steps": {
                "fx": round(fx, 6),
                "fx_plus_h": round(fx_plus_h, 6),
                "fx_minus_h": round(fx_minus_h, 6),
                "x_plus_h": round(x_val + h_val, 6),
                "x_minus_h": round(x_val - h_val, 6),
                "h": h_val,
                "function_str": func_str,
                "derivative_str": str(f_prime_expr),
                "forward_formula": f"({round(fx_plus_h, 6)} - {round(fx, 6)}) / {h_val}",
                "backward_formula": f"({round(fx, 6)} - {round(fx_minus_h, 6)}) / {h_val}",
                "central_formula": f"({round(fx_plus_h, 6)} - {round(fx_minus_h, 6)}) / (2 * {h_val})",
            },
            "errors": {
                "forward_abs": round(abs(forward_diff - exact_diff), 8),
                "forward_rel": round(abs((forward_diff - exact_diff) / exact_diff) * 100, 4) if exact_diff != 0 else None,
                "backward_abs": round(abs(backward_diff - exact_diff), 8),
                "backward_rel": round(abs((backward_diff - exact_diff) / exact_diff) * 100, 4) if exact_diff != 0 else None,
                "central_abs": round(abs(central_diff - exact_diff), 8),
                "central_rel": round(abs((central_diff - exact_diff) / exact_diff) * 100, 4) if exact_diff != 0 else None,
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}