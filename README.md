# **AerOptima** ✈️
## **An End-to-End Data Project for Flight Delay Prediction**

![AerOptima cover](<AerOptima cover.png>)

---

## 📌 **Project Overview**
AerOptima is a comprehensive data science project designed to analyze and predict US flight delays. The project covers the entire data lifecycle, from engineering and cleaning to exploratory analysis and advanced machine learning modeling.

The primary goal is to predict the **arrival delay** of a flight using only information available before takeoff, providing a realistic tool for passengers and airlines.


## 📂 **Repository Structure**

The project is organized into three main pillars:

### 👨‍🔬 Data Engineering

```
├── 📁 Data Engineer
│   ├── 🐍 Data_Engineer.py
│   └── 📄 Data_engineer.ipynb
```
- **Folder:** ``Data Engineer/``

- **Key Files:** ``Data_Engineer.py``, ``Data_engineer.ipynb``

- **Objective:** Ingestion and cleaning of raw aviation datasets.

- **Tasks:** Handling missing values, database management (SQLite), and initial feature preparation to ensure data consistency across the pipeline.

### 📊 Data Analysis

```
├── 📁 Data Analyst
│   ├── 📁 Exports
│   │   ├── 🖼️ Average delay per day of week.png
│   │   ├── 🖼️ Change in average delay per month.png
│   │   ├── 🖼️ Correlation matrix.png
│   │   ├── 🖼️ Delay distribution.png
│   │   ├── 🖼️ Link departure and arrival delay.png
│   │   ├── 🖼️ Mean delay for each airline.png
│   │   └── 🖼️ Occurence of airlines.png
│   └── 📄 Data_Analyst.ipynb
```

- **Folder:** ``Data Analyst/``

- **Key Files:** ``Data_Analyst.ipynb``, ``Exports/``

- **Objective:** Uncovering trends and correlations in flight data.

- **Highlights:**
    - Analysis of delays by **airline performance**.

    - Temporal patterns (delay distribution by **day of the week** and **month**).

![Average Delay by Day of Week](Data%20Analyst/Exports/Average%20delay%20per%20day%20of%20week.png)
*Insight: Flight delays fluctuate significantly depending on the day of the week, revealing patterns in air traffic congestion.*


### 🤖 Data Science

```
├── 📁 Data Scientist
│   ├── 🖼️ Actual flights vs forecasts.png
│   └── 📄 Data Scientist.ipynb
```

- **Folder:** ``Data Scientist/``

- **Key Files:** ``Data Scientist.ipynb``

- **Objective:** Building a robust predictive model.

- **Models used:** Linear Regression (Baseline) and **XGBoost** (Advanced).

- **The "Honest Model" Approach:** A major focus of this project was identifying and removing **Data Leakage**. We strictly eliminated "future variables" (like ``AIR_SYSTEM_DELAY`` or ``WHEELS_ON``) to ensure the model makes genuine predictions.

![Actual vs Forecasts](Data%20Scientist/Actual%20flights%20vs%20forecasts.png)
*Result: Our final "honest" XGBoost model (red) successfully anticipates the baseline structural delays (the signal) while correctly ignoring unpredictable, exceptional spikes (the noise).*


## 🚀 **Technical Stack**

- **Language:** Python 3.13.9

- **Data Handling:** Pandas, NumPy, SQLite

- **Visualization:** Matplotlib, Seaborn

- **Machine Learning:** Scikit-Learn, **XGBoost** (GPU accelerated)


## 📈 **Results & Key Learnings**

- **Initial Accuracy:** Our first models reached an unrealistically low error (MAE of 3.5 min) due to data leakage.

- **Final Performance:** After cleaning "future" features, our **XGBoost** model achieved a realistic **MAE of ~17 minutes**, significantly outperforming the Linear Regression baseline.

- **Conclusion:** Predicting flight delays is a complex task where understanding the difference between signal (structural delays) and noise (exceptional events) is key.

## 👤 **Author**
Project created by Nathan Houel.