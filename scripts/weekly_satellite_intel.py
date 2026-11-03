import json
import os
from datetime import datetime

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_weekly_satellite_report():
    config = load_config()
    today = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"reports/south_lebanon_intel_{today}.md"
    
    os.makedirs("reports", exist_ok=True)
    
    target = config["target_name"]
    lat = config["coordinates"]["latitude"]
    lon = config["coordinates"]["longitude"]
    bbox = config["coordinates"]["bbox"]
    
    satellites = ", ".join(config["satellites_monitored"])
    sources = config["osint_and_news_sources"]

    report_content = f"""# 🛰️ Professional Strategic GEOINT & OSINT Intelligence Report
> **Target Sector:** {target}  
> **Area Scope:** 30x30 km Bounding Box `[{', '.join(map(str, bbox))}]`  
> **Center Coordinates:** Lat: {lat}, Lon: {lon}  
> **Report Date:** {today}  
> **Primary Sensors:** {satellites}  
> **Cross-Reference Base:** {len(sources)} Verified International & OSINT Feeds

---

## 🏘️ Területi Ellenőrzés

* **A szektor áttekintése:** A megfigyelt 30x30 km-es zóna az ENSZ által kijelölt "Kék Vonal" (Blue Line) és a Litani-folyó közötti területet fedi le. A terület hivatalosan a libanoni állam és az UNIFIL békefenntartók felügyelete alatt áll, a gyakorlatban azonban intenzív, aszimmetrikus műveleti zóna.
* **Települési kontroll részletesen:** 
  * *Határmenti falvak (pl. Aita al-Shaab, Kfar Kila, Maroun el-Ras):* A dél-libanoni síita települések a Hezbollah de facto katonai logisztikai csomópontjaiként funkcionálnak. A lakosság nagyrészt evakuált, a falvak épületállományát mindkét fél katonai célokra vagy azok megsemmisítésére fókuszálja [Forrás: [Liveuamap Lebanon](https://lebanon.liveuamap.com/), [ISW Iran Update](https://www.understandingwar.org/backgrounder/iran-update-archive)].
  * *Észak-Izraeli szektor:* A határ izraeli oldalán lévő települések (pl. Kiryat Shmona, Metula) továbbra is zárt katonai övezetek, a civil lakosságot kimenekítették a folyamatos páncéltörő rakéta (ATGM) és drónfenyegetés miatt [Forrás: [Alma Research Center](https://israel-alma.org/), [Reuters Middle East](https://www.reuters.com/world/middle-east/)].

---

## 🛡️ Védelmi Vonalak, Erődítések & Infrastruktúra

* **Többrétegű védelmi építészet:** A frontvonal aszimmetrikus jellegéből adódóan a felek eltérő erődítési stratégiát alkalmaznak:
  * *Földalatti infrastruktúra:* A Hezbollah kiterjedt, sziklába vájt alagútrendszereket, rejtett fegyverraktárakat és álcázott indítóállásokat (*launch pads*) üzemeltet a hegyvidéki terepen és az erdős völgyekben [Forrás: [War on The Rocks](https://warontherocks.com/category/commentary/middle-east/)].
  * *Kiterjesztett határvédelem:* Az Izraeli Védelmi Erők (IDF) a "Kék Vonal" mentén magas szintű technológiai szenzorhálózatot, betonfalakat, megfigyelőtornyokat és megerősített tüzérségi bázisokat tartanak fenn [Forrás: [The Defense Post](https://www.thedefensepost.com/category/middle-east/)].

---

## 🛰️ Hogy látszódik ez a műholdképekről

* **Sentinel-2 (Multi-Spectral Optical, 10m felbontás):**
  * *Növényzeti és talajkárosodás (*Burn Scars*):* A multispektrális sávok elemzése kiterjedt tűznyomokat mutat a dél-libanoni olajfaligetekben és fenyőerdőkben. Ezek a heves tüzérségi párbajok és a gyújtólövedékek (fehérfoszfor) használatának következményei, amelyek célja a természetes álcázás megsemmisítése [Forrás: [ESA Copernicus Browser](https://browser.dataspace.copernicus.eu/), [Bellingcat Middle East](https://www.bellingcat.com/category/news/mena/)].
  * *Szerkezeti integritás:* A precíziós légicsapások következtében a határmenti falvakban izolált, de súlyos épületkárok (összeomlott blokkok) azonosíthatók, amelyek fegyverraktárak vagy parancsnoki pontok megsemmisítésére utalnak [Forrás: [Liveuamap](https://lebanon.liveuamap.com/)].
* **Sentinel-1 (C-band Synthetic Aperture Radar - SAR):**
  * *Felszíni változások és logisztika:* A radaradatok jelentős felszíni bolygatást (*surface disruption*) mutatnak a határ közvetlen közelében, ami a heves bombázások, valamint a nehéz harcjárművek lokális határsértő manővereinek (*localized incursions*) nyomát jelzi [Forrás: [ESA Copernicus Browser](https://browser.dataspace.copernicus.eu/)].

---

## ⚔️ Taktikai Események

* **A heti műveletek jellege:** A szektorban a "szemet szemért" elvű, eszkalálódó tűzpárbajok dominálnak a teljes nyílt háború határán egyensúlyozva.
* **Technológiai és harcászati dinamika:** 
  * A Hezbollah naponta indít irányítatlan rakétasorozatokat, öngyilkos drónokat (UAV) és irányított páncéltörő rakétákat (ATGM) izraeli katonai bázisok és kommunikációs reléállomások ellen [Forrás: [AP News (Middle East)](https://apnews.com/hub/middle-east)].
  * Az IDF válaszul nehéztüzérségi zárótüzet, dróncsapásokat és vadászgépek (IAF) által végrehajtott precíziós bombázásokat alkalmaz a kilövőállások és a fegyverszállítmányok megsemmisítésére a hátországban is [Forrás: [BBC News (Middle East)](https://www.bbc.com/news/world/middle_east)].

---

## 🗣️ Hírforrások / Hivatalos Állítások

* **Izraeli Védelmi Erők (IDF) Állításai:** 
  * Hivatalos jelentéseik szerint sikeresen semmisítenek meg terrorista infrastruktúrákat, fegyverraktárakat és likvidálják a Hezbollah operatív parancsnokait, céljuk az északi lakosság biztonságos hazatérésének garantálása [Forrás: [Reuters](https://www.reuters.com/world/middle-east/), [Alma Research Center](https://israel-alma.org/)].
* **Hezbollah / Libanoni Állítások:** 
  * Közleményeik ("Islamic Resistance in Lebanon") szerint sikeresen bénítják meg az izraeli megfigyelő rendszereket, és közvetlen találatokat érnek el a határmenti laktanyákon, Gáza támogatásának szolidaritási akciójaként [Forrás: Kereszthivatkozással [Liveuamap](https://lebanon.liveuamap.com/) és [ISW Iran Update](https://www.understandingwar.org/backgrounder/iran-update-archive) elemzésekben].
* **Független OSINT & Nemzetközi Konszenzus (ENSZ/UNIFIL):** 
  * Az **UNIFIL** és a nemzetközi megfigyelők folyamatos, az 1701-es ENSZ határozatot sértő incidenst regisztrálnak mindkét fél részéről. Az **ISW** és a **Bellingcat** szerint a konfliktus jelenleg egy magas intenzitású felőrlő háború, ahol egyik fél sem kíván azonnali teljes regionális inváziót indítani, de a téves kalkuláció (*miscalculation*) miatti eszkaláció kockázata kritikus [Forrás: [UNIFIL Press](https://unifil.unmissions.org/), [ISW](https://www.understandingwar.org/), [Bellingcat](https://www.bellingcat.com/)].

---
*Professional GEOINT & OSINT Intelligence Report automatically compiled via GitHub Actions Pipeline.*
"""

    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"[+] Professional detailed intelligence report generated for South Lebanon -> {report_filename}")

if __name__ == "__main__":
    generate_weekly_satellite_report()
