# 🏡 Real Estate Valuation Engine

*Predicting housing values with Machine Learning, FastAPI, and Streamlit.*

---

## 🌟 Overview

The **Real Estate Valuation Engine** is an interactive, full-stack machine learning application designed to predict median house values based on geographic coordinates, demographic information, and property characteristics.

The application separates the frontend from the machine learning inference layer by combining a **FastAPI** backend with a **Streamlit** dashboard.

The dashboard provides real-time data filtering, interactive data exploration, and dynamic **Plotly** visualizations, delivering an intuitive experience for exploring housing data and generating predictions.

---

## ✨ Key Features

- **🤖 Live AI Price Prediction:** Generate estimated median house values using a trained Random Forest Regressor served through a REST API.
- **📊 Interactive Data Explorer:** Explore dataset previews through expandable data tables.
- **🎛️ Dynamic Sidebar Filters:** Filter housing data using interactive sliders for total rooms and households, as well as category selection for ocean proximity.
- **📈 Interactive Visualizations:** Explore regional housing trends through Plotly scatter plots mapping total rooms against median income, with population density represented by color.
- **🔌 API Integration:** Communicate seamlessly with the backend through HTTP requests, including connection checks and error handling.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit, Plotly Express |
| Backend | FastAPI, Uvicorn, Requests |
| Machine Learning | Scikit-Learn (Random Forest Regressor) |
| Data Processing | Pandas |
| Model Serialization | Joblib |

---

## 📂 Project Structure

```text
Housing_Project/
│
├── models/
│   ├── data_frame.pkl        # Serialized dataset for analytics
│   └── model.pkl             # Trained Random Forest model
│
├── app/
│   └── main.py               # FastAPI backend entry point
│
├── housing_app.py            # Streamlit frontend dashboard
│
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started Locally

Follow these steps to run the application on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-estate-valuation-engine.git

cd real-estate-valuation-engine
```

### 2. Install Dependencies

Make sure Python is installed, then install the required packages:

```bash
pip install streamlit pandas plotly requests joblib scikit-learn fastapi uvicorn
```

### 3. Run the FastAPI Backend

Start the backend server:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at:

`http://127.0.0.1:8000`

You can also access the automatically generated API documentation at:

`http://127.0.0.1:8000/docs`

### 4. Launch the Streamlit Frontend

Open a separate terminal and run:

```bash
streamlit run housing_app.py
```

The dashboard will automatically open in your browser.

---

## 💡 How to Use

1. Launch the Streamlit dashboard in your web browser.
2. Navigate to the **Live Price Prediction** section.
3. Enter the required property features, including:
   - Geographic coordinates (latitude and longitude).
   - Housing median age.
   - Total rooms.
   - Population.
   - Median income.
   - Ocean proximity.
4. Click **Predict Price** to receive an estimated house valuation from the trained machine learning model.
5. Use the sidebar filters to explore different housing subsets and interact with the visualizations.

---

## 🎯 Project Goal

This project demonstrates the integration of machine learning with modern web development technologies, covering the complete process of serving a trained model through an API and building an interactive frontend for real-world predictions.
