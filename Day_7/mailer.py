# nigdy haseł i loginów, adresów email nie wysyłaj na zdalne repo
# nawet jeśli jest prywatne - czasem poprzez błedy w oprogramowaniu
# może zdarzyć się tak, że prywatne repo stanie się publicznym
# i wtedy Twoje hasła zostaną na 99.999999% wykradzione.
import secrets
import smtplib


adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworze silnik mailera
mailer = smtplib.SMTP("smtp.gmail.com", 587)
# witam sie z serwerem / łącze się
mailer.ehlo()
# szyfruje połączenie
mailer.starttls()
# loguje się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Arek\n"
wiadomosc = "To jest moja wiadomosc"
tresc = temat + wiadomosc

# wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila!")

mailer.close()
