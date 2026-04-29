import multiprocessing
import os
import sys

# Allow running from src/ directly
sys.path.insert(0, os.path.dirname(__file__))

from app.app import create_app
from views.main_window import MainWindow, APP_VERSION
from modules.Updater import check_for_updates


def main():
    multiprocessing.freeze_support()
    app = create_app(sys.argv)

    window = MainWindow()
    window.show()

    # Non-blocking update check after window is shown
    app.processEvents()
    proxy_path = os.path.join(os.path.dirname(__file__), "proxy.json")
    check_for_updates(window, APP_VERSION, proxy_path)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
