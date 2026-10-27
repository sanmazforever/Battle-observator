# Battle-observator
Steallite observation on any battle

1. Fázis: Koncepció és Területválasztás
Cél: Egy aktív fegyveres konfliktus zóna monitorozása nyílt hozzáférésű média és műholdas adatokkal.

Helyszín kiválasztása: Bármikor könnyen átírható a megfigyelt terület, ezáltal a világ bármelyik fegyveres konfliktusát meglehet figyelni. Jelenleg az ukrajnai frontvonalra, pontosabban a Zaporizzsja déli szektorára, egy 30x30 kilométeres kereten belül figyeli meg a területet.

2. Fázis: Architektúra és Konfiguráció 
A központi konfigurációs fájl strukturált formában tárolja a koordinátákat, a bounding box-ot, valamint a monitorozott műholdak (Sentinel-1 SAR és Sentinel-2) és a 10 legfontosabb globális OSINT forrás listáját (ISW, DeepStateMap, Reuters, AP, BBC, AFP, Bellingcat, Liveuamap, War on The Rocks, The Defense Post).

3. Fázis: Automatikus Adatfeldolgozó Szkript 
A Python beolvassa a konfigurációt, majd dinamikusan generálja a napi dátummal ellátott Markdown jelentéseket, és biztosítja, hogy minden riport fixen 5 professzionális szempontot dolgozzon fel részletesen, közvetlen forrásmegjelölésekkel:

Kik uralnak milyen falvakat (Területi ellenőrzés & frontvonal-dinamika)

Hol vannak az állásaik (Védelmi vonalak, erődítések, aknamezők)

Hogy látszódik ez a műholdképekről (Sentinel-1 SAR és Sentinel-2 optikai elemzés)

Mi folyik a környéken (Taktikai események és harcmező-dinamika)

Ki mit mond (Hivatalos narratívák és független OSINT konszenzus)

4. Fázis: Felhőbeli Automatikus Futtatás
Minden egyes hétfőn írja meg a jelentést az adott csatatérről. Gyakrabban nem lehetséges, mert a műholdak csak 5 naponta tudnak frissebb információkkal szolgálni.
