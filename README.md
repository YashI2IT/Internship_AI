# Energy Consumption Prediction System

## 📋 Project Overview

A Django web application that predicts energy consumption using machine learning models. This project analyzes the AEP (American Electric Power) hourly dataset to forecast energy usage patterns.

## 🎯 Objective

Build a model that predicts energy consumption in smart homes to optimize energy usage and reduce costs.

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (for development)
- **Machine Learning**: NumPy for calculations
- **Frontend**: Bootstrap 5, Chart.js
- **Data**: AEP Hourly Energy Consumption Dataset

## 📁 Project Structure

```
energy-prediction-system/
├── energy_project/           # Django project settings
├── energy_app/              # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── ml_predictor.py      # ML prediction logic
│   └── management/          # Custom commands
├── templates/               # HTML templates
├── static/css/             # Custom CSS
├── media/                  # User uploaded files
├── docs/                   # Documentation
├── Internship (1).ipynb   # Original ML analysis
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Test Data (Optional)
```bash
python manage.py create_test_data --username demo
```

### 4. Start Server
```bash
python manage.py runserver
```

### 5. Access Application
- **URL**: http://127.0.0.1:8000
- **Demo Login**: username=`demo`, password=`demo123`

## 🤖 Machine Learning Models

Based on analysis from `Internship (1).ipynb`:

1. **Linear Regression** - Simple baseline model
2. **XGBoost** - Advanced gradient boosting  
3. **Random Forest** - Ensemble method

### Feature Engineering
- **Hour of day**: Energy usage patterns
- **Day of week**: Weekday vs weekend consumption
- **Month**: Seasonal variations
- **Pattern multipliers**: Derived from historical data

## 📈 Key Features

- **🔮 Energy Prediction**: Input date/time to get MW predictions
- **📊 Analytics Dashboard**: Interactive charts and trends
- **👤 User Management**: Registration, login, profiles
- **📱 Responsive Design**: Works on desktop and mobile

## 🔧 Usage

1. **Register/Login** to create an account
2. **Make Predictions** by selecting date/time and model
3. **View Analytics** to see charts and trends
4. **Manage Profile** to update your information

## 📚 Learning Outcomes

- Django web development
- Machine learning integration
- Data visualization with Chart.js
- User authentication and authorization
- Database design and modeling
- Responsive web design

## 👨‍💻 Developer

**Student**: [Your Name]  
**Supervisor**: Yogesh Sir  
**Year**: 2024

## 📖 Documentation

- [Setup Instructions](docs/SETUP.md)
- [Features Guide](docs/FEATURES.md)

---

**Note**: This is a student project for learning Django and ML integration. The models are simplified implementations based on the Jupyter notebook analysis.