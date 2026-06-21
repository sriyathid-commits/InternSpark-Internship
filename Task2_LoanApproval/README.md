
# Task 2: Loan Approval Prediction

## 📌 Objective
Build a supervised machine learning model to predict loan approval status based on applicant features.  
Focus areas:
- Preprocessing and handling missing values
- Addressing class imbalance with SMOTE
- Comparing multiple models
- Recommending deployment strategy

---

## 📂 Dataset
- Source: Loan application dataset (structured tabular data)
- Target: `Loan_Status` (Approved / Not Approved)

---

## ⚙️ Preprocessing
- Missing values handled (median for numeric, mode for categorical)
- Label encoding for categorical variables
- StandardScaler applied to numerical features
- Train/Test split: 80/20 with stratification

---

## ⚖️ Class Imbalance
- Initial distribution: ~70% Approved vs ~30% Not Approved
- Applied **SMOTE** to balance classes in training set
- Result: ~50/50 balanced dataset

---

## 🤖 Models Compared
- Logistic Regression  
- Decision Tree  
- Random Forest  

---

## 📊 Model Performance

| Model               | Precision | Recall  | F1‑Score | ROC‑AUC |
|----------------------|-----------|---------|----------|---------|
| Logistic Regression  | 0.8370    | 0.9059  | 0.8701   | 0.8220  |
| Decision Tree        | 0.8169    | 0.6824  | 0.7436   | 0.6701  |
| Random Forest        | 0.8556    | 0.9059  | 0.8800   | 0.7565  |

---

## 🔎 Insights
- **Random Forest**: Best overall performance (highest F1‑Score and Precision, strong Recall).  
- **Logistic Regression**: Competitive with highest ROC‑AUC and interpretability.  
- **Decision Tree**: Lower performance, less suitable without optimization.

---

## 🚀 Deployment Recommendation
- Use **Random Forest** with threshold = **0.5** for initial deployment.  
- Balance between maximizing approvals of eligible loans (high recall) and minimizing risky approvals (good precision).  
- Further refinement: Perform cost‑benefit analysis to align threshold with business objectives.

---

## 📁 Deliverables
- `notebooks/loan_prediction.ipynb` → Full analysis and training workflow  
- `plots/` → Confusion matrix, ROC curve, feature importance  
- `report/LoanApproval_Report.pdf` → One‑page strategy document  
- `README.md` → This summary

