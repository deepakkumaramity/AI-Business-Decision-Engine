"""
Config file for AI Business Decision Engine
Contains hyperparameters and settings
"""

# Model Configuration
MODEL_CONFIG = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': 42,
    'n_jobs': -1
}

# Data Configuration
DATA_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'shuffle': True
}

# Feature Names
FEATURES = [
    'age',
    'income',
    'purchase_frequency',
    'avg_transaction',
    'loyalty_score',
    'product_preference'
]

TARGET = 'profit'

# Thresholds
PROFIT_THRESHOLD = 0.5
HIGH_PROFIT_CLASS = 'High'
LOW_PROFIT_CLASS = 'Low'

# Paths
MODEL_PATH = 'models/model.pkl'
DATA_PATH = 'data/sample_data.csv'

# Streamlit Configuration
STREAMLIT_CONFIG = {
    'page_title': 'AI Business Decision Engine',
    'page_icon': '🚀',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# Business Rules
BUSINESS_RULES = {
    'high_profit_min_income': 50000,
    'high_profit_min_frequency': 8,
    'high_profit_min_loyalty': 0.7,
    'recommended_actions': {
        'High': ['Increase engagement', 'Premium offers', 'VIP treatment'],
        'Low': ['Retention campaign', 'Discount offers', 'Re-engagement']
    }
}