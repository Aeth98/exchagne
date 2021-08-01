# exchange
Grazie al Driver Djongo, utilizzato per poter sfruttare le potenzialità di Django, ma usando come Database non relazionale MongoDB, ho realizzato una piattaforma di scambio di Bitcoin finti.
La piattaforma prevede una pagina per gestire la registrazione e l’accesso degli utenti.
Assegna automaticamente a ciascun utente registrato una cifra variabile tra gli 1 e i 10 bitcoin. 
Ciascun utente può pubblicare uno o più ordini di vendita o di acquisto di una certa quantità di bitcoin ad un certo prezzo.
Al momento della pubblicazione, se il prezzo di acquisto dell’ordine è pari o superiore al prezzo di vendita di un qualsiasi altro utente, registra la transazione e contrassegna entrambi gli ordini come eseguiti.
Prevede una pagina per ottenere tutti gli ordini di acquisto e vendita attivi.
Prevede anche una pagina per calcolare il profitto o la perdita totale derivante dalle operazioni di ciascun utente.
