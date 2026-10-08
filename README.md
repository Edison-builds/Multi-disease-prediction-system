# Multi-Disease Prediction System

A web-based Machine Learning application for predicting **Heart Disease, Diabetes, and Breast Cancer** using machine learning models trained on publicly available datasets.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Installation

### 1. Clone the Repository

After creating your GitHub repository, clone the repository using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd disease-predictor
```

### 2. Create a Virtual Environment

Install `virtualenv` if it is not already installed:

```bash
pip install virtualenv
```

Create a virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Then open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

## Features

- Diabetes prediction
- Heart disease prediction
- Breast cancer prediction
- Machine Learning-based prediction
- Django-based web application
- User-friendly web interface
- Multiple disease prediction modules

## Technologies Used

- Python
- Django
- Machine Learning
- Scikit-learn
- NumPy
- Pandas
- HTML5
- CSS3
- Bootstrap
- SQLite

## Datasets

The Machine Learning models are developed using publicly available datasets obtained from Kaggle.

## Publication

This project has been published as a research paper in the **International Research Journal of Modernization in Engineering Technology and Science (IRJMETS)**.

**Paper Title:**  
*MULTI-DISEASE PREDICTION SYSTEM USING MACHINE LEARNING: AN INTEGRATED WEB-BASED APPROACH FOR EARLY DETECTION OF DIABETES, HEART DISEASE, AND BREAST CANCER*

**Author:** Edison J

**Journal:** International Research Journal of Modernization in Engineering Technology and Science (IRJMETS)

**Volume:** 08

**Issue:** 06

**Publication Date:** June 2026

**Paper ID:** IRJMETS80600088916

**DOI:** https://doi.org/10.56726/IRJMETS100592

## Project Structure

```text
disease-predictor/
│
├── core/
├── predictor/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── README.md
├── Procfile
└── runtime.txt
```

## Built With

- [Django](https://www.djangoproject.com/) - Web framework
- [Python](https://www.python.org/) - Programming language
- [Scikit-learn](https://scikit-learn.org/) - Machine Learning library
- [Pandas](https://pandas.pydata.org/) - Data analysis
- [NumPy](https://numpy.org/) - Numerical computing

## Author

**J. Edison**

MCA Graduate | Aspiring Software Engineer

## Disclaimer

This project is developed for educational and academic purposes. The predictions provided by this application should not be considered a substitute for professional medical diagnosis or advice.
