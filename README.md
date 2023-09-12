# Rock Your Mouse! (Similar to MouseJiggler)

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
pyinstaller --noconfirm --onefile --windowed --icon "./rock.ico" --name "RockYourMouse.exe" --version-file "./version-info.txt" --add-data "./rock.ico;." --add-data "./rock-dog.gif;." --paths "./venv/Lib/site-packages"  "./rock-your-mouse.py"
```