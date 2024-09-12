from BrowserPackage.Openbrowser import open_browser
from BrowserPackage.Closebrowser import close_browser

def test_case():
    open_browser()
    print("heloo im executing")
    close_browser()

test_case()