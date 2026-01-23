# 🧪 UI Automation Framework (Python + Playwright + Jenkins)

Цей проєкт реалізує автоматизоване тестування веб-інтерфейсу з використанням **Playwright** та інтеграцією в **Jenkins CI/CD**.

Основна мета налаштування — забезпечити стабільний запуск UI-тестів (включно з режимом `headless=False`) у контейнеризованому середовищі Docker, яке за замовчуванням не має графічного інтерфейсу.

---

## 🛠 Технічний стек та архітектурні рішення

-   **Python 3.13** + **Pytest**: Основний двигун тестів.
-   **Playwright**: Інструмент автоматизації браузера.
-   **Docker**: Ізольоване середовище для Jenkins.
-   **Xvfb (X Virtual Framebuffer)**: Емуляція монітора в оперативній пам'яті.
    -   *Аргументація:* Тести налаштовані на запуск із GUI (`headless=False`). Оскільки Docker-контейнер — це сервер без екрана, браузер падає з помилкою `Missing X server`. Xvfb створює віртуальний дисплей, "обманюючи" браузер і дозволяючи йому рендерити сторінки.
-   **Allure Report**: Для візуалізації результатів тестування.

---

## 🚀 Інструкція: Локальний запуск

Для розробки та налагодження тестів локально:

1.  **Клонування та підготовка:**
    
    ```bash
    git clone [https://github.com/Kai4ch1/hillel_python_aqa.git](https://github.com/Kai4ch1/hillel_python_aqa.git)
    cd hillel_python_aqa
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install
    ```
    
2.  **Конфігурація:** Створіть файл `.env` (доданий у `.gitignore`) для локальних запусків:
    
    ```bash
    BASE_PAGE_URL_WITH_CREDENTIALS="[https://login:pass@example.com](https://login:pass@example.com)"
    ```
    
3.  **Запуск:**
    
    ```bash
    pytest lesson_26/tests/test_login.py
    ```
    

---

## 🐳 Інструкція: Налаштування CI/CD (Jenkins in Docker)

Для запуску в CI ми використовуємо офіційний образ Jenkins, але з суттєвими модифікаціями середовища для підтримки Playwright.

### Етап 1: Підйом інфраструктури

Запускаємо Jenkins з монтуванням тому для збереження даних (jobs, history, plugins):

```bash
docker run -d -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts-jdk17
```

### Етап 2: Ручне встановлення системних бібліотек

```bash
docker exec -u 0 -it jenkins bash
```

#### Встановлення всередені контейнеру

```bash
apt-get update && apt-get install -y xvfb libglib2.0-0 libnss3 libnspr4 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxcb1 libxkbcommon0 libatspi2.0-0 libx11-6 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2
```