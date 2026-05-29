import streamlit as st

st.set_page_config(
    page_title="FinanceAI Coach",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --primary: #00C896;
    --primary-dark: #00A07A;
    --accent: #FFD166;
    --bg: #0A0F1E;
    --card: #111827;
    --border: #1F2937;
    --text: #F9FAFB;
    --muted: #6B7280;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

h1, h2, h3 { font-family: 'Syne', sans-serif; }

.stApp { background-color: var(--bg); }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00C896, #FFD166);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}

.hero-sub {
    font-size: 1.15rem;
    color: #9CA3AF;
    margin-bottom: 2rem;
    font-weight: 300;
}

.metric-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.2s ease;
}

.metric-card:hover { border-color: var(--primary); transform: translateY(-2px); }

.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--primary);
}

.metric-label {
    font-size: 0.85rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.25rem;
}

.nav-pill {
    display: inline-block;
    background: var(--primary);
    color: #000;
    font-weight: 600;
    padding: 0.3rem 1rem;
    border-radius: 999px;
    font-size: 0.8rem;
    margin-bottom: 1rem;
}

.section-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}

.insight-chip {
    display: inline-block;
    background: rgba(0,200,150,0.12);
    border: 1px solid rgba(0,200,150,0.3);
    color: var(--primary);
    border-radius: 8px;
    padding: 0.4rem 0.8rem;
    font-size: 0.85rem;
    margin: 0.2rem;
}

.warn-chip {
    display: inline-block;
    background: rgba(255,209,102,0.12);
    border: 1px solid rgba(255,209,102,0.3);
    color: var(--accent);
    border-radius: 8px;
    padding: 0.4rem 0.8rem;
    font-size: 0.85rem;
    margin: 0.2rem;
}

.chat-bubble-user {
    background: var(--primary);
    color: #000;
    border-radius: 18px 18px 4px 18px;
    padding: 0.75rem 1.1rem;
    margin: 0.5rem 0;
    max-width: 75%;
    margin-left: auto;
    font-size: 0.95rem;
}

.chat-bubble-ai {
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 18px 18px 18px 4px;
    padding: 0.75rem 1.1rem;
    margin: 0.5rem 0;
    max-width: 80%;
    font-size: 0.95rem;
}

.stButton > button {
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: #000;
    font-weight: 600;
    font-family: 'Syne', sans-serif;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1.5rem;
    transition: all 0.2s;
}

.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 20px rgba(0,200,150,0.3); }

.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div > input,
.stTextArea textarea {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}

.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--primary);
    padding: 1rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
}

div[data-testid="stSidebar"] {
    background: #0D1321;
    border-right: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown('<div class="sidebar-logo">💰 FinanceAI Coach</div>', unsafe_allow_html=True)
    st.markdown("**Navigation**")
    page = st.radio("", [
        "🏠 Dashboard",
        "📊 Budget Tracker",
        "🤖 AI Coach Chat",
        "🎯 Goals",
        "📈 Investments",
        "📋 Business Plan"
    ], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("**Your Profile**")
    st.markdown("👤 Demo User")
    st.markdown("💼 Financial Health: **Good**")
    st.progress(0.72)
    st.caption("Score: 720 / 1000")

# ─── DASHBOARD ────────────────────────────────────────────────
if page == "🏠 Dashboard":
    st.markdown('<div class="hero-title">Your Financial Command Center</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">AI-powered insights to grow, protect, and optimize your money</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        ("$8,420", "Monthly Income", "↑ 5%"),
        ("$5,180", "Monthly Spend", "↓ 3%"),
        ("$3,240", "Net Savings", "↑ 12%"),
        ("$24,600", "Total Savings", "↑ 8%"),
    ]
    for col, (val, label, change) in zip([col1,col2,col3,col4], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{val}</div>
                <div class="metric-label">{label}</div>
                <div style="color:#00C896;font-size:0.8rem;margin-top:0.3rem">{change} vs last month</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1.6, 1])

    with col_a:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Spending Breakdown")
        import pandas as pd
        import plotly.express as px
        df = pd.DataFrame({
            "Category": ["Housing", "Food", "Transport", "Entertainment", "Healthcare", "Shopping", "Other"],
            "Amount": [1800, 650, 380, 290, 210, 450, 400]
        })
        fig = px.bar(df, x="Category", y="Amount",
                     color="Amount", color_continuous_scale=["#00C896","#FFD166"],
                     template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          showlegend=False, coloraxis_showscale=False,
                          margin=dict(t=10, b=10))
        fig.update_traces(marker_line_width=0)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 AI Insights")
        st.markdown('<span class="insight-chip">✅ 38% savings rate</span>', unsafe_allow_html=True)
        st.markdown('<span class="insight-chip">✅ Emergency fund: 4 months</span>', unsafe_allow_html=True)
        st.markdown('<span class="warn-chip">⚠️ Food budget 18% over</span>', unsafe_allow_html=True)
        st.markdown('<span class="warn-chip">⚠️ Shopping spike detected</span>', unsafe_allow_html=True)
        st.markdown('<span class="insight-chip">✅ No missed payments</span>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("**💡 Top Recommendation**")
        st.info("You could save an extra **$234/month** by switching to a meal-prep routine. That's **$2,808/year** toward your house down payment!")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📈 6-Month Savings Trend")
    months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May"]
    savings = [1800, 2100, 1950, 2400, 2900, 3240]
    income =  [7800, 7900, 8000, 8100, 8200, 8420]
    spend =   [6000, 5800, 6050, 5700, 5300, 5180]
    fig2 = px.line(x=months, y=[income, spend, savings],
                   labels={"x":"Month","value":"$"},
                   template="plotly_dark",
                   color_discrete_sequence=["#00C896","#EF4444","#FFD166"])
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       legend=dict(orientation="h", y=1.1),
                       margin=dict(t=10,b=10))
    fig2.data[0].name = "Income"
    fig2.data[1].name = "Spending"
    fig2.data[2].name = "Savings"
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─── BUDGET TRACKER ────────────────────────────────────────────
elif page == "📊 Budget Tracker":
    st.markdown('<div class="hero-title">Budget Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Track every dollar. Find every opportunity.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### ➕ Add Transaction")
        t_name = st.text_input("Description", placeholder="e.g. Grocery run")
        t_amount = st.number_input("Amount ($)", min_value=0.0, step=10.0)
        t_cat = st.selectbox("Category", ["Housing","Food","Transport","Entertainment","Healthcare","Shopping","Income","Other"])
        t_type = st.radio("Type", ["Expense", "Income"], horizontal=True)
        if st.button("Add Transaction"):
            st.success(f"✅ Added: {t_name} — ${t_amount:.2f} [{t_cat}]")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Budget Limits")
        import pandas as pd
        budgets = {"Food": (650, 550), "Shopping": (450, 300), "Entertainment": (290, 250), "Transport": (380, 380)}
        for cat, (spent, limit) in budgets.items():
            pct = min(spent/limit, 1.0)
            color = "🔴" if pct >= 1 else "🟡" if pct >= 0.8 else "🟢"
            st.markdown(f"**{color} {cat}** — ${spent} / ${limit}")
            st.progress(pct)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🧾 Recent Transactions")
    import pandas as pd
    data = {
        "Date": ["May 28","May 27","May 26","May 25","May 24","May 23"],
        "Description": ["Whole Foods","Netflix","Gas Station","Amazon","Salary","Restaurant"],
        "Category": ["Food","Entertainment","Transport","Shopping","Income","Food"],
        "Amount": ["-$87","-$15","-$54","-$129","+$4,210","-$62"],
        "Status": ["✅","✅","✅","⚠️ Over budget","✅","✅"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─── AI COACH CHAT ─────────────────────────────────────────────
elif page == "🤖 AI Coach Chat":
    st.markdown('<div class="hero-title">AI Finance Coach</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Ask anything. Get personalized, judgment-free financial guidance.</div>', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Hi! I'm your AI Finance Coach. I can see your spending patterns, savings goals, and financial health score.\n\nAsk me anything — budgeting, investing, debt payoff, or just 'how am I doing?' I'm here 24/7, judgment-free. 💚"}
        ]

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-bubble-ai">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col_input, col_btn = st.columns([5,1])
    with col_input:
        user_input = st.text_input("", placeholder="Ask your AI coach anything about your finances...", label_visibility="collapsed", key="chat_input")
    with col_btn:
        send = st.button("Send 💬")

    # Quick prompts
    st.markdown("**Quick Questions:**")
    qcols = st.columns(4)
    quick = ["How am I doing?", "How to save more?", "Start investing?", "Pay off debt faster?"]
    for i, (qc, q) in enumerate(zip(qcols, quick)):
        with qc:
            if st.button(q, key=f"q{i}"):
                user_input = q
                send = True

    if send and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # AI responses based on keywords
        responses = {
            "how am i doing": "📊 Based on your profile, you're doing **really well**!\n\n✅ Savings rate: **38%** (target is 20%+)\n✅ Emergency fund: **4 months** of expenses\n✅ No missed payments in 6 months\n⚠️ Food spending is 18% over budget this month\n\n**Overall score: 720/1000 — Great!** 🎉",
            "save more": "💡 Here are your top 3 saving opportunities:\n\n1. **Meal prep** — Save ~$234/month vs dining out\n2. **Cancel unused subscriptions** — Detected 2 unused (~$28/month)\n3. **Automate savings** — Set up $500 auto-transfer on payday\n\nTotal potential: **+$762/month** 🚀",
            "invest": "📈 Great time to start! Based on your $3,240/month savings:\n\n**Step 1:** Max out emergency fund to 6 months ✅ (almost there!)\n**Step 2:** Contribute to 401k up to employer match (free money!)\n**Step 3:** Open a Roth IRA — $500/month\n**Step 4:** Index funds (VOO/VTI) for long-term growth\n\nWith $500/month at 8% avg return = **$745,000 in 30 years** 🤯",
            "debt": "💪 Debt payoff strategy for you:\n\n**Avalanche Method** (saves most money):\n1. List all debts by interest rate\n2. Pay minimums on all\n3. Throw every extra dollar at highest-rate debt\n\nWith your current surplus of $3,240/month, you could be **debt-free in 18 months** if you allocate $1,500/month to debt payoff!",
        }
        
        reply = "Great question! Based on your financial data, I'd recommend focusing on your savings rate first. You're currently at 38% which is excellent — keep it up! Would you like me to dig deeper into any specific area? 💡"
        for key, val in responses.items():
            if any(word in user_input.lower() for word in key.split()):
                reply = val
                break
        
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

# ─── GOALS ─────────────────────────────────────────────────────
elif page == "🎯 Goals":
    st.markdown('<div class="hero-title">Financial Goals</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Define your future. Track your progress. Celebrate wins.</div>', unsafe_allow_html=True)

    import plotly.graph_objects as go

    goals = [
        {"name": "🏠 House Down Payment", "target": 50000, "saved": 24600, "monthly": 1000, "deadline": "Dec 2027"},
        {"name": "🚨 Emergency Fund",      "target": 25000, "saved": 20160, "monthly": 500,  "deadline": "Oct 2025"},
        {"name": "✈️ Europe Vacation",     "target": 5000,  "saved": 2100,  "monthly": 300,  "deadline": "Aug 2025"},
        {"name": "📚 Education Fund",      "target": 15000, "saved": 4500,  "monthly": 250,  "deadline": "Jan 2027"},
    ]

    cols = st.columns(2)
    for i, g in enumerate(goals):
        with cols[i % 2]:
            pct = g["saved"] / g["target"]
            months_left = int((g["target"] - g["saved"]) / g["monthly"])
            st.markdown(f"""
            <div class="section-card">
                <div style="font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:700;margin-bottom:0.5rem">{g['name']}</div>
                <div style="color:var(--muted);font-size:0.85rem;margin-bottom:0.8rem">Target: ${g['target']:,} • Deadline: {g['deadline']}</div>
            </div>""", unsafe_allow_html=True)
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=pct*100,
                number={"suffix": "%", "font": {"color": "#00C896", "size": 28}},
                gauge={
                    "axis": {"range": [0,100], "tickcolor": "#374151"},
                    "bar": {"color": "#00C896"},
                    "bgcolor": "#1F2937",
                    "borderwidth": 0,
                    "steps": [{"range": [0,100], "color": "#1F2937"}],
                    "threshold": {"line": {"color": "#FFD166", "width": 3}, "thickness": 0.75, "value": 75}
                }
            ))
            fig.update_layout(height=180, margin=dict(t=20,b=10,l=10,r=10),
                              paper_bgcolor="rgba(0,0,0,0)", font_color="#F9FAFB")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(f"**${g['saved']:,}** saved · **{months_left} months** to go at ${g['monthly']}/mo")

    st.markdown("---")
    st.markdown("### ➕ Add New Goal")
    c1, c2, c3 = st.columns(3)
    with c1: st.text_input("Goal Name", placeholder="e.g. New Car")
    with c2: st.number_input("Target Amount ($)", min_value=100)
    with c3: st.number_input("Monthly Contribution ($)", min_value=10)
    if st.button("Create Goal 🎯"):
        st.success("Goal created! Your AI coach will track your progress.")

# ─── INVESTMENTS ───────────────────────────────────────────────
elif page == "📈 Investments":
    st.markdown('<div class="hero-title">Investment Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Grow your wealth with AI-guided investment strategies.</div>', unsafe_allow_html=True)

    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go

    col1, col2, col3 = st.columns(3)
    for col, (val, lbl, chg, color) in zip([col1,col2,col3], [
        ("$18,240","Portfolio Value","↑ $1,240 (7.3%)","#00C896"),
        ("$2,400","Invested This Year","on track","#FFD166"),
        ("8.4%","Annual Return","vs 7.2% benchmark","#00C896"),
    ]):
        with col:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value" style="color:{color}">{val}</div>
                <div class="metric-label">{lbl}</div>
                <div style="color:{color};font-size:0.8rem;margin-top:0.3rem">{chg}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    ca, cb = st.columns([1,1])

    with ca:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🥧 Allocation")
        df = pd.DataFrame({"Asset": ["US Stocks (VOO)","Bonds","Intl Stocks","REIT","Cash"], "Value": [9800,3200,2800,1600,840]})
        fig = px.pie(df, values="Value", names="Asset", hole=0.55,
                     color_discrete_sequence=["#00C896","#FFD166","#06B6D4","#8B5CF6","#374151"],
                     template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=0,b=0))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cb:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 📅 Performance (12 months)")
        months = ["Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May"]
        vals = [14200,14800,14100,15200,15800,16100,15600,16500,17100,17400,17900,18240]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=months, y=vals, fill="tozeroy",
                                  fillcolor="rgba(0,200,150,0.1)",
                                  line=dict(color="#00C896", width=2.5)))
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           margin=dict(t=0,b=0), yaxis=dict(tickprefix="$"))
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🤖 AI Investment Recommendations")
    r1, r2, r3 = st.columns(3)
    recs = [
        ("📈 Increase Stock Allocation", "Your age profile suggests you can handle more equity. Moving from 54% → 65% stocks could add 1.2% annual return.", "High Impact"),
        ("🔁 Rebalance Portfolio", "Your REIT allocation has drifted to 8.8% (target: 10%). A small rebalance is recommended this month.", "Low Effort"),
        ("💸 Tax-Loss Harvest", "You have $320 in unrealized losses in international stocks — harvesting now saves ~$80 in taxes.", "Money Saver"),
    ]
    for col, (title, desc, badge) in zip([r1,r2,r3], recs):
        with col:
            st.markdown(f"""<div class="metric-card" style="text-align:left">
                <div style="font-family:'Syne',sans-serif;font-weight:700;margin-bottom:0.5rem">{title}</div>
                <div style="color:var(--muted);font-size:0.85rem;margin-bottom:0.8rem">{desc}</div>
                <span class="insight-chip">{badge}</span>
            </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─── BUSINESS PLAN ─────────────────────────────────────────────
elif page == "📋 Business Plan":
    st.markdown('<div class="hero-title">Business Plan & MVP Roadmap</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">FinanceAI Coach — Full Go-To-Market Strategy</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📌 Executive Summary", "📅 MVP Roadmap", "💰 Financials", "🚀 Tech Stack"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### 🎯 Mission
            > *"Make expert financial guidance accessible to every person on earth — regardless of income."*
            
            ### 🌍 Problem
            - **80%** of people live paycheck to paycheck
            - Financial advisors cost **$200–$400/hour**
            - Existing apps (Mint, YNAB) track — they don't **coach**
            - **Gen Z & Millennials** need money help, not spreadsheets
            
            ### 💡 Solution
            An AI-powered personal finance coach that:
            - Syncs with your bank automatically
            - Learns your spending personality
            - Gives proactive, personalized advice
            - Available 24/7 for less than a coffee/week
            """)
        with col2:
            st.markdown("""
            ### 📊 Market Opportunity
            | Segment | Size |
            |---------|------|
            | TAM (Global Fintech) | $340B |
            | SAM (Personal Finance Apps) | $8.5B |
            | SOM (Year 1 Target) | $2.4M ARR |
            
            ### 🏆 Competitive Edge
            | Feature | Us | Mint | YNAB |
            |---------|-----|------|------|
            | AI Coach Chat | ✅ | ❌ | ❌ |
            | Proactive Insights | ✅ | ❌ | ❌ |
            | Investment Advice | ✅ | ❌ | ❌ |
            | Goal AI | ✅ | Basic | Basic |
            | Price/month | $9.99 | Free | $14.99 |
            """)

    with tab2:
        st.markdown("### 🗓️ 12-Month MVP Roadmap")
        phases = [
            ("Phase 1 — Foundation", "Months 1–2", [
                "✅ Core dashboard (income, expenses, savings)",
                "✅ Manual transaction entry",
                "✅ Budget category tracking",
                "✅ Streamlit + GitHub deployment",
                "✅ User authentication (Streamlit secrets)",
            ], "#00C896"),
            ("Phase 2 — Intelligence", "Months 3–4", [
                "🔗 Plaid API bank sync integration",
                "🤖 Claude AI coach chat (Anthropic API)",
                "📊 Spending pattern analysis",
                "🔔 Smart alerts & push notifications",
                "📱 Mobile-responsive design",
            ], "#06B6D4"),
            ("Phase 3 — Growth", "Months 5–7", [
                "🎯 Goal tracking with AI projections",
                "📈 Investment portfolio tracker",
                "👥 Referral & invite system",
                "💳 Subscription billing (Stripe)",
                "📧 Weekly AI-generated email summaries",
            ], "#8B5CF6"),
            ("Phase 4 — Scale", "Months 8–12", [
                "🏢 Enterprise/employer wellness tier",
                "🌍 Multi-currency support",
                "📊 Tax optimization suggestions",
                "🤝 Bank & credit card partnerships",
                "📱 Native iOS/Android app launch",
            ], "#FFD166"),
        ]
        for name, timeline, items, color in phases:
            with st.expander(f"{name} — {timeline}", expanded=True):
                for item in items:
                    st.markdown(f"- {item}")
                st.markdown(f'<div style="color:{color};font-size:0.8rem;margin-top:0.5rem">● {timeline}</div>', unsafe_allow_html=True)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### 💸 Revenue Model
            | Stream | Price | Target Users |
            |--------|-------|-------------|
            | Freemium | $0 | 10,000 |
            | Pro Plan | $9.99/mo | 2,000 |
            | Premium | $19.99/mo | 500 |
            | Enterprise | $5/user/mo | 5 companies |
            
            ### 📈 Year 1 Projections
            | Metric | Target |
            |--------|--------|
            | Total Users | 12,500 |
            | Paid Users | 2,500 |
            | MRR (Month 12) | $28,000 |
            | ARR | $336,000 |
            | Churn Rate | < 5%/mo |
            """)
        with col2:
            st.markdown("""
            ### 🏗️ Cost Structure (Monthly)
            | Item | Cost |
            |------|------|
            | AI API (Anthropic/OpenAI) | $800 |
            | Plaid (Bank Sync) | $500 |
            | Streamlit Cloud / AWS | $200 |
            | Stripe Fees (~2.9%) | $400 |
            | Marketing | $1,500 |
            | **Total** | **$3,400** |
            
            ### 💰 Funding Strategy
            - **Bootstrap**: $0–$50K ARR (self-funded)
            - **Angel Round**: $250K at $2M valuation
            - **Seed**: $1.5M at 18 months (if traction)
            - **Series A**: $8M at 36 months
            """)

    with tab4:
        st.markdown("""
        ### ⚙️ Complete Tech Stack
        
        | Layer | Technology | Why |
        |-------|-----------|-----|
        | **Frontend** | Streamlit | Rapid deployment, Python-native |
        | **AI Engine** | Anthropic Claude API | Best-in-class financial reasoning |
        | **Bank Sync** | Plaid API | Industry standard, 12,000+ banks |
        | **Database** | Supabase (PostgreSQL) | Free tier, real-time, auth built-in |
        | **Payments** | Stripe | Subscription billing made easy |
        | **Deployment** | Streamlit Community Cloud | 1-click GitHub deploy |
        | **Charts** | Plotly | Interactive, beautiful |
        | **Auth** | Streamlit-Authenticator | Simple JWT auth |
        | **CI/CD** | GitHub Actions | Auto-deploy on push |
        | **Monitoring** | Sentry | Error tracking |
        
        ### 🚀 Deployment Steps (GitHub → Streamlit Cloud)
        ```bash
        # 1. Push to GitHub
        git init && git add . && git commit -m "Initial commit"
        git push origin main
        
        # 2. Go to share.streamlit.io
        # 3. Connect GitHub repo
        # 4. Set secrets in Streamlit dashboard:
        #    ANTHROPIC_API_KEY = "sk-..."
        #    PLAID_CLIENT_ID = "..."
        #    SUPABASE_URL = "..."
        
        # 5. Click Deploy — live in 2 minutes! 🎉
        ```
        """)
