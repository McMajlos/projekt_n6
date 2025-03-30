# Engeto Testovací Projekt

## 🧪 Testování webového obsahu pomocí Playwrightu

Tento projekt využívá knihovnu [Playwright](https://playwright.dev/python/) pro automatizované testování webového obsahu napříč různými prohlížeči.

### 📁 Přehled

Soubor `test_website.py` obsahuje celkem **5 testů**, které se spouští ve **3 různých prohlížečích**:

- Chromium
- Firefox
- WebKit

Dohromady je tedy spuštěno **15 testů** při každém běhu.

### ✅ Co se testuje

Testovací sada ověřuje následující funkce:

1. Správný **název stránky** (page title)
2. Zobrazení a obsah **nadpisu H1**
3. Zobrazení tlačítka **"Restart"**
4. Zobrazení tlačítka/odkazu **"WS"**
5. Že **"WS" tlačítko** odkazuje na správnou cílovou URL adresu

---

### 🚀 Jak spustit testy

1. Ujisti se, že máš nainstalovaný Playwright a potřebné závislosti:

```bash
pip install -r requirements.txt
playwright install
