# 🚀 Project Name
AIDEL-AI-MAVERICKS
## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Our project focuses on AI-driven financial risk assessment for transaction analysis. It aims to automate risk evaluation by analyzing transaction details and generating structured risk insights.

Financial institutions struggle with manual risk assessments, leading to delays, inconsistencies, and potential fraud exposure. Our AI model efficiently processes transaction data, evaluates risk factors using authoritative sources, and delivers accurate, real-time risk scores in a structured JSON format.

By leveraging AI, we enhance fraud detection, regulatory compliance, and financial security, ensuring faster, more reliable decision-making in the financial sector. 

## 🎥 Demo
Demo videos are uploaded in test folder along with data used in the demo

🖼️ Screenshots:

![Screenshot 1](link-to-image)



## ⚙️ What It Does
Key Features & Functionalities of the AI-Powered Financial Risk Assessment
Our AI-driven financial risk assessment system offers a structured, automated approach to evaluating transaction risks. Here are its core features:

1. Risk Scoring & Confidence Assessment
Assigns a Risk Score (0-1) based on sender, receiver, and intermediaries.

Computes a Confidence Score (0-1) based on the reliability and credibility of sources.

2. Data-Driven Risk Evaluation
Extracts entities from the transaction (e.g., individuals, corporations, shell companies).

Analyzes fraud history, financial instability, regulatory violations, and sanctions.

Considers VPN usage, transaction locations, and intermediaries for enhanced risk detection.

3. Source-Based Evidence & Justification
Uses authoritative financial reports, regulatory filings, and crime databases to support assessments.

Only includes relevant sources that impact the risk score (e.g., OpenCorporates, SEC Edgar, OFAC Sanctions List).

4. Adaptive Risk Calculation
Weighted risk formula:

Sender Risk (50%)

Receiver Risk (30%)

Intermediary Risk (20%) (if applicable, otherwise balanced equally between sender & receiver)

5. Automated & Structured JSON Output
Generates machine-readable JSON with risk insights.

Ensures consistency and compliance for financial institutions.

This system enhances fraud detection, reduces manual workload, and accelerates financial decision-making, making risk assessment more efficient, reliable, and scalable.

## 🛠️ How We Built It
Technologies/Frameworks Used:
Python 3.12
llama-3.3-70b-versatile
Groq API Client

## 🏃 How to Run
Python 3.12.x is required.
Run the below to install dependencies:
pip3 install groq
pip3 install fastapi
pip3 install uvicorn

To start the app run the below command :
uvicorn risk_analysis_api:app --host 0.0.0.0 --port 8000 --reload
