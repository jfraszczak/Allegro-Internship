# Allegro-Internship Zadanie nr. 3

Środowisko wirtualne
1. conda create --name your_env_name
2. conda activate your_env_name

3. Przejść do folderu, w którym znajduje się projekt (Allegro-Internship)
4. Zainstalować potrzebne biblioteki: pip install -r requirements.txt
5. Uruchomienie serwera: python manage.py runserver
6. W przypadku przekroczenia limitu requestów wykonywanych do API GitHuba należy zamieścić wygenerowany prywatny token (https://github.com/settings/tokens) w pliku settings.py 
w zmiennej GITHUB_TOKEN = <token> w postaci stringa

API

Wylistowanie repozytoriów
http://127.0.0.1:8000/github_api/repositories_list/?user=allegro

Suma gwiazdek
http://127.0.0.1:8000/github_api/stars_count_sum/?user=allegro

Ponadto istnieje możliwość paginacji oraz odwołania się do konkretnej strony poprzez parametr jak w poniższym przykładzie
http://127.0.0.1:8000/github_api/repositories_list/?user=allegro&page=3
