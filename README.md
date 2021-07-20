# exchange
Ho realizzato un semplice exchange, dove si scambiano bitcoin finti. Ad ogni utente vengono assegnati alla registrazione 10 bitcoin. Il sito ha una pagina in cui si puo' immettere
un ordine a mercato, una pagina in cui si possono vedere le operazioni effettuate, e un'altra in cui si possono vedere tutti gli ordini ancora attivi a mercato.
Il meccanismo di scambio funziona in questo modo: Se un utente decide di comprare una determinata quantita' di bitcoin ad un certo prezzo, si controlla se c'è almeno un'altra persona
che ha immesso un ordine di vendita a quel prezzo o meno. Se ad esempio l'utente X vuole comprare 3 bitcoin a a 9000 usd, ed esiste un secondo utente Y che ha immesso un ordine di vendita
a un prezzo <= 9000 usd, la transazione si conclude. Si considera anche il caso in cui non tutta la domanda viene soddisfatta, ad esempio se l'utente Y volesse vendere soltanto 2 bitcoin
, la transazione avverrebbe comunque, tenendo conto di 1 bitcoin ancora da comprare.

Future migliorie:
Implementare lo stesso algoritmo anche per chi sta vendendo, infatti per ora gli ordini sell sono "passivi" e vengono eseguiti soltanto se dopo aver immesso l'ordine,
un secondo utente decide di comprare a quel prezzo o meno. Questo vuol dire che nell'esempio precedente il bitcoin rimanente non verrebbe piu' comprato.

Realizzare un html e css accattivante, infatti mi sono concentrato soltanto sulla parte backend.

Assegnare alla registrazione non solo una quantità di bitcoin fissa, ma anche di USD, infatti al momento è possibile immettere ordini di acquisto infiniti.
