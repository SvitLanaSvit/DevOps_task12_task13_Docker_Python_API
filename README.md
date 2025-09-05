# Flask Students API

## Як запустити проект

1. **Створіть віртуальне оточення**
   ```bash
   python -m venv .venv
   ```

2. **Активуйте віртуальне оточення**
   - **Windows:**
     ```bash
     source .venv/Scripts/activate
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```


3. **Встановіть необхідні пакети**
   > **Рекомендується:**
   ```bash
   pip install -r requirements.txt
   ```
   > Якщо потрібно, можна перевірити всі встановлені пакети командою `pip freeze`, але для запуску проєкту достатньо requirements.txt.

4. **Запустіть сервер**
   ```bash
   python app.py
   ```

5. **Запустіть тести для API**
   ```bash
   python test_requests.py
   ```

## Використання API

- **GET /students** — отримати список всіх студентів
- **GET /students/<id>** — отримати студента за id
- **GET /students/lastname/<last_name>** — отримати студентів за прізвищем
- **POST /students** — додати нового студента (тіло: first_name, last_name, age)
- **PATCH /students/<id>** — оновити лише вік студента (тіло: age)
- **PUT /students/<id>** — оновити дані студента
- **DELETE /students/<id>** — видалити студента

## Примітки
- Дані зберігаються у файлі `students.csv`, який ігнорується у git.
- Всі налаштування та залежності описані у цьому README.
