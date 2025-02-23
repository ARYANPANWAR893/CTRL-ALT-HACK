# 🚀 Vaibhav ID - AI-Powered Healthcare & Financial System

## 📌 Overview
Vaibhav ID is a **decentralized healthcare and financial platform** that securely manages user health records, analyzes fitness data, and integrates AI-generated health reports for doctors and insurance assessors. Built with **Flask**, **SQLAlchemy**, **Gemini AI**, and **Tailwind CSS**, this project ensures **data privacy**, **security**, and **user-friendly accessibility**.

## 🏗️ Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Database:** SQLite (default), PostgreSQL (optional)
- **AI Integration:** Gemini AI API
- **Blockchain:** Custom-built using Python

## 🔹 Features
### 1️⃣ **User Management**
- Secure **signup, login, and logout**
- Store and retrieve user **personal & medical data**
- Blockchain-based **"Vaibhav Code"** generation for data security

### 2️⃣ **Health & Expense Tracking**
- **Gym Tracker:** Log exercises, sets, reps, and duration
- **Calorie Tracker:** Track daily food intake and calories
- **Expense Manager:** Record transactions from GPay, Paytm, PayPal, and cash
- **Groups:** Split expenses with friends and family

### 3️⃣ **AI-Powered Health Analysis**
- Uses **Gemini AI** to generate:
  - **Doctor’s Report:** Summarizes medical risks and lifestyle suggestions
  - **Insurance Report:** Assesses health risks for insurance purposes
- **Graphical Representation** of health logs

### 4️⃣ **Secure Report Storage & Sharing**
- Upload medical reports with user and uploader tracking
- Fetch reports with metadata (uploader info, date, recipient)
- Secure **access requests** to another user's medical history

## 🔧 Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/VaibhavID.git
   cd VaibhavID
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask App:**
   ```sh
   python main.py
   ```

5. **Access the Web App:**  
   Open your browser and visit:  
   👉 `http://127.0.0.1:5000/`

## 📊 Health Report API Endpoint
### **Request:**
```http
GET /generate_health_report/<user_id>
```

### **Response Example:**
```json
{
  "health_report": "**Medical Condition Summary:** Aryan's height and weight indicate that he is overweight for his age. His excessive calorie intake and unhealthy habits (alcohol and smoking) pose risks to his long-term health.\n\n**Potential Risks:** Obesity, cardiovascular disease, respiratory issues, developmental impairments, psychosocial problems.\n\n**Lifestyle Suggestions:** Reduce calorie intake, increase physical activity (focus on football), cease alcohol and smoking habits, improve nutrition by consuming healthy foods, consult healthcare professionals for guidance and support."
}
```

## 🖥️ Frontend - Displaying AI Health Report
The report is dynamically loaded using **Tailwind CSS** and JavaScript:
```html
<p id="loadingText" class="text-gray-600 text-center animate-pulse">⏳ Generating patient analysis...</p>
<div id="report" class="hidden mt-4 text-gray-700 leading-relaxed"></div>
```

JavaScript fetches the API and displays formatted content:
```js
async function fetchHealthReport() {
    const response = await fetch('/generate_health_report/1');
    const data = await response.json();
    document.getElementById("loadingText").classList.add("hidden");
    document.getElementById("report").innerHTML = formatReport(data.health_report);
    document.getElementById("report").classList.remove("hidden");
}
```

## 🛠️ Future Enhancements
🔹 AI-powered **disease prediction** based on historical data  
🔹 **Automated credit scoring** from financial transactions  
🔹 More **blockchain integration** for decentralized security  
🔹 **User-friendly mobile app** version  

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

---
🚀 **Vaibhav ID** - Secure, AI-Powered Healthcare & Finance for the Future! 🔥

