## 📄 README.md


# 📊 Avazu CTR Marketing Dashboard

An interactive **Streamlit dashboard** for analyzing **Click-Through Rate (CTR)** performance across devices, apps, and sites using a sample of the **Avazu dataset**.

This project provides key marketing insights such as **total impressions, clicks, CTR performance, and top-performing categories** with interactive filters and time-series analysis.

---

## 🚀 Features
- **Filters**
  - Date range filter (days)
  - Device type filter
  - App category filter
  - Site category filter
- **Key Metrics**
  - Total impressions
  - Total clicks
  - Overall CTR (%)
- **Visualizations**
  - Top 10 CTR by app category, site category, device model, and device type
  - Daily CTR trend over time (time series chart)

---

## 🛠 Tech Stack
- **Python**
- **Pandas** (data processing)
- **Streamlit** (dashboard UI)
- **Plotly Express** (interactive charts)

---

## 📂 Project Structure
```

CTR\_PRO/
│── requirements.txt
│── Dash.py              # Streamlit dashboard
│── 50krecords.csv       # Sample dataset (50k rows from Avazu)
│── README.md

````

---

## ⚡ Installation & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/CTR_PRO.git
   cd CTR_PRO


2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate # On Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:

   ```bash
   streamlit run src/Dash.py
   ```

5. Open the app in your browser at:

   ```
   http://localhost:8501
   ```

---

## 📊 Dataset

* **Avazu Click-Through Rate Prediction Dataset** (sample: 50k records)
* Original dataset: [Kaggle - Avazu CTR](https://www.kaggle.com/c/avazu-ctr-prediction)

---

## 🔮 Future Improvements

* Add hourly CTR trends
* Deploy to **Streamlit Cloud**
* Use a larger dataset for deeper insights
* Add predictive modeling (CTR prediction)

---

## 👩‍💻 Author

**Mariam Sayed**
