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
  <img src="https://github.com/Priyahari123/DjangoMailer/issues/1#issue-3234823165" alt="Email Sender UI" width="700"/>

  
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
<div align="center"> <img src="https://github.com/Priyahari123/DjangoMailer/issues/1#issue-3234823165" alt="Email Form Screenshot" width="700"/> </div>
🤝 Contributing
Pull requests are welcome! Feel free to submit improvements, report bugs, or suggest features.



📬 Contact
Author: Haripriya C
📧 Email: haripriyaece123@gmail.com

