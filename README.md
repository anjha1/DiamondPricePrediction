# 💎 Diamond Price Prediction

An end-to-end Machine Learning project that predicts diamond prices using machine learning models, data preprocessing pipelines, and a Flask-based web application. The project demonstrates best practices in ML pipeline development, model training, and deployment.

## 🚀 Features

- 📦 **Data Ingestion & Splitting** - Automated data loading and train-test split
- 🧹 **Data Preprocessing** - Imputation, categorical encoding, feature scaling pipelines
- 🤖 **Model Training** - LinearRegression, Ridge, Lasso, ElasticNet with R² evaluation
- 📈 **Intelligent Model Selection** - Automatic best model selection based on R² scores
- 💾 **Model Serialization** - Pickle-based model and preprocessor saving/loading
- 🌐 **Flask Web Application** - Interactive web UI for price predictions
- 🎨 **Responsive Frontend** - Modern HTML/CSS interface
- 🐳 **Docker Support** - Containerized deployment ready
- 📊 **Logging & Error Handling** - Custom exception handling and detailed logging

## 📊 Model Performance

- **Best Model:** LinearRegression
- **R² Score:** ~0.937 (93.7% variance explained)
- **Training Time:** < 1 second

---

## 🔧 Setup Instructions

### Option 1: Local Setup (Recommended for Development)

#### Step 1: Clone the repository

```bash
git clone https://github.com/anjha1/DiamondPricePrediction.git
cd DiamondPricePrediction
```

#### Step 2: Create and activate virtual environment

**Windows:**
```bash
python -m venv venv_new
venv_new\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv_new
source venv_new/bin/activate
```

#### Step 3: Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 4: Train the model

```bash
python -m src.pipelines.training_pipelines
```

Expected output:
```
[ ... ] Data Ingestion method starts
[ ... ] Train Test Split
[ ... ] Data Transformation: Creating preprocessing object
[ ... ] Model Training Started
[ ... ] LinearRegression - R2 Score: 0.937...
[ ... ] Best Model: LinearRegression
```

#### Step 5: Run the Flask application

```bash
python app.py
```

The app will be available at: **http://127.0.0.1:5000**

---

### Option 2: Docker Setup (Production)

#### Step 1: Build the Docker image

```bash
docker-compose build
```

#### Step 2: Run the container

```bash
docker-compose up
```

The app will be available at: **http://localhost:5000**

#### Stop the container

```bash
docker-compose down
```

---

## 📁 Project Structure

```
DiamondPricePrediction/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipelines/
│   │   └── training_pipelines.py
│   ├── logger.py
│   └── exception.py
├── artifacts/
│   ├── model.pkl          # Trained model
│   ├── preprocessor.pkl   # Data preprocessing pipeline
│   ├── train.csv          # Training data
│   └── test.csv           # Testing data
├── templates/
│   └── index.html         # Web UI
├── static/
│   └── style.css          # Styling
├── app.py                 # Flask application
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
└── README.md             # This file
```

---

## 🧪 Input Features

For prediction, provide the following diamond attributes:

* **Carat** - Weight of the diamond (0.2 to 5.0)
* **Cut** - Quality of cut (Fair, Good, Very Good, Premium, Ideal)
* **Color** - Diamond color grade (J, I, H, G, F, E, D)
* **Clarity** - Diamond clarity (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
* **Depth** - Total depth percentage (43 to 79)
* **Table** - Width of diamond top relative to widest point (43 to 95)
* **X** - Length in mm
* **Y** - Width in mm
* **Z** - Depth in mm

---

## 🌐 How to Use the Web App

1. Open the application at **http://127.0.0.1:5000**
2. Fill in all diamond specifications:
   - Select Cut, Color, and Clarity from dropdowns
   - Enter numerical values for Carat, Depth, Table, and dimensions (X, Y, Z)
3. Click **"Predict"** button
4. View the estimated diamond price instantly!

---

## 🧬 Machine Learning Pipeline

### Data Preprocessing
- **Numerical Features:** StandardScaler normalization
- **Categorical Features:** OneHotEncoder for Cut, Color, Clarity
- **Missing Values:** SimpleImputer with mean strategy

### Model Training
The pipeline automatically:
1. Splits data into train (80%) and test (20%) sets
2. Trains multiple models simultaneously
3. Selects the best model based on R² score
4. Saves model and preprocessor for inference

### Supported Models
- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression

---

## 🔍 Performance Metrics

| Model | R² Score |
|-------|----------|
| LinearRegression | 0.9373 ✅ (Best) |
| Ridge | 0.9373 |
| Lasso | 0.9373 |
| ElasticNet | 0.8541 |

---

## 📦 Dependencies

- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scikit-learn** - ML algorithms and preprocessing
- **flask** - Web framework
- **seaborn** - Data visualization
- **matplotlib** - Plotting
- **gunicorn** - WSGI server for production

---

## 🚀 Troubleshooting

### Issue: Module not found errors
**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Model file not found
**Solution:** Train the model first:
```bash
python -m src.pipelines.training_pipelines
```

### Issue: Port 5000 already in use
**Solution:** Kill the process using port 5000 or specify a different port in `app.py`

---

## 🔐 Security Notes

- Never commit `.pkl` files to public repositories (model contains trained weights)
- Use environment variables for configuration in production
- Validate all user inputs on the server side
- Use HTTPS in production deployments

---

## 📝 License

This project is built for educational purposes.
Feel free to fork, modify, and use for learning.

---

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

## 📧 Contact

Created with ❤️ by **Achhuta Nand Jha**

For questions or feedback, please reach out via GitHub.

---

**Happy Predicting! 💎✨**