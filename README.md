```markdown
# 💎 Diamond Price Prediction

This is an end-to-end Machine Learning project that predicts the price of a diamond based on features such as carat, cut, color, clarity, depth, and dimensions. It includes data preprocessing, model training, evaluation, and deployment via a Flask-based web app.

---

## 📁 Project Structure

```

DiamondPricePrediction/
│
├── artifacts/                  # Stores raw, train, test data and saved models
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw\.csv
│   ├── test.csv
│   └── train.csv
│
├── notebooks/                  # Jupyter Notebooks for analysis
│   ├── data/
│   ├── EDA.ipynb
│   └── Model Training.ipynb
│
├── src/                        # Main source code
│   ├── components/             # Data ingestion, transformation, training
│   │   ├── **init**.py
│   │   ├── data\_ingestion.py
│   │   ├── data\_transformation.py
│   │   └── model\_trainer.py
│   ├── pipelines/              # Training and prediction pipelines
│   │   ├── **init**.py
│   │   ├── prediction\_pipeline.py
│   │   └── training\_pipelines.py
│   ├── **init**.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── static/                     # Static files like CSS
│   └── style.css
│
├── templates/                  # HTML templates
│   └── index.html
│
├── app.py                      # Flask web app
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignored files
├── README.md                   # Project readme
└── setup.py                    # Setup for packaging (optional)

````

---

## 🚀 Features

- 📦 Data Ingestion & Train-Test Split
- 🧹 Data Preprocessing with Pipelines (Imputation, Encoding, Scaling)
- 🤖 Model Training with LinearRegression, Ridge, Lasso, ElasticNet
- 📈 R² Score-based model selection
- 💾 Pickle-based model saving/loading
- 🌐 Flask-based Web UI for Prediction
- 🎨 Stylish, Responsive Frontend using HTML & CSS

---

## 🔧 Setup Instructions

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/diamond-price-prediction.git
cd diamond-price-prediction
````

### Step 2: Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train the model

```bash
python -m src.pipelines.training_pipelines
```

### Step 5: Run the Flask app

```bash
python app.py
```

---

## 🧪 Input Features

* **Carat**
* **Cut** *(Fair, Good, Very Good, Premium, Ideal)*
* **Color** *(J to D)*
* **Clarity** *(I1 to IF)*
* **Depth**
* **Table**
* **X, Y, Z** *(dimensions in mm)*

---

## 🌐 Web App

* Enter the diamond features
* Click "Predict"
* Get the estimated price instantly!

---

## 📊 Best Model

* ✅ **LinearRegression**
* 🎯 **R² Score:** \~0.937 on test set

---

## 📄 License

This project is built for educational purposes.
Feel free to fork and customize.

---

Made with ❤️ by Achhuta Nand Jha

```
