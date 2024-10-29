# kavvaTTGprojektprogrammeerimine4Tartutammegymnaasium.ee
Liikmed: Martin Sibul, ralf Puhk, Rando Soodla, Mikk-Marcus Reidolf

Projekti nimi: Weekly

Projekt/Probleem:
Päevad on liiga kaootilised ja vajavad struktuuri. -> Programm, kuhu saab oma nädalakava kirja panna ning saadab vastavalt sõnumeid meeldetuletuseks (nt telefoni läbi discord bot'i). Lisame jooksvalt funktsioone kui ideid tuleb ja kui need on kohased.

Rollid:
Selguvad töö käigus
Esitluse tegemine - Rando ja Mikk

Trello link: https://trello.com/invite/b/66e00a063001d3e1a232c855/ATTI25a1ab93e3f7186cae275477210ec4de3531DF86/kavvattgprojektprogrammeerimine4

Paberprototüüp: https://magma.com/d/g1fcoIu3nH

Kasutajaliides prototüüp: https://magma.com/d/wln7slbyec



# Prototüübi juhend:
 Moodulid - tkcalendar, customtkinter,  spire.xls, spire, pandas [("pip install openpyxl"), kui openpyxl ei tööta, siis: "pip install pandas --upgrade"?], numpy, discordwebhook, discord, httplib2,  
 
 Meelespea loomiseks pead vajutama kuupäeva peale ning sisestama kellaaja.
 
 Kellaaeg tuleb sisestada formaadis HH:MM nt 12:29 voi 01:32
 
 Kui kuupäev ja kellaaeg on valitud, vajuta "Loo meelespea", siis kirjuta selle kohale oma sonum ning vajuta "Salvesta".
 
 Salvestamine appendib Discord ID, kuupäeva, kellaaja ning meelespea faili, milleks vaikimisi on fail.txt ning kohandab andmed ja salvestab .xlsx faili.
 
 NB! Programm peab lahti olema, et see sonumi saadaks Discordi. (discordi server, millesse sõnum saadetakse: https://discord.gg/qr4RssDH9J)
 
 Programm saadab teate minuti jooksul, kuna oleneb programmi avamise ajast -> ei pruugi olla iga minuti alguses.
 
 Kuidas saada oma discord ID: 
 
 Vajuta discordis all vasakul nupule "User Settings" -> Vajuta "Advanced" -> Käivita "Developer Mode" -> Mine seadetest välja -> All vasakul vajuta oma discordi profiili peale -> Vajuta "Copy User ID"

# Esitluse link: https://docs.google.com/presentation/d/1MXQZZ2hyl65x2q95LSAfljLQUDDqcKUjDBFytX8m9LI/edit?usp=sharing
