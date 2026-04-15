# Työvuorojärjestelmä
Alkuperäiset tavoitteet: 
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan työvuoroja.
- Käyttäjä pystyy lisäämään tietoja työvuoroon.
- Käyttäjä näkee sovellukseen lisätyt työvuorot ja niiden tiedot
- Käyttäjä pystyy etsimään työvuoroja hakusanalla (teemoittain).
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät ilmoitukset koskien työvuoroja.
- Käyttäjä pystyy valitsemaan työvuorolle yhden tai useamman luokittelun (esim. mikä työ on kyseessä, teema, kohderyhmä).
- Käyttäjä pystyy kommentoimaan työvuoroja

Tämänhetkinen tilanne:
- Kaikki toiminnot alkuperäisistä tavoitteista toteutuvat.
- Tietoturvaa on lisätty CSRF-avulla ja myös niin, että vain kirjautuneena pääset näkemään enemmän tietoja. Käyttäjä pystyy myös muokkaamaan vain omia työvuorojaan.
- Kategorioita pystyy tarkoituksella valitsemaan vain yhden. 

Asennusohjeet:
- Kloonaa repositorio: git clone https://github.com/pylkeetu/Tyovuorojarjestelma.git
- Siirry projektikansioon: cd Tyovuorojarjestelma
- Luo virtuaaliympäristö: python -m venv venv
- Aktivoi virtuaaliympäristö: venv\Scripts\activate (Windows)
- Aktivoi virtuaaliympäristö: source venv/bin/activate (Mac/Linux)
- Asenna riippuvuudet: pip install -r requirements.txt ja pip install flask-wtf

Tietokannan luominen:

Powershell:
- Get-Content schema.sql | sqlite3 database.db

CMD:
- sqlite3 database.db < schema.sql

Sovelluksen käynnistäminen:

- flask run

- Sovellus käynnistyy osoitteeseen: http://127.0.0.1:5000/
