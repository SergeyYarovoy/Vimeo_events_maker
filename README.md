## Налаштування середовища

1. Створіть віртуальне середовище:
   ```bash
   python3 -m venv venv
   ```

2. Активуйте віртуальне середовище:

   На Windows:

   ```bash
   venv\Scripts\activate
   ```
   На macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Перейти в фолдер python
   ```bash
   cd python
   ```
   
4. Встановіть залежності:

   ```bash
   pip install -r requirements.txt
   ```

## Використання

   ```bash
   python3 create_live_events.py --user_token <insert_your_user_token> --user_id <insert_your_user_id> --count <insert_count_of_ivents>
   ```

