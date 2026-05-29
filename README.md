# 💰 FinanceAI Coach

> **Your AI-powered personal finance coach — available 24/7, judgment-free, for less than a coffee per week.**

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Live Demo

Deploy your own in 2 minutes → [share.streamlit.io](https://share.streamlit.io)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏠 **Dashboard** | Real-time financial health overview with KPI metrics |
| 📊 **Budget Tracker** | Track transactions, set limits, visualize spending |
| 🤖 **AI Coach Chat** | Personalized financial advice powered by Claude AI |
| 🎯 **Goals** | Set and track financial goals with AI projections |
| 📈 **Investments** | Portfolio overview and AI-driven recommendations |
| 📋 **Business Plan** | Full MVP roadmap and go-to-market strategy |

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: Anthropic Claude API
- **Charts**: Plotly
- **Database**: Supabase *(optional for persistence)*
- **Payments**: Stripe *(for subscription tier)*

---

## ⚡ Quick Deploy to Streamlit Cloud

### Step 1 — Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/ai-finance-coach.git
cd ai-finance-coach
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run Locally
```bash
streamlit run app.py
```

### Step 4 — Deploy to Streamlit Cloud (FREE)
1. Push to GitHub: `git push origin main`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"**
4. Select your repo → `app.py`
5. Add secrets (optional):
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
6. Click **Deploy** 🎉 — live in ~2 minutes!

---

## 🔐 Environment Variables (Optional)

Create `.streamlit/secrets.toml` for local development:
```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
PLAID_CLIENT_ID = "your-plaid-id"
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

> ⚠️ Never commit secrets to GitHub. Add `.streamlit/secrets.toml` to `.gitignore`

---

## 📁 Project Structure

```
ai-finance-coach/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .streamlit/
│   └── config.toml          # Theme & server config
└── .gitignore
```

---

## 🗺️ MVP Roadmap

| Phase | Timeline | Key Deliverables |
|-------|----------|-----------------|
| **Phase 1** | Months 1-2 | Core dashboard, budget tracking, Streamlit deploy |
| **Phase 2** | Months 3-4 | Plaid bank sync, Claude AI chat, mobile UI |
| **Phase 3** | Months 5-7 | Goals, investments, Stripe billing |
| **Phase 4** | Months 8-12 | Enterprise tier, native mobile app |

---

## 💸 Business Model

- **Free tier**: Core tracking (10,000 users target)
- **Pro — $9.99/month**: AI coaching + insights
- **Premium — $19.99/month**: Investment advice + tax optimization
- **Enterprise — $5/user/month**: Employer wellness programs

**Year 1 Target**: $336K ARR with 2,500 paid users

---

## 🤝 Contributing

Pull requests welcome! Please open an issue first for major changes.

---

## 📄 License

MIT License — free to use and modify.

---

*Built with ❤️ using Streamlit + Anthropic Claude*
