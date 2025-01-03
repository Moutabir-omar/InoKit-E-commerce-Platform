# InoKit E-commerce Platform

[![License](https://img.shields.io/badge/License-Custom-blue.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-purple.svg)](https://getbootstrap.com/)

## 🚀 About InoKit

InoKit is a modern e-commerce platform specializing in electronic components and accessories. Built with Django and Bootstrap, it offers a seamless shopping experience with a beautiful, responsive interface.

**Author:** Omar Moutabir  
**Contact:** omar.moutabir@gmail.com

## ✨ Features

- 🛍️ **Product Management**
  - Detailed product listings with images and descriptions
  - Category-based organization
  - Advanced search functionality

- 🛒 **Shopping Experience**
  - User-friendly cart system
  - Secure checkout process
  - Order tracking

- 👤 **User Management**
  - User registration and authentication
  - Profile management
  - Order history

- 💬 **Customer Support**
  - Contact form
  - Complaint management system
  - FAQ section

- 🌐 **Multilingual Support**
  - English
  - Arabic (العربية)
  - French (Français)
  - Amazigh (Tamaziɣt)

- 🎨 **Modern UI/UX**
  - Responsive design
  - Beautiful animations
  - Intuitive navigation

## 🛠️ Technical Stack

- **Backend:** Django 4.2
- **Frontend:** Bootstrap 5.1, HTML5, CSS3, JavaScript
- **Database:** SQLite (default), PostgreSQL (production)
- **Additional Libraries:**
  - Font Awesome 6.0
  - Google Fonts
  - Custom CSS animations

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/inokit.git
   cd inokit
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
inokit/
├── src/                    # Main application code
│   ├── core/              # Core application
│   │   ├── models.py     # Core models
│   │   ├── views.py      # Core views
│   │   └── urls.py       # Core URLs
│   └── shop/             # Shop application
│       ├── models.py     # Shop models
│       ├── views.py      # Shop views
│       └── urls.py       # Shop URLs
├── templates/             # HTML templates
│   ├── base/            # Base templates
│   ├── core/            # Core templates
│   └── shop/            # Shop templates
├── static/               # Static files
│   ├── css/            # CSS files
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
├── media/                # User-uploaded files
│   └── product_images/  # Product images
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🔧 Configuration

1. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

2. **Database Configuration**
   Update `settings.py` for your database:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

## 🌟 Usage

1. **Admin Panel**
   - Access `/admin` with superuser credentials
   - Manage products, orders, and users
   - Handle customer complaints

2. **Shopping**
   - Browse products by category
   - Add items to cart
   - Complete checkout process

3. **User Account**
   - Register/Login
   - View order history
   - Submit complaints

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Copyright © 2024 Omar Moutabir. All rights reserved.

This project and its contents are protected by copyright law. Unauthorized copying, modification, distribution, or use of this code is strictly prohibited.

## 📞 Contact

Omar Moutabir - omar.moutabir@gmail.com

Project Link: [https://github.com/yourusername/inokit](https://github.com/yourusername/inokit)

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Team
- Font Awesome
- All contributors and users of InoKit 

## 🔔 System Tray Application

InoKit comes with a convenient system tray application that allows you to manage the Django server directly from your taskbar's notification area (next to WiFi and battery icons).

### Features
- 🖥️ Start/Stop Django server with one click
- 🌐 Quick access to the website
- 📌 System tray icon with status indicators
- 🔔 Desktop notifications for server status

### Files
```
inokit/
├── system_tray.py          # Main tray application
├── tray_requirements.txt   # Tray app dependencies
├── setup_tray.bat         # Setup script
└── start_tray.bat         # Launcher script
```

### Setup Instructions

1. **Run the Setup Script**
   ```bash
   setup_tray.bat
   ```
   This will:
   - Install required packages (pystray, Pillow, psutil)
   - Create a desktop shortcut
   - Configure the application icon

2. **Launch the Application**
   - Double-click the "InoKit Server" shortcut on your desktop
   - Or run `start_tray.bat` directly

3. **Using the Tray Application**
   - Look for the InoKit icon in your system tray
   - Right-click the icon to see options:
     - Toggle Server: Start/stop Django server
     - Open Website: Launch http://127.0.0.1:8000
     - Quit: Close the application
   - Left-click to quickly toggle the server

### Requirements
- Windows OS
- Python 3.8+
- Required packages (automatically installed):
  ```
  pystray==0.19.5
  Pillow==10.1.0
  psutil==5.9.7
  ``` 