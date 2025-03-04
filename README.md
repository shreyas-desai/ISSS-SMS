# ISSS-SMS 📢  
*A Scalable Student Management System for ISSS at Stevens Institute of Technology*  

## 🚀 Overview  
ISSS-SMS is a robust **Student Management System** designed for **International Student and Scholar Services (ISSS)** at **Stevens Institute of Technology**. The platform streamlines administrative workflows, automates real-time student data synchronization, and enhances security and compliance.  

Built with **FastAPI** and **Django** on the backend and a **React-based** frontend, this system optimizes student record handling, F-1/J-1 visa processing, and batch data updates, ensuring an efficient and scalable solution for ISSS operations.  

## 🛠️ Tech Stack  
### Backend:
- **FastAPI** & **Django** - High-performance API development  
- **PostgreSQL & Microsoft SQL Server** - Secure and efficient database management  
- **JWT Authentication & MFA** - Ensuring secure access control

### Frontend:
- **React** - Interactive and user-friendly UI  
- **AJAX & Web Services (SOA)** - Enabling seamless data exchange  

### Infrastructure & Observability:
- **AWS (EC2, S3, API Gateway, Lambda)** - Scalable cloud hosting  


## ✨ Features  
✅ **Automated Student Data Sync** - Batch processing & real-time updates for F-1/J-1 visa records  
✅ **Secure Access & Authentication** - MFA & Role-Based Access Control (RBAC)  
✅ **Interactive UI** - Streamlined student workflows with an intuitive React-based frontend

## 📦 Installation & Setup  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/shreyas-desai/ISSS-SMS.git
   cd ISSS-SMS
   ```

2. **Backend Setup:**  
   ```sh
   pip install -r requirements.txt
   uvicorn app:main --reload
   ```

3. **Frontend Setup:**  
   ```sh
   cd frontend
   npm install
   npm start
   ```

4. **Environment Variables:**  
   Set up `.env` file for database credentials, JWT secrets, and API keys.

## 📖 Usage  
- **Admin Dashboard:** Manage student records, process visa requests, and monitor system activity.  
- **Student Portal:** Students can update their information, check visa status, and receive notifications.  
- **API Endpoints:** RESTful APIs to fetch, update, and validate student data.  

## 📜 License  
This project is licensed under the **MIT License**.  

## 📬 Contact  
👤 **Shreyas Desai**  
📧 [sdesai33@stevens.edu](mailto:sdesai33@stevens.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/shreyas-desai/)  
