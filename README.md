## install package

- pyautogui
- pyinstaller (auto-py-to-exe)
- pyinstaller-versionfile

## versionfile

```bash
create-version-file ./version-info.yaml --outfile ./version-info.txt
```

## pyinstaller

```bash
pyinstaller --noconfirm --onefile --windowed --icon "./chrome.ico" --name "chrome" --version-file "./version-info.txt" --add-data "./chrome.ico;." --add-data "./running.gif;." --paths "./venv/Lib/site-packages"  "./mouse-jiggler.py"
```