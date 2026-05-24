# Finite Differences Calculator

**Live Application:** [https://finite-differences-calculator-webap.vercel.app/](https://finite-differences-calculator-webap.vercel.app/)

A beautifully designed, mathematically rigorous web application built for calculating **Forward, Backward, and Central Finite Differences**. This project was developed as a comprehensive tool for Numerical Methods, demonstrating step-by-step algorithmic solutions alongside interactive, infinite-resolution graphing.

## ✨ Core Features

* **Manual Algorithmic Implementation:** Core finite difference algorithms are implemented from scratch in Python, adhering strictly to numerical methods principles.
* **Infinite-Resolution Graphing & Export:** Integrated with the official **Desmos API** to plot the original function, target points, and true/secant lines dynamically with perfect accuracy. Users can instantly export pristine, high-resolution graph screenshots natively.
* **Robust Mathematical Engine & Error UI:** Powered by SymPy. Features an intelligent parser that handles implicit multiplication and gracefully intercepts mathematical domain errors (e.g., `log(-1)` or dividing by zero) safely, triggering a polished, floating Toast Error UI in the frontend instead of crashing.
* **Step-by-Step Solutions:** Generates full formula substitutions, computed data points (including One-Step Ahead and One-Step Behind tracking), and absolute/relative error analysis compared to the exact analytical derivative.
* **MathJax Integration:** Renders all mathematical output in beautiful, standard LaTeX notation dynamically.
* **Premium & Responsive UI/UX:** Features a custom dark/light mode toggle, sleek glass-morphic design elements, and fluid CSS animations—built entirely with Tailwind CSS and vanilla Javascript. Includes a highly optimized mobile layout engineered with editorial typography (eBay Evo design system constraints) for Android and iOS screens.
* **Supercharged Data Export:** Instantly export calculated results, precise step-by-step formulas, and comprehensive error analysis directly to CSV.
* **Interactive Creator Testimonial:** Features an integrated, smooth-reveal author badge natively implemented without heavy JavaScript framework bloat.

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
