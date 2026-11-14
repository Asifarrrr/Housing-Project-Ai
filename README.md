# 🏡 Real Estate Valuation Engine
*Predicting housing values with machine learning, FastAPI, and Streamlit.*

---

## 🌟 Overview

The **Real Estate Valuation Engine** is an interactive, full-stack machine learning web application designed to predict median house values based on geographic coordinates, demographic features, and property characteristics. 

The application decouples presentation logic from machine learning inference by pairing a high-performance **FastAPI** backend with a modern, feature-rich **Streamlit** frontend dashboard equipped with real-time data filtering and interactive **Plotly** data visualizations. 📊✨

---

## ✨ Key Features

* **🤖 Live AI Price Prediction:** Instantly calculate estimated median house values using a fine-tuned Random Forest Regressor model served via a REST API.
* **📊 Interactive Data Explorer:** Inspect dataset previews directly within expandable table containers.
* **🎛️ Dynamic Sidebar Filters:** Filter housing data live using dual sliders for total rooms/households and category selection for ocean proximity.
* **📈 Rich Visualizations:** Gain insights into regional housing trends using dark-themed Plotly scatter plots mapping total rooms against median income, color-coded by population density.
* **🔌 Robust API Integration:** Seamlessly handles backend communication with automatic error handling and connection status checks.

---

## 🛠️ Technology Stack

* **Frontend:** Streamlit, Plotly Express
* **Backend Inference:** FastAPI, Uvicorn, Requests
* **Machine Learning / Data:** Scikit-Learn (Random Forest Regressor), Pandas, Joblib

---

## 📂 Project Structure

```text
Housing_Project/
│
├── models/
│   ├── data_frame.pkl        # Serialized dataset for preview and analytics
│   └── model.pkl             # Trained Random Forest Regressor model
│
├── app/
│   └── main.py               # FastAPI backend entry point
│
├── housing_app.py            # Streamlit frontend dashboard interface
└── README.md                 # Project documentation
```
## 🚀 Getting Started Locally
Follow these steps to get your full-stack application up and running on your local machine:

- 1. Clone the Repository
Bash
git clone [https://github.com/your-username/real-estate-valuation-engine.git](https://github.com/your-username/real-estate-valuation-engine.git)
cd real-estate-valuation-engine
- 2. Install Dependencies
Ensure you have Python installed, then install the required packages:

Bash
pip install streamlit pandas plotly requests joblib scikit-learn fastapi uvicorn
- 3. Run the FastAPI Backend
Start the backend model server to handle prediction requests:

Bash
uvicorn app.main:app --reload --port 8000
- 4. Launch the Streamlit Frontend
Open a separate terminal window and run the dashboard UI:

Bash
streamlit run housing_app.py
## 💡 How to Use
Launch the Streamlit dashboard in your web browser. 🌐

**Navigate to the Live Price Prediction section on the right column.

**Fill out the property features (such as geographic coordinates, housing median age, total rooms, population, median income, and ocean proximity). 📝

**Click Predict Price to receive a real-time estimated valuation from the model. 💰

**Use the Dashboard Features sidebar to filter property subsets and explore interactive scatter analytics. 🔍
