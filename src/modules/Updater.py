import json
import platform
import webbrowser
import requests
from PySide6.QtWidgets import QMessageBox


def check_for_updates(parent, current_version: str, proxy_path: str = "proxy.json") -> None:
    try:
        with open(proxy_path) as f:
            cfg = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        cfg = {"enable": "0", "proxy_ip": "0", "proxy_port": "0", "proxy_user": "", "proxy_password": ""}

    if cfg.get("enable") != "1":
        return

    proxies = None
    if cfg.get("proxy_ip", "0") != "0":
        auth = f"{cfg['proxy_user']}:{cfg['proxy_password']}@" if cfg.get("proxy_user") else ""
        proxy_url = f"http://{auth}{cfg['proxy_ip']}:{cfg['proxy_port']}"
        proxies = {"http": proxy_url, "https": proxy_url}

    try:
        resp = requests.get(
            "https://api.github.com/repos/felipecaninnovaes/PDFU/releases/latest",
            proxies=proxies,
            timeout=5,
        )
        data = resp.json()
        latest = data.get("tag_name", current_version)
    except Exception:
        return

    if latest == current_version:
        return

    answer = QMessageBox.question(
        parent,
        "Atualização disponível",
        f"Nova versão disponível: {latest}\nDeseja baixar agora?",
        QMessageBox.Yes | QMessageBox.No,
    )
    if answer == QMessageBox.Yes:
        os_name = platform.system()
        urls = {
            "Darwin": f"https://github.com/felipecaninnovaes/PDFU/releases/download/{latest}/PDFU_Setup_{latest}_MacOS.dmg",
            "Linux": f"https://github.com/felipecaninnovaes/PDFU/releases/download/{latest}/PDFU_Setup_{latest}_Linux.zip",
            "Windows": f"https://github.com/felipecaninnovaes/PDFU/releases/download/{latest}/PDFU_Setup_{latest}_Windows.exe",
        }
        url = urls.get(os_name)
        if url:
            webbrowser.open(url)
