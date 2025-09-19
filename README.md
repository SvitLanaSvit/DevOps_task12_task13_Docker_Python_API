# Запуск через Docker Compose

1. **Запустіть сервіси через docker-compose:**
   ```bash
   docker compose up -d 
   ```

2. **Перевірте роботу контейнерів:**
   ```bash
   docker compose ps
   ```

3. **API буде доступний через nginx-проксі:**
   - Відкрийте у браузері: http://localhost:8080
   - Всі запити до API проходять через nginx (reverse proxy)

4. **Зупинити сервіси:**
   ```bash
   docker compose down
   ```

1. **docker compose up -d, docker ps**
![DOCKER_COMPOSE_UP_DOCKER_PS](Screenshots/DOCKER_COMPOSE_GET_ALL_SUCCSESS.png)
2. **GET /students** — отримати всіх студентів
![DOCKER_COMPOSE_GET_ALL_SUCCSESS](Screenshots/DOCKER_COMPOSE_GET_ALL_SUCCSESS.png)

---

# Запуск через Docker

1. **Зберіть Docker-образ:**
   ```bash
   docker build -t dz12-api .
   ```
2. **Запустіть контейнер:**
   ```bash
   docker run --rm -d -p 8000:8000 --name dz12-api-container dz12-api
   ```

Контейнер буде доступний на порту 8000.
1. **DOCKER_BUILD**
   ![DOCKER_BUILD](Screenshots/DOCKER_BUILD.png)
2. **DOCKER_RUN**
   ![DOCKER_RUN](Screenshots/DOCKER_RUN.png)
3. **GET /students** — отримати всіх студентів
   ![DOCKER_GET_ALL_SUCCSESS](Screenshots/DOCKER_GET_ALL_SUCCSESS.png)
4. **PUT /students/5** — оновити всі дані студента (успіх)
    ![DOCKER_PUT_SUCCSESS](Screenshots/DOCKER_PUT_SUCCSESS.png)

---

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
2. **GET /students/2** — отримати студента за id (успіх)
   ![GET_BY_ID_SUCCSESS](Screenshots/GET_BY_ID_SUCCSESS.png)
3. **GET /students/2** — отримати студента за id (помилка: не знайдено)
   ![GET_BY_ID_FAILED](Screenshots/GET_BY_ID_FAILED.png)
4. **GET /students/lastname/Smith** — отримати студентів за прізвищем (успіх)
   ![GET_BY_LASTNAME_SUCCSESS](Screenshots/GET_BY_LASTNAME_SUCCSESS.png)
5. **GET /students/lastname/Unknown** — отримати студентів за прізвищем (помилка)
    ![GET_BY_LASTNAME_FAILED](Screenshots/GET_BY_LASTNAME_FAILED.png)
6. **POST /students** — створити нового студента (успіх)
   ![POST_SUCCSESS](Screenshots/POST_SUCCSESS.png)
7. **POST /students** — створити нового студента (успіх, ще один)
   ![POST_SUCCSESS_1](Screenshots/POST_SUCCSESS_1.png)
8. **POST /students** — помилка: відсутнє поле вік
   ![POST_FAILED_NAME_1](Screenshots/POST_FAILED_NAME_1.png)
9. **POST /students** — помилка: не валідне поле
   ![POST_FAILED_NAME_2](Screenshots/POST_FAILED_NAME_2.png)
10. **POST /students** — помилка: студент з таким id вже існує
   ![POST_FAILED_ID_1](Screenshots/POST_FAILED_ID_1.png)
11. **PUT /students/5** — оновити всі дані студента (успіх)
    ![PUT_SUCCSESS](Screenshots/PUT_SUCCSESS.png)
12. **PUT /students/5** фбо **PUT /students/9** — оновити всі дані студента (логування)
    ![PUT_Logging](Screenshots/PUT_Logging.png)
13. **PUT /students/9** — оновити всі дані студента (помилка: студента не знайдено)
    ![PUT_FAILED_1](Screenshots/PUT_FAILED_1.png)
14. **PUT /students/5** — оновити всі дані студента (помилка: відсутнє поле вік)
    ![PUT_FAILED_2](Screenshots/PUT_FAILED_2.png)
15. **PUT /students/3** — оновити всі дані студента (помилка: відсутні поля)
    ![PUT_FAILED_3](Screenshots/PUT_FAILED_3.png)
16. **PUT /students/3** — оновити всі дані студента (помилка: не валідне поле)
   ![PUT_FAILED_4](Screenshots/PUT_FAILED_4.png)
17. **PATCH /students/2** — оновити вік студента (успіх)
   ![PATCH_AGE_SUCCESSSESS](Screenshots/PATCH_AGE_SUCCSESS.png)
18. **PATCH /students/9** — оновити вік студента (помилка: не знайдено студента за id)
   ![PATCH_AGE_NOT_FOUND_STUDENT_BY_ID](Screenshots/PATCH_AGE_NOT_FOUND_STUDENT_BY_ID.png)
19. **PATCH /students/2** — оновити вік студента (помилка: не передано поле age)
   ![PATCH_AGE_FAILED_NO_FIELD_AGE](Screenshots/PATCH_AGE_FAILED_NO_FIELD_AGE.png)
20. **PATCH /students/2** — оновити вік студента (помилка: невалідне поле)
   ![PATCH_AGE_FAILED_INVALID_FIELD](Screenshots/PATCH_AGE_FAILED_INVALID_FIELD.png)
21. **DELETE /students/2** — видалити студента (успіх)
    ![DELETE_SUCCSESS](Screenshots/DELETE_SUCCSESS.png)
22. **DELETE /students/4** — видалити студента (помилка: не знайдено студента за id)
    ![DELETE_FAILED](Screenshots/DELETE_FAILED.png)

---
