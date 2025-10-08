# Setup Instructions

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Test Data (Optional)**
   ```bash
   python manage.py create_test_data --username demo
   ```

4. **Start Server**
   ```bash
   python manage.py runserver
   ```

5. **Access Application**
   - URL: http://127.0.0.1:8000
   - Demo Login: username=`demo`, password=`demo123`

## Features

- **Energy Prediction**: Input date/time to get MW predictions
- **Multiple ML Models**: Linear Regression, XGBoost, Random Forest
- **Analytics Dashboard**: Charts showing prediction trends
- **User Management**: Registration, login, profile management

## Project Structure

```
energy-prediction-system/
├── energy_project/          # Django project settings
├── energy_app/             # Main application
├── templates/              # HTML templates
├── static/                 # CSS and static files
├── media/                  # User uploaded files
├── docs/                   # Documentation
├── Internship (1).ipynb   # Original ML analysis
├── manage.py               # Django management
├── requirements.txt        # Dependencies
└── README.md              # Main documentation
```