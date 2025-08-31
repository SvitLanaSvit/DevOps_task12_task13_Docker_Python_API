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

3. **Перевірте залежності**
   ```bash
   pip freeze
   ```

4. **Встановіть необхідні пакети**
   ```bash
   pip install flask requests
   ```

5. **Запустіть сервер**
   ```bash
   python app.py
   ```

## Використання API

- **GET /students** — отримати список всіх студентів
- **GET /students/<id>** — отримати студента за id
- **GET /students/lastname/<last_name>** — отримати студентів за прізвищем
- **POST /students** — додати нового студента (тіло: first_name, last_name, age)
- **PUT /students/<id>** — оновити дані студента
- **DELETE /students/<id>** — видалити студента

## Примітки
- Дані зберігаються у файлі `students.csv`, який ігнорується у git.
- Всі налаштування та залежності описані у цьому README.
