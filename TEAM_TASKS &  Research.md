# 🚀 Batch Monitoring Project - Team Tasks

> **What is this?** Simple instructions for each team member about what to build/research.
> **How to use?** Pick your task, read the "What to do" section, deliver what it asks.

---

## 📋 Quick Navigation

- [Research Tasks (Learn how things work)](#-research-tasks-learn-how-things-work)
- [Coding Tasks (Write actual code)](#-coding-tasks-write-actual-code)
- [Testing Tasks (Make sure it works)](#-testing-tasks-make-sure-it-works)
- [Documentation Tasks (Write guides)](#-documentation-tasks-write-guides)
- [Deployment Tasks (Put it on cloud)](#-deployment-tasks-put-it-on-cloud-for-everyone-to-see)
- [Stretch Tasks (Optional extras)](#-stretch-tasks-if-you-finish-early)

---

# 🔬 RESEARCH TASKS (Learn how things work)

## 📌 R1: Study Autosys Job Scheduler

**What to do:** Find out how to check batch job status in Autosys system

**You need to answer:**
- Does Autosys have a web API or do we use command line?
- What command shows failed jobs? (Example: `autorep -J ALL -d`)
- What does the output look like? (Copy-paste example)
- How do we login? (Username/password?)

**What to deliver:** `docs/research/autosys_research.md`

**Time:** 1-2 hours

---

## 📌 R2: Study Openlink Log Files

**What to do:** Understand how Openlink App Manager writes logs

**You need to answer:**
- Where are log files stored? (File path)
- How are log files named? (Example: `batch_name_2025-01-15.log`)
- How do we know a batch FAILED? (Look for ERROR, FAIL, EXIT CODE 1)
- What's the date/time format in logs?

**What to deliver:** `docs/research/openlink_logs_research.md`

**Time:** 1-2 hours

---

## 📌 R3: Study ServiceNow API

**What to do:** Learn how to update ServiceNow incidents using Python

**You need to answer:**
- What is the API web address? (Example: `https://company.service-now.com/api/now/table/incident`)
- How do we login? (Username/password or token?)
- How to find existing incident by batch name?
- How to ADD a note without creating a new incident?

**What to deliver:** `docs/research/servicenow_research.md` (Include Python code example)

**Time:** 1-2 hours

---

## 📌 R4: Study Azure OpenAI (GPT-4o)

**What to do:** Figure out how to send logs to AI and get a summary back

**Steps to follow:**
1. Create free Azure account
2. Search "Azure OpenAI" in portal
3. Request access to GPT-4o model
4. Get API key and endpoint URL
5. Test with this prompt:

> "You are a Senior SRE. You will receive a raw error log. Produce ONE sentence, max 20 words. Tell what failed and why."

**What to deliver:** `docs/research/azure_openai_research.md` (Include working Python code + screenshot)

**Time:** 2 hours

---

## 📌 R5: Study Teams Adaptive Cards

**What to do:** Design message cards with buttons for Microsoft Teams

**You need to create two card designs:**

**Card 1 - L1 Approval Card (Shows to L1 operator)**
```
🔍 L1 VALIDATION REQUIRED
Batch: EOD_PRICE_OL
System: Openlink
Failure: DB connection pool exhausted

[APPROVE] [ESCALATE] [FALSE POSITIVE]
```

**Card 2 - L2 Alert Card (Shows to L2 engineer)**
```
🚨 BATCH FAILURE ALERT
Batch: EOD_PRICE_OL
AI Diagnosis: DB connection pool exhausted
Full log: [Click to view]
```

**What to deliver:**
- `docs/research/teams_cards_research.md` (How to send cards + JSON code)
- `docs/research/l1_card.json` (JSON for first card)
- `docs/research/l2_card.json` (JSON for second card)

**Time:** 2 hours

---

## 📌 R6: Study Power Automate Approvals

**What to do:** Design workflow that sends approval and waits 5 minutes

**The workflow must:**
1. Receive trigger from Python
2. Send Teams card to L1 with buttons
3. Wait 5 minutes for response
4. If approved → call L2 notification
5. If no response in 5 minutes → auto-escalate to L2

**What to deliver:** `docs/research/power_automate_research.md` (Flow diagram + step-by-step setup guide)

**Time:** 2 hours

---

## 📌 R7: Study Power BI Dashboard

**What to do:** Design dashboard showing batch health metrics

**You need these charts:**
1. **Average response time** - How fast L2 gets notified (target: <5 min)
2. **Failure rate** - How many batches fail per day
3. **L1 response speed** - How fast L1 clicks Approve
4. **Failures by system** - Pie chart (Openlink vs Autosys vs Feed vs DB)
5. **Top failing batches** - Table showing worst batches

**What to deliver:** `docs/research/power_bi_research.md` (Hand-drawn dashboard sketch + list of charts + sample DAX formula)

**Time:** 2 hours

---

# 💻 CODING TASKS (Write actual code)

## 📌 C1: Build Mock Log Generator

**What to do:** Create Python script that makes fake log files for testing

**You need to create these 8 failure patterns:**

| # | Failure Type | What the log looks like |
|---|---|---|
| 1 | Database error | `ORA-12541: TNS:no listener` |
| 2 | Connection pool full | `connection pool exhausted, max 20 connections` |
| 3 | Timeout | `timeout after 300 seconds` |
| 4 | File missing | `file not found: /data/input.csv` |
| 5 | Permission denied | `permission denied: /logs/access` |
| 6 | Out of memory | `java.lang.OutOfMemoryError` |
| 7 | Database deadlock | `deadlock detected when updating table` |
| 8 | Null pointer | `NullPointerException at line 42` |

**The script should:**
- Generate 100 log lines
- 80 lines = success, 20 lines = failures (mix of above 8 types)
- Save to `simulation/sample_logs/` folder
- Create separate files: `openlink.log`, `autosys.log`, `feed.log`, `db.log`

**What to deliver:** Update `simulation/log_generator.py`

**Time:** 4 hours

---

## 📌 C2: Write Regex Fallback (AI Backup)

**What to do:** Create function that detects failures without AI (used when AI is down)

**How it works:**
```
Input:  "ORA-12541: TNS:no listener. Connection refused."
Output: "[REGEX-FALLBACK] Oracle DB connection error detected"
```

**You need to map:**

| Pattern | Output Message |
|---|---|
| `ORA-` | Database connection error |
| `connection pool exhausted` | Connection pool full |
| `timeout` | Operation timed out |
| `file not found` | Input file missing |
| `permission denied` | Permissions error |
| `out of memory` | Memory exhaustion |
| `deadlock` | Database deadlock detected |
| `null pointer` | Null reference error |
| No match | Root cause unclear — review log |

**What to deliver:** Update `agents/ai_enrichment.py` (add `regex_fallback_summary()` function) + Update `tests/test_ai_enrichment.py` (add 8 test cases)

**Time:** 3 hours

---

## 📌 C3: Build Health Check Watchdog

**What to do:** Create monitor that alerts if main agent stops working

**How it works:**
```
Every 60 seconds:  Main agent says "I'm alive"
Watchdog checks:   "When was last 'I'm alive'?"
If > 180 seconds:  Send alert to operations team
```

**What to deliver:** Create `utils/health_check.py` with Watchdog class + Update `main.py` to use it + Create `tests/test_health_check.py`

**Time:** 3 hours

---

## 📌 C4: Environment Tag Validation

**What to do:** Prevent DEV alerts from going to PROD (very important!)

**Rules:**
- Every batch event must have `environment = "DEV"` or `"UAT"` or `"PROD"`
- Before sending anywhere, check: event environment matches config environment
- If mismatch → RAISE ERROR, DO NOT SEND

**Example:**
```python
def send_to_teams(event, config):
    if event['environment'] != config['environment']:
        raise Exception(f"WRONG ENVIRONMENT! Event={event['environment']}, Config={config['environment']}")
    # Now it's safe to send
```

**What to deliver:** Update ALL 7 agent files (`teams_notifier.py`, `servicenow_agent.py`, etc.) + Create `tests/test_env_isolation.py`

**Time:** 3 hours

---

# 🧪 TESTING TASKS (Make sure it works)

## 📌 T1: Write 10 Gate Tests

**What to do:** Create automated tests for each requirement

**The 10 tests:**

| Test # | What to test | How to test |
|---|---|---|
| G1 | All 4 collectors run 24 hours without crash | Run them for 24 hours in test mode |
| G2 | Classification accuracy >98% | Feed 100 failures, check 98 correct |
| G3 | AI summary ≤20 words | Check length of AI output |
| G4 | L1 card delivers in <10 seconds | Measure time from trigger to arrival |
| G5 | Auto-escalate at exactly 5 minutes | Wait 5 minutes, check escalation |
| G6 | L2 gets alert <5 sec after approval | Measure time after Approve button |
| G7 | ServiceNow never creates duplicate incident | Run 10 alerts, count incidents created (should be 0 new) |
| G8 | One source down, others still work | Turn off Openlink, check Autosys still works |
| G9 | DEV never reaches PROD | Send DEV alert, check PROD channel empty |
| G10 | Dashboard shows correct data | Compare dashboard numbers with database |

**What to deliver:** Create folder `tests/gates/` with 10 test files (`g1_test.py`, `g2_test.py`, etc.)

**Time:** 5 hours

---

## 📌 T2: Test Failure Scenarios (Chaos Testing)

**What to do:** Test what happens when things break

**Test these scenarios:**

| What breaks | What you do | Expected behavior |
|---|---|---|
| AI goes down | Disable internet or use wrong API key | System uses regex fallback, doesn't crash |
| Power Automate down | Use fake webhook URL | Skip L1, send directly to L2 |
| ServiceNow down | Use wrong credentials | Log error, continue working |
| Database down | Use wrong connection string | Retry 3 times, then log failure |
| Log format changes | Send corrupted log | Flag as `[PARSE_ERROR]`, send raw log |
| Network is slow | Add 10 second delay | Retry with backoff, don't crash |

**What to deliver:** Create folder `tests/resilience/` with 6 test files (`test_ai_down.py`, `test_power_automate_down.py`, etc.)

**Time:** 4 hours

---

# 📝 DOCUMENTATION TASKS (Write guides)

## 📌 D1: Write L1 Training Guide

**What to do:** Create simple guide for L1 operators (non-technical people)

**What to include:**

**Page 1: What changed**
```
BEFORE: You spent 15 minutes copying logs from 4 systems
NOW:    You spend 30 seconds clicking ONE button
```

**Page 2: The 3 buttons**
```
✅ APPROVE        - Alert looks correct, send to L2
⚠️ ESCALATE       - This is urgent, mark as P1
❌ FALSE POSITIVE  - This alert is wrong, dismiss it
```

**Page 3: What if you don't respond?**
```
After 5 minutes → System automatically sends to L2
You're busy? No problem. SLA is still protected.
```

**Page 4: Your new role**
```
You are now a QUALITY GATE, not a data fetcher.
You catch AI mistakes. You escalate real emergencies.
This is a promotion, not a reduction.
```

**What to deliver:** `docs/L1_TRAINING_GUIDE.md` + `docs/L1_QUICK_REFERENCE.pdf` (1 page cheat sheet)

**Time:** 2 hours

---

## 📌 D2: Create Discovery Checklist for Client (Citi)

**What to do:** Create checklist of 8 things we need from client before going to production

**The 8 questions:**

| # | Question | Who to ask | Status |
|---|---|---|---|
| 1 | Where are Openlink log files? (DEV, UAT, PROD paths) | Openlink Admin | ⬜ |
| 2 | What Autosys version? Does it have API? | Autosys Admin | ⬜ |
| 3 | Can we get read-only database credentials? | DBA | ⬜ |
| 4 | ServiceNow API endpoint and auth method? | SNOW Admin | ⬜ |
| 5 | Teams webhook URL for L2 alerts? | M365 Admin | ⬜ |
| 6 | How to request firewall whitelist? | Network Security | ⬜ |
| 7 | Who owns Azure OpenAI subscription? | Cloud Team | ⬜ |
| 8 | Is Power Automate already licensed? | M365 Admin | ⬜ |

**What to deliver:** `docs/DISCOVERY_CHECKLIST.md` (Table format with columns: Question, Owner, Contact Email, Status, Date Resolved)

**Time:** 1 hour

---

## 📌 D3: Write Configuration Guide

**What to do:** Document all settings and secrets needed to run the project

**What to include:**

**Section 1: Environment variables needed**
```bash
AZURE_OPENAI_ENDPOINT=https://citi-openai.openai.azure.com/
AZURE_OPENAI_KEY=abc123...
SERVICENOW_INSTANCE=citi.service-now.com
SERVICENOW_USER=svc_batch_monitor
SERVICENOW_PASSWORD=xxx
TEAMS_L2_WEBHOOK=https://.../webhook
```

**Section 2: Config files**
- `config/dev.yaml` - DEV environment settings
- `config/uat.yaml` - UAT environment settings
- `config/prod.yaml` - PROD environment settings

**Section 3: How to add a new batch system**
Step-by-step instructions

**What to deliver:** Update `docs/CONFIGURATION_GUIDE.md` + Update `.env.example` if needed

**Time:** 2 hours

---

# ☁️ DEPLOYMENT TASKS (Put it on cloud for everyone to see)

## 📌 DEP1: Deploy to AWS Free Tier

**What to do:** Put the batch monitoring system on AWS so everyone can access it

**AWS Free Tier includes (12 months free):**
- EC2 server: 750 hours/month free (1 server running 24/7 = 720 hours, fits in free tier)
- 30GB storage free

**Step 1: Create AWS Account**

Go to https://aws.amazon.com → Click "Create an AWS Account" → Choose "Basic Support" (free)

**Step 2: Launch EC2 Server (Ubuntu)**
```
1. Search "EC2" in AWS console
2. Click "Launch Instance"
3. Name: "batch-monitoring-server"
4. Choose Ubuntu 22.04 (free tier eligible)
5. Instance type: t2.micro (free tier)
6. Key pair: Create new "batch-monitoring-key" (download .pem file)
7. Network settings: Allow HTTP, HTTPS, SSH from anywhere
8. Storage: 20GB (free tier includes 30GB)
9. Click "Launch Instance"
```

**Step 3: Connect to your server**
```bash
chmod 400 batch-monitoring-key.pem
ssh -i batch-monitoring-key.pem ubuntu@<your-server-public-ip>
```

**Step 4: Install required software on server**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y
sudo apt install git -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install nginx -y
```

**Step 5: Deploy your code**
```bash
git clone https://github.com/AI-Commodities/Batch-monitoring.git
cd Batch-monitoring
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
nano .env

sudo -u postgres psql
# CREATE DATABASE batch_monitoring;
# CREATE USER batch_user WITH PASSWORD 'your_password';
# GRANT ALL PRIVILEGES ON DATABASE batch_monitoring TO batch_user;
# \q

python3 setup_db.py
```

**Step 6: Run the application**
```bash
python3 main.py

sudo apt install screen -y
screen -S batch-monitor
python3 main.py
# Press Ctrl+A then D to detach
# To reattach: screen -r batch-monitor
```

**Step 7: Set up web dashboard**
```bash
sudo cp Batchmonitoring.html /var/www/html/
sudo systemctl start nginx
sudo systemctl enable nginx
# Dashboard at: http://<your-server-public-ip>/Batchmonitoring.html
```

**Step 8: Set up auto-start on boot**
```bash
sudo nano /etc/systemd/system/batch-monitor.service
```
```ini
[Unit]
Description=Batch Monitoring Agent
After=network.target postgresql.service

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/Batch-monitoring
ExecStart=/home/ubuntu/Batch-monitoring/venv/bin/python3 /home/ubuntu/Batch-monitoring/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl enable batch-monitor.service
sudo systemctl start batch-monitor.service
sudo systemctl status batch-monitor.service
```

**Step 9: Add health check endpoint**
```python
@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}
```

**What to deliver:** `docs/DEPLOYMENT_AWS.md` (Step-by-step guide with screenshots) + Live URL where dashboard is running

**Time:** 4 hours

---

## 📌 DEP2: Deploy to Azure Free Tier (Alternative)

**What to do:** Put the batch monitoring system on Azure (alternative to AWS)

**Azure Free Tier includes:**
- 750 hours of B1S virtual machine
- 64GB storage free
- 12 months free + $200 credit for first 30 days

**Step 1: Create Azure Account**

Go to https://azure.microsoft.com/free → Click "Start free"

**Step 2: Create Virtual Machine**
```
1. Search "Virtual Machines" in portal
2. Click "Create" → "Azure virtual machine"
3. Resource group: Create new "batch-monitoring-rg"
4. VM name: "batch-monitoring-vm"
5. Region: Pick closest to you
6. Image: Ubuntu 22.04 LTS
7. Size: Standard B1s (free tier)
8. Username: azureuser
9. SSH public key: Generate or paste your key
10. Public inbound ports: SSH (22), HTTP (80), HTTPS (443)
11. Click "Review + Create"
```

**Step 3: Connect and deploy**

Follow same steps as AWS from Step 3 onwards.

**What to deliver:** `docs/DEPLOYMENT_AZURE.md` (Step-by-step guide with screenshots) + Live URL where dashboard is running

**Time:** 4 hours

---

## 📌 DEP3: Deploy Using Docker (Easiest for consistency)

**What to do:** Package the application in Docker so it runs anywhere

**Step 1: Create Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "main.py"]
```

**Step 2: Create docker-compose.yml**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/batch_monitoring
      - AZURE_OPENAI_ENDPOINT=${AZURE_OPENAI_ENDPOINT}
      - AZURE_OPENAI_KEY=${AZURE_OPENAI_KEY}
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=batch_monitoring
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./Batchmonitoring.html:/usr/share/nginx/html/index.html
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - app

volumes:
  postgres_data:
```

**Step 3: Build and run locally**
```bash
docker build -t batch-monitor .
docker-compose up -d
docker-compose logs -f app
docker-compose down
```

**Step 4: Push to Docker Hub**
```bash
docker login
docker tag batch-monitor yourusername/batch-monitor:latest
docker push yourusername/batch-monitor:latest
```

**Step 5: Deploy to any cloud using Docker**
```bash
docker run -d \
  --name batch-monitor \
  -p 8000:8000 \
  -e AZURE_OPENAI_ENDPOINT="your_endpoint" \
  -e AZURE_OPENAI_KEY="your_key" \
  yourusername/batch-monitor:latest
```

**What to deliver:** `Dockerfile` + `docker-compose.yml` + `docs/DEPLOYMENT_DOCKER.md`

**Time:** 3 hours

---

## 📌 DEP4: Set Up Free Monitoring (Uptime Robot)

**What to do:** Make sure your deployed app stays online and alerts you if it goes down

**Uptime Robot Free Tier:** 50 monitors, 5 minute check intervals, email alerts

**Step 1:** Go to https://uptimerobot.com and sign up for free

**Step 2: Add your dashboard to monitor**
```
1. Click "Add New Monitor"
2. Monitor Type: HTTP(S)
3. Friendly Name: "Batch Monitoring Dashboard"
4. URL: http://your-server-ip/Batchmonitoring.html
5. Monitoring Interval: 5 minutes
6. Click "Create Monitor"
```

**Step 3: Add API endpoint monitor**
```
URL: http://your-server-ip:8000/health
Friendly Name: "Batch Monitoring API"
```

**Step 4: Set up alert contacts**
```
1. Go to "Alert Contacts"
2. Add your email
3. Configure when to alert (down for 5+ minutes)
```

**What to deliver:** `docs/MONITORING_SETUP.md` (Screenshots + URLs being monitored)

**Time:** 1 hour

---

## 📌 DEP5: Quick Public URL Using Ngrok (For demos)

**What to do:** Expose your local server to internet instantly (for quick demos)

**Step 1: Install ngrok**
```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
# Or on Mac: brew install ngrok
```

**Step 2: Get free auth token**

Go to https://ngrok.com → Sign up → Copy auth token → Run:
```bash
./ngrok config add-authtoken YOUR_TOKEN
```

**Step 3: Expose your local server**
```bash
./ngrok http 8000
# You'll get a public URL like: https://abc123.ngrok.io
```

**Limitations (free tier):** URL changes each time you restart, limited to 40 connections/minute. Good for demos, not production.

**What to deliver:** `docs/NGROK_SETUP.md`

**Time:** 30 minutes

---

# 🚀 STRETCH TASKS (If you finish early)

## 📌 S1: Predictive Alerting (Phase 3 Feature)

**What to do:** Detect batches that will fail BEFORE they actually fail

**How it works:**
```
Normal range = average runtime + (1.5 × standard deviation)
If current runtime > normal range → send alert
```

> **Important:** Use lightweight statistical model only. Do NOT use neural networks or complex ML.

**What to deliver:** Create folder `experimental/anomaly_detection/` + `anomaly_detection.py` + Jupyter notebook showing the math

**Time:** 5 hours

---

## 📌 S2: Live Web Dashboard with Real-time Updates

**What to do:** Make `Batchmonitoring.html` show live data (auto-refresh every 10 seconds)

**Add API endpoint in main.py:**
```python
@app.get("/api/failures")
def get_failures():
    return {"failures": current_failures, "pending": pending_approvals}
```

**Update HTML with JavaScript:**
```javascript
setInterval(() => {
    fetch('/api/failures')
        .then(response => response.json())
        .then(data => updateDashboard(data));
}, 10000);
```

**What to deliver:** Update `Batchmonitoring.html` + Add API endpoints in `main.py`

**Time:** 4 hours

---

## 📌 S3: CI/CD Pipeline (GitHub Actions)

**What to do:** Automatically run tests and deploy when code changes

**What to deliver:** Create `.github/workflows/deploy.yml`
```yaml
name: Test and Deploy

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest tests/

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server
        run: |
          ssh ubuntu@your-server "cd Batch-monitoring && git pull && sudo systemctl restart batch-monitor"
```

**Time:** 3 hours

---

# ✅ COMPLETION CHECKLIST

### Research Tasks
- [ ] R1: Autosys research done
- [ ] R2: Openlink logs research done
- [ ] R3: ServiceNow API research done
- [ ] R4: Azure OpenAI research done
- [ ] R5: Teams cards research done
- [ ] R6: Power Automate research done
- [ ] R7: Power BI research done

### Coding Tasks
- [ ] C1: Mock log generator works (creates 8 failure types)
- [ ] C2: Regex fallback function works (all 8 patterns)
- [ ] C3: Health check watchdog works (alerts after 3 minutes)
- [ ] C4: Environment validation works (DEV/PROD never mix)

### Testing Tasks
- [ ] T1: 10 gate tests written and passing
- [ ] T2: 6 resilience tests written and passing

### Documentation Tasks
- [ ] D1: L1 training guide complete
- [ ] D2: Discovery checklist ready for client
- [ ] D3: Configuration guide complete

### Deployment Tasks (Pick at least ONE)
- [ ] DEP1: Deployed to AWS free tier (URL: _____________)
- [ ] DEP2: Deployed to Azure free tier (URL: _____________)
- [ ] DEP3: Docker container working (pushed to Docker Hub)
- [ ] DEP4: Uptime monitoring set up
- [ ] DEP5: Ngrok setup documented (for quick demos)

### Stretch Tasks (Optional)
- [ ] S1: Predictive alerting prototype
- [ ] S2: Live web dashboard with real-time updates
- [ ] S3: CI/CD pipeline with GitHub Actions

---

# 🎯 QUICK START - WHAT EACH PERSON DOES

| Person | Tasks |
|---|---|
| **Person 1** (Lead/Architect) | R1, C3, DEP1 or DEP2, S3 |
| **Person 2** (Backend Developer) | R3, R4, C2, C4 |
| **Person 3** (Data/Collectors) | R2, C1, T1, T2 |
| **Person 4** (Frontend/UI) | R5, R6, R7, D1, S2 |
| **Person 5** (Documentation/BA) | D2, D3, DEP3, DEP5 |
| **Person 6** (DevOps/Deployment) | DEP1, DEP2, DEP4, S1 |

---

# 📞 NEED HELP?

If stuck:
1. Check the HCL document (section numbers mentioned above)
2. Ask in team chat
3. Google the error message
4. Document what you tried and ask for help

---

*Last Updated: May 2025 | Status: Active — Pick your tasks and start!*
