🎓 Student Result Management System
      A Flask-based web application to manage student records, results, and academic history.
      This project demonstrates CRUD operations, database integration, and form handling using Python and SQLite.
      
🚀 Features
    1. Add new student records
    2.View all students in a history table
    3.Edit existing student details (prefilled form)
    4.Delete student records
    5.Registration number set as read-only during updates
    6.Automatic creation date and update date tracking
    7.Redirect to updated history page after editing
    8.Basic error handling (404 for invalid IDs)  


🛠 Tech Stack
    1.Backend: Python, Flask
    2.Database: SQLite
    3.Frontend: HTML, Jinja2 Templates
    4.Version Control: Git & GitHub
    
📂Project Structure
    student-result-app/
    │
    ├── app.py
    ├── students.db
    ├── templates/
    │   ├── index.html
    │   ├── edit.html
    │   └── history.html
    └── static/
        ├── jinjacss.css


⚙️ Installation & Setup

1.Clone Repositriy

  git clone https://github.com/your-username/student-result-app.git
  cd student-result-app
  
2. Create a Virtual Environment
  python -m venv venv

4. Activate the Virtual ENvironment 
  • Windows
      venv/scripts/activate
  • Mac/Linux
      source venv/bin/activate
   
4.Install Dependencies
    pip install -r requirements.txt
    
6. Run the application
    py app.run
   
6.Open in browser

  •  http://127.0.0.1:5000/http://127.0.0.1:5000/
  
  🏠 Home - Student Data Entry
  
        • Fill in student details and submit
  <img width="1868" height="604" alt="Screenshot 2026-03-02 143215" src="https://github.com/user-attachments/assets/171fb6b8-8f80-4476-8ee2-76ba23492c90" />
  📊 Result Page
  
        • View individual student result
<img width="972" height="703" alt="Screenshot 2026-03-02 140808" src="https://github.com/user-attachments/assets/e166338b-5527-4caa-a2b1-8daafdb64cb1" />
 📋 History - All Students
 
        • View all students with Search & Edit options
<img width="1845" height="510" alt="Screenshot 2026-03-02 143242" src="https://github.com/user-attachments/assets/bc0cb9eb-13a3-48cf-85a1-dbec423a2525" />
<img width="1838" height="517" alt="image" src="https://github.com/user-attachments/assets/b83a888d-1e0a-4f00-bdbf-5b4406530e6f" />
<img width="1863" height="509" alt="Screenshot 2026-03-02 143254" src="https://github.com/user-attachments/assets/0d7361ec-d234-43cb-a613-dd71f05d900e" />



