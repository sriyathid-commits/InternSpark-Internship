# 🍽️ Task 1 — Zomato Dataset Analysis

## 📊 Dataset Source and Purpose
The dataset used in this project is the **Zomato Bangalore Restaurants dataset**, containing details such as restaurant names, locations, cuisines, ratings, and average cost for two people.  
**Purpose:** To analyze restaurant trends, customer preferences, and pricing patterns in Bangalore using data visualization and exploratory analysis.

---

## ⚙️ How to Run the Notebook and Script

### Option 1 — Jupyter/Colab Notebook
1. Open `zomato.ipynb` in **VS Code** (Jupyter extension) or **Google Colab**.  
2. Run all cells sequentially to view data cleaning, analysis, and visualizations.  
3. Outputs (plots and tables) will appear inline in the notebook.

### Option 2 — Terminal Script
1. Ensure `zomato.csv` is placed inside the `data/` folder.  
2. Run the script from terminal:
   ```bash
   python zomato.py
3.All plots will be automatically saved in the plots/ folder.
📈 What Each Plot Represents
Word Cloud: Shows the most frequent cuisines mentioned in the dataset. Larger words indicate higher frequency.

Bar Chart — Top 10 Cuisines by Restaurant Count: Displays which cuisines are most common among Bangalore restaurants.

Bar Chart — Top 10 Cuisines by Average Rating: Compares average ratings across the most popular cuisines.

Scatter Plot — Price vs Rating: Visualizes how restaurant ratings vary with average cost for two people.

Bar Chart — Top 10 Locations by Average Rating: Highlights areas with the highest‑rated restaurants.

Heatmap (if included): Shows correlations between numeric features like cost, rating, and votes.

Insights and Conclusions
Indian, Chinese, and South Indian cuisines dominate Bangalore’s restaurant scene.

Moderately priced restaurants (₹500–₹2000) receive the most customer ratings, suggesting affordability drives engagement.

Top-rated areas include Lavelle Road, Koramangala, and Church Street, known for premium dining experiences.

Price vs Rating shows no strong correlation — expensive restaurants don’t always guarantee higher ratings.

Fusion cuisines (Continental + Asian + Mediterranean) tend to maintain consistently high ratings, indicating customer appreciation for variety.

🧰 Tools and Libraries Used
Python — Data analysis and visualization

Pandas — Data cleaning and manipulation

Matplotlib / Seaborn — Plotting and visualization

WordCloud — Text frequency visualization

📦 Deliverables
zomato.ipynb — Interactive notebook with analysis and outputs

zomato.py — Terminal script for automated plot generation

plots/ — Folder containing saved visualizations

data/zomato.csv — Dataset file

README.md — Project documentation

✨ This project is part of the InternSpark Internship — Task 1: Exploratory Data Analysis on Zomato Dataset.

---

