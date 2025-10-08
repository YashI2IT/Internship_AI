# Features Documentation

## 🔮 Energy Prediction

### How it Works
The system uses machine learning models trained on AEP (American Electric Power) hourly consumption data to predict future energy usage.

### Available Models
1. **Linear Regression** - Simple baseline model
2. **XGBoost** - Advanced gradient boosting
3. **Random Forest** - Ensemble method

### Input Requirements
- **Date & Time**: Select when you want to predict consumption
- **Model Choice**: Choose which ML algorithm to use

### Output
- **Predicted Consumption**: Energy usage in Megawatts (MW)
- **Prediction History**: View all your past predictions

## 📊 Analytics Dashboard

### Charts Available
1. **Model Usage Distribution** - Pie chart showing which models you use most
2. **Daily Prediction Activity** - Bar chart of predictions per day
3. **Consumption Trends** - Line chart showing predicted values over time

### Data Insights
- Track your prediction patterns
- Compare different model results
- Analyze energy consumption trends

## 👤 User Management

### Registration
- Create account with username, email, password
- Optional: Add first name, last name

### Profile Management
- Update personal information
- Add bio, location, birth date
- Upload profile picture
- View account creation date

### Activity Tracking
- System tracks all user actions
- View recent activities on dashboard
- Monitor prediction history

## 🎨 User Interface

### Responsive Design
- Works on desktop and mobile devices
- Bootstrap 5 framework for modern UI
- Font Awesome icons for visual appeal

### Navigation
- **Dashboard**: Overview of your account and recent activity
- **Predict**: Make new energy consumption predictions
- **Analytics**: View charts and data insights
- **Profile**: Manage your account information

### Interactive Elements
- Real-time form validation
- Success/error message notifications
- Interactive charts with Chart.js
- Hover effects and animations