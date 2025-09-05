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

## Опис результатів та скріншоти

Нижче наведено послідовність виконання всіх методів API згідно з вимогами завдання. Для кожного кроку додано скріншот із результатом (див. папку Screenshots):


1. **GET /students** — отримати всіх студентів
   ![GET_ALL_SUCCSESS](Screenshots/GET_ALL_SUCCSESS.png)
2. **POST /students** — створити нового студента (успіх)
   ![POST_SUCCSESS](Screenshots/POST_SUCCSESS.png)
3. **POST /students** — створити нового студента (успіх, ще один)
   ![POST_SUCCSESS_1](Screenshots/POST_SUCCSESS_1.png)
4. **POST /students** — помилка: не вказано ім'я
   ![POST_FAILED_NAME_1](Screenshots/POST_FAILED_NAME_1.png)
5. **POST /students** — помилка: не вказано ім'я (ще один варіант)
   ![POST_FAILED_NAME_2](Screenshots/POST_FAILED_NAME_2.png)
6. **POST /students** — помилка: не вказано id
   ![POST_FAILED_ID_1](Screenshots/POST_FAILED_ID_1.png)
7. **GET /students/2** — отримати студента за id (успіх)
   ![GET_BY_ID_SUCCSESS](Screenshots/GET_BY_ID_SUCCSESS.png)
8. **GET /students/2** — отримати студента за id (помилка: не знайдено)
   ![GET_BY_ID_FAILED](Screenshots/GET_BY_ID_FAILED.png)
9. **GET /students/lastname/Smith** — отримати студентів за прізвищем (успіх)
   ![GET_BY_LASTNAME_SUCCSESS](Screenshots/GET_BY_LASTNAME_SUCCSESS.png)
10. **GET /students/lastname/Unknown** — отримати студентів за прізвищем (помилка)
    ![GET_BY_LASTNAME_FAILED](Screenshots/GET_BY_LASTNAME_FAILED.png)
11. **PUT /students/3** — оновити всі дані студента (успіх)
    ![PUT_SUCCSESS](Screenshots/PUT_SUCCSESS.png)
12. **PUT /students/3** — оновити всі дані студента (логування)
    ![PUT_Logging](Screenshots/PUT_Logging.png)
13. **PUT /students/3** — оновити всі дані студента (помилка 1)
    ![PUT_FAILED_1](Screenshots/PUT_FAILED_1.png)
14. **PUT /students/3** — оновити всі дані студента (помилка 2)
    ![PUT_FAILED_2](Screenshots/PUT_FAILED_2.png)
15. **PUT /students/3** — оновити всі дані студента (помилка 3)
    ![PUT_FAILED_3](Screenshots/PUT_FAILED_3.png)
16. **PUT /students/3** — оновити всі дані студента (помилка 4)
    ![PUT_FAILED_4](Screenshots/PUT_FAILED_4.png)
17. **DELETE /students/1** — видалити студента (успіх)
    ![DELETE_SUCCSESS](Screenshots/DELETE_SUCCSESS.png)
18. **DELETE /students/1** — видалити студента (помилка)
    ![DELETE_FAILED](Screenshots/DELETE_FAILED.png)
