# My First Python Project: Rule-Based Reservoir Evaluation Tool

My first real Python project after learning and practising Python in Jupyter Notebook.

This project started as a simple play around with Python. I wanted to see if I could bring a few functions together to create a console that collects well-log values from a user and returns preliminary interpretations based on simple rules.

What began as an experiment became my first small, interactive Python application. I decided to document it here because it marks the beginning of my journey into data science and applying programming to subsurface problems.

## About the Project

The **Rule-Based Reservoir Evaluation Tool** is a beginner-friendly Python console application that accepts four well-log measurements:

- Gamma Ray (GR)
- Resistivity (RES)
- Neutron Porosity (NPHI)
- Bulk Density (RHOB)

It uses predefined conditional rules to return preliminary interpretations of lithology, hydrocarbon potential and possible fluid type.

The console was created using a simple prompt:

> Create a console that collects user inputs and produces outputs using the functions below.

It was a small experiment, but it was exciting to see the functions come together into a program I could run and interact with.

## Features

- Collects well-log values from the user through a console.
- Uses separate Python functions for each interpretation.
- Applies `if`, `elif` and `else` statements to classify input values.
- Returns preliminary lithology, hydrocarbon-zone and fluid-type indications.
- Handles some invalid numerical inputs.
- Allows the user to exit the console by entering `q` at the Gamma Ray prompt.

## Tools Used

- **Python** — programming language.
- **Jupyter Notebook** — used during my Python learning and practice.
- **Python built-in functions and features** — including conditional statements, user input, dictionaries, loops and exception handling.

No external Python libraries are required to run the current version.

## What I Learned

Working on this project helped me move from practising Python in Jupyter Notebook to writing code that I could run as a complete, interactive program.

Through this exercise, I practised:

- **Python functions:** Breaking the evaluation logic into smaller, reusable functions.
- **Conditional statements:** Using `if`, `elif` and `else` to apply simple rules to well-log values.
- **User input:** Collecting GR, RES, NPHI and RHOB values through a console.
- **Error handling:** Using `try` and `except` to handle invalid numerical inputs.
- **Loops:** Repeating the evaluation process until the user chooses to exit.
- **Dictionaries:** Grouping the interpretation results into a single structure.
- **Problem-solving:** Exploring how Python can be used to represent simplified screening rules for a geoscience problem.

Most importantly, I learned that I do not need to start with a complex project to begin applying programming to my field.

## How to Run the Project

### 1. Clone the repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/rule-based-reservoir-evaluation.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the project folder

```bash
cd rule-based-reservoir-evaluation
```

### 3. Run the program

Make sure Python is installed, then run:

```bash
python reservoir_console.py
```

Depending on your system, you may need to use `python3` instead of `python`.

No additional packages are required.

## Example Usage

When the program starts, it asks the user to enter the well-log values.

```text
==================================================
        RESERVOIR EVALUATION CONSOLE
==================================================
Enter well log values below. Type 'q' at any prompt to quit.

Gamma Ray (GR) [API units, or 'q' to quit]: 35
Resistivity (RES) [ohm.m]: 80
Neutron Porosity (NPHI) [v/v]: 0.12
Bulk Density (RHOB) [g/cc]: 2.2

--- Evaluation Result ---
Inputs           : GR=35.0, RES=80.0, NPHI=0.12, RHOB=2.2
Lithology        : Clean Sandstone
Hydrocarbon Zone : Possible Hydrocarbon Zone
Fluid Type       : Possible Gas
--------------------------------------------------
```

*Note: This is an illustrative example of the program's output, not a validated geological interpretation.*

## How the Rules Work

The program uses simple predefined thresholds to generate its results.

| Function | Purpose |
|---|---|
| `evaluate_lithology()` | Uses Gamma Ray values to classify intervals into simplified lithology categories. |
| `evaluate_hydrocarbon_zone()` | Uses Gamma Ray and resistivity to screen for possible hydrocarbon-bearing intervals. |
| `evaluate_fluid_type()` | Uses resistivity, neutron porosity and bulk density to generate preliminary fluid indications. |
| `Reservoir_evaluation()` | Combines the results of the three evaluation functions. |
| `run_console()` | Runs the interactive console and displays the results. |

These rules were created as a learning exercise to practise Python logic in a geoscience context.

## Important Limitations

This is a **simple, rule-based learning project**, not a validated petrophysical evaluation tool.

The interpretation thresholds are illustrative and have not been calibrated against field-specific geological data or independently validated results.

In actual subsurface work:

- Gamma Ray responses depend on lithology, mineralogy and local formation characteristics.
- Resistivity must be interpreted in context; high resistivity does not automatically indicate hydrocarbons.
- Fluid interpretation requires consideration of lithology, porosity, formation water properties, borehole conditions and other relevant information.
- Reliable petrophysical evaluation involves appropriate quality control, calibrated parameters and integration of available subsurface data.

The outputs should therefore be treated as preliminary screening indications, not definitive identification of reservoir lithology or fluid type. This program should not be used to make operational or field-development decisions.

## Future Improvements

As I continue learning Python and data science, I would like to explore ways to improve this project, including:

- Improving input validation and handling unrealistic or out-of-range values.
- Reviewing and refining the interpretation rules with appropriate petrophysical guidance.
- Extending the program to evaluate multiple depth intervals from a well-log dataset.
- Reading LAS files using Python.
- Using Pandas for well-log data handling and quality control.
- Visualising well logs and interpreted intervals using Plotly.
- Exporting evaluation results to CSV.
- Adding automated tests and documenting the assumptions behind each rule.

These are future learning goals, not features already implemented in the current version.

## A Note on My Journey

As a geoscientist, I am interested in exploring how programming, data analytics and eventually machine learning can support well-log analysis and other subsurface workflows.

This project may be simple, but it represents an important step for me: moving from learning Python concepts to experimenting with how I can apply them to problems within my field.

I am sharing it not because it is perfect, but because it is the beginning. I look forward to learning, building and improving one project at a time.

I welcome **constructive feedback, corrections, mentorship and opportunities to learn and apply these skills within a subsurface team**.

If you have suggestions on how a beginner can improve this project or approach similar subsurface problems with Python, I would be glad to learn from your experience.

Thank you for taking the time to explore my first project!

---

*This repository documents my learning journey. The code and interpretation rules may evolve as I gain more experience in Python, data science and petrophysical evaluation.*
