# Finite Differences Calculator

A beautifully designed, mathematically rigorous web application built for calculating **Forward, Backward, and Central Finite Differences**. This project was developed as a comprehensive tool for Numerical Methods, demonstrating step-by-step algorithmic solutions alongside interactive, infinite-resolution graphing.

## ✨ Core Features

* **Manual Algorithmic Implementation:** Core finite difference algorithms are implemented from scratch in Python, adhering strictly to numerical methods principles.
* **Infinite-Resolution Graphing:** Integrated with the official **Desmos API** to plot the original function, target points, true tangent lines, and calculated secant lines dynamically with perfect accuracy.
* **Robust Mathematical Engine:** Powered by SymPy. Features an intelligent parser that understands implicit multiplication (e.g., `2x`, `x(2)`) and gracefully handles mathematical domain errors (e.g., `log(-5)`).
* **Step-by-Step Solutions:** Generates full formula substitutions, computed data points, and absolute/relative error analysis compared to the exact analytical derivative.
* **MathJax Integration:** Renders all mathematical output in beautiful, standard LaTeX notation dynamically.
* **Premium UI/UX:** Features a custom dark/light mode toggle, sleek glass-morphic design elements, floating input labels, and fluid CSS animations—built entirely with Tailwind CSS and vanilla Javascript.
* **Data Export:** Instantly export calculated results to CSV for external analysis.

## 🛠️ Technology Stack

* **Backend:** Python 3.8+, Flask, SymPy, NumPy (for exact analytical validations)
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **APIs & Rendering:** Desmos Graphing Calculator API, MathJax (LaTeX)

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd finite-differences-app
   ```

2. **Create a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the calculator.

## 📐 Project Objectives

This project satisfies the core requirements for a Numerical Methods web application:
1. Provides a short mathematical discussion of the method (Theory section).
2. Shows fully worked examples with step-by-step solutions (Examples section).
3. Includes an interactive calculator where users can input parameters and obtain numeric results.
4. Implements core algorithms manually using Python and Flask, with HTML/CSS templates and MathJax LaTeX rendering.

---
*Designed and built for Numerical Methods precision.*
