# AutomatedCryptoWebsite

🇫🇷

Ce script Python récupère les données des 10 principales crypto-monnaies de l'API CoinMarketCap et les stocke dans un fichier CSV.

__Comment ça marche__ ?

* Le script commence par charger les variables d'environnement à l'aide de dotenv.
* Il tente ensuite de se connecter à l'API CoinMarketCap avec une clé API spécifiée.
* Une fois les données récupérées, elles sont normalisées en utilisant pandas.
* Les données sont ensuite enregistrées dans un fichier CSV.
* Le script s'exécute en boucle, avec une pause de 60 secondes entre chaque exécution.

🇺🇸

This Python script retrieves data for the top 10 cryptocurrencies from the CoinMarketCap API and stores it in a CSV file.

__How it works__ ?

* The script starts by loading environment variables using dotenv.
* It then attempts to connect to the CoinMarketCap API with an activated API key.
* After the data is retrieved, it is normalized using pandas.
* The data is then saved in a CSV file.
* The script runs in a loop, with a 60 second pause between each run.
