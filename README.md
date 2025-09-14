# RentVerse AI Service

A production-ready FastAPI service for property rental price prediction using machine learning. This service provides REST API endpoints for predicting property rental prices in Malaysia based on property features like location, size, type, and furnishing status.

## 🏗️ Project Structure

```
rentverse-ai-service/
├── rentverse/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── cli.py                     # CLI commands for dev/prod
│   ├── config.py                  # Configuration management
│   ├── models/                    # ML models and schemas
│   │   ├── __init__.py
│   │   ├── ml_models.py          # Model loading/inference logic
│   │   ├── schemas.py            # Pydantic request/response models
│   │   ├── enhanced_deployment_pipeline.pkl    # Enhanced ML model
│   │   ├── standard_deployment_pipeline.pkl    # Standard ML model
│   │   ├── enhanced_price_prediction_pipeline.pkl
│   │   └── improved_price_prediction_pipeline.pkl
│   ├── api/                       # API endpoints and middleware
│   │   ├── __init__.py
│   │   ├── middleware.py         # Custom middleware
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── health.py         # Health check endpoints
│   │       └── prediction.py     # Prediction endpoints
│   ├── core/                      # Core business logic
│   │   ├── __init__.py
│   │   ├── exceptions.py         # Custom exceptions
│   │   └── logging.py            # Logging configuration
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       ├── helpers.py            # General utilities
│       └── preprocessor.py       # Data preprocessing utilities
├── notebooks/                     # Jupyter notebooks for model development
│   ├── Rentverse_rentprice_prediction.ipynb
│   ├── compiled.csv              # Training data
│   └── *.csv                     # Model evaluation results
├── tests/                         # Test files
├── debug_prediction.py           # Debug script for testing
├── test_batch_prediction.py      # API testing script
├── use_pipeline.py               # Pipeline usage examples
├── pyproject.toml                # Poetry dependencies
├── Dockerfile                    # Docker configuration
├── docker-compose.yml           # Docker Compose setup
├── .env.example                  # Environment variables template
└── README.md
```

## 🚀 Features

- **FastAPI Framework**: High-performance, async web framework with automatic API documentation
- **Advanced ML Pipeline**: Enhanced Extra Trees model with log transformation (R² = 0.84+)
- **Data Preprocessing**: Robust preprocessing with outlier removal and feature engineering
- **Batch Processing**: Support for single and batch predictions (up to 100 properties)
- **Malaysian Property Focus**: Optimized for Malaysian rental market with location parsing
- **Health Checks**: Comprehensive health and readiness endpoints with model validation
- **Input Validation**: Strict Pydantic schemas with property type and range validation
- **Error Handling**: Structured error handling with detailed debugging information
- **Logging**: Comprehensive logging for monitoring and debugging
- **Docker Support**: Complete containerization with Docker and Docker Compose
- **CORS Support**: Configurable CORS settings for web applications
- **Utility Module**: Reusable preprocessor utilities for data validation and cleaning

## 📋 API Endpoints

### Health & Monitoring
- `GET /api/v1/health` - Basic health check
- `GET /api/v1/health/ready` - Readiness check with model validation
- `GET /api/v1/health/live` - Liveness check

### Predictions
- `POST /api/v1/predict/single` - Single property price prediction
- `POST /api/v1/predict/batch` - Batch property price predictions
- `GET /api/v1/predict/model-info` - Model information and metadata

### Documentation
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation
- `GET /` - API information and available endpoints

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12+
- Poetry (for dependency management)
- Docker (optional, for containerization)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rentverse-ai-service
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

4. **Run development server**
   ```bash
   # Using Poetry
   poetry run python -m uvicorn rentverse.main:app --reload --host 0.0.0.0 --port 8000
   
   # Or using CLI (if available)
   poetry run dev
   ```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📝 API Usage Examples

### Single Property Prediction

```bash
curl -X POST "http://localhost:8000/api/v1/predict/single" \
  -H "Content-Type: application/json" \
  -d '{
    "property_type": "Condominium",
    "bedrooms": 3,
    "bathrooms": 2,
    "area": 1200,
    "furnished": "Yes",
    "location": "KLCC, Kuala Lumpur"
  }'
```

**Response:**
```json
{
  "predicted_price": 2500.0,
  "confidence_score": 0.89,
  "price_range": {
    "min": 2200.0,
    "max": 2800.0
  },
  "currency": "RM",
  "status": "success",
  "model_version": "Extra Trees",
  "features_used": ["property_type", "bedrooms", "bathrooms", "area", "furnished", "region"],
  "timestamp": "2025-09-14T10:30:00"
}
```

### Batch Property Prediction

```bash
curl -X POST "http://localhost:8000/api/v1/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": [
      {
        "property_type": "Condominium",
        "bedrooms": 3,
        "bathrooms": 2,
        "area": 1200,
        "furnished": "Yes",
        "location": "KLCC, Kuala Lumpur"
      },
      {
        "property_type": "Apartment",
        "bedrooms": 2,
        "bathrooms": 1,
        "area": 800,
        "furnished": "No",
        "location": "Petaling Jaya, Selangor"
      }
    ]
  }'
```

**Response:**
```json
{
  "predictions": [
    {
      "batch_index": 0,
      "predicted_price": 2500.0,
      "confidence_score": 0.89,
      "price_range": {"min": 2200.0, "max": 2800.0},
      "currency": "RM",
      "status": "success",
      "model_version": "Extra Trees",
      "timestamp": "2025-09-14T10:30:00"
    },
    {
      "batch_index": 1,
      "predicted_price": 1800.0,
      "confidence_score": 0.85,
      "price_range": {"min": 1620.0, "max": 1980.0},
      "currency": "RM",
      "status": "success",
      "model_version": "Extra Trees",
      "timestamp": "2025-09-14T10:30:00"
    }
  ],
  "total_count": 2,
  "success_count": 2,
  "error_count": 0,
  "timestamp": "2025-09-14T10:30:00"
}
```

### Model Information

```bash
curl -X GET "http://localhost:8000/api/v1/predict/model-info"
```

**Response:**
```json
{
  "model_version": "Extra Trees",
  "created_at": "2025-09-14T10:30:00",
  "feature_columns": ["property_type", "bedrooms", "bathrooms", "area", "furnished", "region"],
  "supported_property_types": ["Apartment", "Condominium", "Service Residence", "Townhouse"],
  "supported_furnished_types": ["Yes", "No", "Partial", "Fully Furnished", "Partially Furnished", "Unfurnished"],
  "is_loaded": true,
  "max_batch_size": 100,
  "use_log_transform": true,
  "performance_metrics": {
    "test_r2": 0.8408,
    "test_rmse": 425.67,
    "test_mae": 301.23
  }
}
```

## 🏠 Property Data Format

The API expects property data in the following format:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `property_type` | string | Yes | Type of property | "Condominium", "Apartment", "Townhouse", "Service Residence" |
| `bedrooms` | integer | Yes | Number of bedrooms | 3 |
| `bathrooms` | integer | Yes | Number of bathrooms | 2 |
| `area` | number | Yes | Area in square feet | 1200.0 |
| `furnished` | string | Yes | Furnishing status | "Yes", "No", "Partial", "Fully Furnished", "Partially Furnished", "Unfurnished" |
| `location` | string | Yes | Property location | "KLCC, Kuala Lumpur", "Petaling Jaya, Selangor" |

### Validation Rules
- **bedrooms**: 0-10 bedrooms
- **bathrooms**: 1-10 bathrooms  
- **area**: 1-10,000 square feet
- **location**: Non-empty string (location parsing extracts region automatically)

## 🧠 Model Information

### Current Model
- **Algorithm**: Extra Trees Regressor with 200 estimators
- **Preprocessing**: Robust preprocessing with outlier removal and log transformation
- **Performance**: R² = 0.84+ (explains 84%+ of price variance)
- **Features**: 6 engineered features including location region parsing
- **Training Data**: Malaysian rental property data with aggressive outlier filtering

### Model Features
1. **property_type**: Encoded property type
2. **bedrooms**: Number of bedrooms
3. **bathrooms**: Number of bathrooms  
4. **area**: Property area in square feet
5. **furnished**: Encoded furnishing status
6. **region**: Extracted region from location string

### Price Range
- **Minimum**: RM 500/month
- **Maximum**: RM 50,000/month
- **Typical Range**: RM 800 - RM 8,000/month
- **Currency**: Malaysian Ringgit (RM)

## ⚙️ Configuration

Configuration is managed through environment variables. Key settings:

```bash
# Application
APP_NAME="RentVerse AI Service"
DEBUG=false
LOG_LEVEL=INFO

# Server
HOST=0.0.0.0
PORT=8000

# Model
MODEL_DIR=rentverse/models
MAX_BATCH_SIZE=100

# API
API_PREFIX=/api/v1
CORS_ORIGINS=["*"]
```

Copy `.env.example` to `.env` and customize as needed.

## 🐳 Docker Support

### Quick Start
```bash
# Build and run with Docker Compose
docker-compose up -d

# Check logs
docker-compose logs -f
```

### Manual Docker
```bash
# Build image
docker build -t rentverse-ai .

# Run container
docker run -p 8000:8000 rentverse-ai

# Run with environment file
docker run -p 8000:8000 --env-file .env rentverse-ai
```

## 🧪 Testing

### Debug Scripts
```bash
# Test prediction pipeline locally
python debug_prediction.py

# Test API endpoints
python test_batch_prediction.py

# Test pipeline usage
python use_pipeline.py
```

### Health Checks
```bash
# Basic health check
curl http://localhost:8000/api/v1/health

# Model readiness check  
curl http://localhost:8000/api/v1/health/ready

# Detailed model information
curl http://localhost:8000/api/v1/predict/model-info
```

## 🔧 Development

### Adding New Features
1. **Model Updates**: Update notebooks and retrain models
2. **API Changes**: Modify schemas in `rentverse/models/schemas.py`
3. **Preprocessing**: Update utilities in `rentverse/utils/preprocessor.py`
4. **Routes**: Add endpoints in `rentverse/api/routes/`

### Preprocessing Utilities
The service includes a comprehensive preprocessor utility:

```python
from rentverse.utils import ImprovedDataPreprocessor, validate_property_data

# Create preprocessor
preprocessor = ImprovedDataPreprocessor(
    remove_outliers=True,
    price_percentile=90,
    area_percentile=95,
    verbose=False
)

# Validate input data
validated_data = validate_property_data(property_dict)
```

## 📊 Model Performance

- **Algorithm**: Extra Trees Regressor (Enhanced Pipeline)
- **R² Score**: 0.8408 (84.08% variance explained)
- **RMSE**: ~426 RM
- **MAE**: ~301 RM
- **Features**: 6 engineered features
- **Data**: Cleaned Malaysian rental property dataset
- **Preprocessing**: Aggressive outlier removal, log transformation

## 🚨 Error Handling

The API provides detailed error responses:

```json
{
  "error": "Validation failed",
  "detail": "Invalid bedrooms count: 15", 
  "code": 400,
  "status": "error",
  "timestamp": "2025-09-14T10:30:00"
}
```

Common error codes:
- **400**: Invalid input data or validation failure
- **500**: Internal server error or prediction failure
- **503**: Model not available or loading failure

## 📈 Monitoring

### Logs
The service provides structured logging for monitoring:
- Request/response logging
- Model prediction logging  
- Error tracking with stack traces
- Performance metrics

### Metrics
Available through model info endpoint:
- Prediction success/failure rates
- Model performance metrics
- Feature importance
- Processing times

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Update documentation
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For issues, questions, or feature requests:
- Create an issue in the repository
- Check the API documentation at `/docs`
- Review the debug scripts for troubleshooting
