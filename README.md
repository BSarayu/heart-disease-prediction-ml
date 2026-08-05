# ❤️ Heart Disease Prediction using Machine Learning

I built this project to see how far a fairly simple model — Random Forest — could go in flagging patients who might be at risk of heart disease, using the classic UCI Heart Disease dataset. It covers the full pipeline: cleaning the data, exploring it, training the model, checking how well it actually performs, and then wrapping it all in a Streamlit app so anyone can try it out without touching code.

Heart disease is still one of the top causes of death globally, and catching it early — even with a rough, data-driven signal — can genuinely help doctors prioritize who to look at more closely. That's the motivation behind this.

## 🚀 Live Demo

👉https://heart-disease-prediction-ml-ljk2cd4npfcpoxzufjinjq.streamlit.app/

## 📌 What's in here

- Cleaning and preparing the raw patient data
- Exploratory data analysis to understand what actually matters
- Training a Random Forest classifier
- Evaluating it properly (not just accuracy — the metrics that matter for medical predictions)
- Looking at which features drive the predictions
- A Streamlit app so you can plug in numbers and get a prediction interactively

## 📂 Dataset

- **Source:** UCI / Kaggle
- **Target column:** `target`
  - `1` → heart disease present
  - `0` → no heart disease

## 🛠️ Built with

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, and Streamlit for the app itself.

## 📁 Project layout

```text
heart-disease-prediction-ml/
├── dataset/
├── src/
├── screenshots/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ Running it yourself

**1. Clone it**
```bash
git clone https://github.com/YOUR_USERNAME/heart-disease-prediction-ml.git
cd heart-disease-prediction-ml
```

**2. Install what it needs**
```bash
pip install -r requirements.txt
```

**3. Train the model**
```bash
python src/train.py
```

**4. Launch the app**
```bash
streamlit run app.py
```

## 📊 How well does it work?

| Metric   | Value         |
| -------- | ------------- |
| Accuracy | ~89%          |
| Model    | Random Forest |

Worth noting: accuracy alone doesn't tell the whole story for a health-related model — precision and recall matter just as much when a false negative could mean missing a real case.

## 📸 Screenshots

**Home page** — `screenshots/app_home.png`

**Prediction result** — `screenshots/prediction_result.png`

## 💼 Why this project

I put this together to get real, hands-on practice across the whole ML workflow — not just training a model in a notebook, but actually cleaning messy data, thinking about feature engineering, evaluating a model honestly, and shipping something people can interact with. It's also been a good exercise in using Git and GitHub properly for a project from start to finish.

## 📜 License

MIT

## 👩‍💻 Author

**Sarayu**

If this was useful to you, a ⭐ on the repo would mean a lot!
