# 📧 Email Sender Web App

A clean and modern Django-based web application to send emails through a responsive and user-friendly interface.

![Email Sender Banner](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=flat&logo=bootstrap)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## ✨ Features

- ✅ Simple and elegant email form inside a Bootstrap card
- ✅ AJAX-powered submission (no page reload)
- ✅ SweetAlert2 popup for success messages
- ✅ Responsive design — works across all devices
- ✅ Input validation and CSRF protected
- ✅ Neatly structured views and form handling

---

## 🖼️ UI Highlights

<div align="center">
  <img src="https://private-user-images.githubusercontent.com/110826217/466870588-0c7a738b-5a30-4a6b-9f42-aeac0561ea7b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI2NTEzMDQsIm5iZiI6MTc1MjY1MTAwNCwicGF0aCI6Ii8xMTA4MjYyMTcvNDY2ODcwNTg4LTBjN2E3MzhiLTVhMzAtNGE2Yi05ZjQyLWFlYWMwNTYxZWE3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxNlQwNzMwMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZDljMjI1MGUwNzcxOTA0Zjk1YmE4MTQzYjEyYjYzOTJhMzc5NmU2NTM1YzQwNDUwZDUxZWNiNDg3Zjg5NGNmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.64ygyHviN-LxaqNuC-fDxIl94jRJsWatH-uAWy4rcTM" alt="Email Sender UI" width="48%"/>
  <img src="https://private-user-images.githubusercontent.com/110826217/466920751-b11d6a52-ef1e-457c-b78e-38ca56e0dc1b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI2NTgzNzIsIm5iZiI6MTc1MjY1ODA3MiwicGF0aCI6Ii8xMTA4MjYyMTcvNDY2OTIwNzUxLWIxMWQ2YTUyLWVmMWUtNDU3Yy1iNzhlLTM4Y2E1NmUwZGMxYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxNlQwOTI3NTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wODU3MTlmNTQyYzZlZWU5MDQ0NzUxMGM2ZGRhNTZmN2ZiNGVkZGM1MWUzNzljZjM1YWE5MmNlZWVhZjVjNTY0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.txyejOOntJeowZp2U-bmxdoPgr2eaG7k59KGgeQ78wc" alt="Email Sender UI" width="48%"/>

  
</div>

- **Stylish Card Layout** using Bootstrap 5
- **Large Inputs & TextArea** for better usability
- **Custom SweetAlert2 Dialog** after sending email
- **Responsive design** with padding and alignment

---

## 🛠️ Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript, AJAX |
| **Backend**  | Django, Python 3     |
| **Alerts**   | SweetAlert2          |
| **Database** | SQLite / PostgreSQL  |

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/email-sender-django.git
   cd email-sender-django
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure your email backend in settings.py

python
Copy
Edit
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
Run the server

bash
Copy
Edit
python manage.py runserver
Navigate to:

arduino
Copy
Edit
http://127.0.0.1:8000/email_send/
📩 Sample Screenshot
<div align="center"> <img src="https://private-user-images.githubusercontent.com/110826217/466870588-0c7a738b-5a30-4a6b-9f42-aeac0561ea7b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI2NTEzMDQsIm5iZiI6MTc1MjY1MTAwNCwicGF0aCI6Ii8xMTA4MjYyMTcvNDY2ODcwNTg4LTBjN2E3MzhiLTVhMzAtNGE2Yi05ZjQyLWFlYWMwNTYxZWE3Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxNlQwNzMwMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZDljMjI1MGUwNzcxOTA0Zjk1YmE4MTQzYjEyYjYzOTJhMzc5NmU2NTM1YzQwNDUwZDUxZWNiNDg3Zjg5NGNmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.64ygyHviN-LxaqNuC-fDxIl94jRJsWatH-uAWy4rcTM" alt="Email Form Screenshot" width="700"/> </div>
🤝 Contributing
Pull requests are welcome! Feel free to submit improvements, report bugs, or suggest features.



📬 Contact
Author: Haripriya C
📧 Email: haripriyaece123@gmail.com

