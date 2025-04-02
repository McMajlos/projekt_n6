from playwright.sync_api import sync_playwright, Page, Browser, expect
import pytest


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser(request):
    # Vytvoříme instanci prohlížeče na základě parametru
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser: Browser):
    context = browser.new_context()
    try:
        page = context.new_page()
        page.set_default_timeout(2000)
        page.goto("https://www.whitescreen.online/fake-windows-11-update-screenn/"),
        page.get_by_role("button", name="Consent to all").click()
        yield page
    finally:
        context.close()


def test_title(page: Page):
    # Ověříme, že stránka má správný titulek
    expect(page).to_have_title("Windows 11 Fake Update | Online Tool")


def test_h1_is_visible(page: Page):
    # Ověříme, že H1 je viditelný a obsahuje správný text
    h1 = page.locator("h1")
    expect(h1).to_be_visible()
    expect(h1).to_contain_text("Windows 11 Fake Update")

def test_restart_button_is_visible(page: Page):
    # Ověříme, že tlačítko Restart je viditelné
    restart_button = page.get_by_role("button", name="Restart")
    # Alternativy tlačítka restart
        # Pomocí ID
    # restart_button = page.locator("#update-restart-btn")
        # Pomocí class
    # restart_button = page.locator(".download-btn")
        # Pomocí id i class
    # restart_button = page.locator(".download-btn#update-restart-btn")
    expect(restart_button).to_be_visible()


def test_ws_button_is_visible(page: Page):
    # Ověříme, že tlačítko WS je viditelné
    ws_button = page.get_by_role("link", name="WS", exact=True)
    expect(ws_button).to_be_visible()


def test_ws_button_url_after_click(page: Page):
    # Ověříme, že po kliknutí na tlačítko WS se otevře správná stránka
    page.get_by_role("link", name="WS", exact=True).click()
    expect(page).to_have_url("https://www.whitescreen.online/")
