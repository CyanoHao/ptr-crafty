# PTR Crafty

## WARNING: NEVER USE 3RD-PARTY SCRIPTING ON LIVE REALMS!

An isolated environment is strongly recommended.

Choose an empty realm and create a placeholder character in connected realms.

Keep an eye on WoW. There is daily(?) limit of character deletion.

## Usage:

### Preparation

1. Install Python.
2. Install dependencies.
   ```bash
   pip install --user -r requirements.txt
   ```
3. Install [PTR Crafty Helper](./CraftyHelper) add-on and do necessary modification.

### Main Script `copy-mail.py`:

Copy character, mail supplies to inventory character, and then delete copied character.

```bash
python copy-mail.py config.yml
```

### Auxiliary Script `tell.py`

Print current position of mouse pointer periodically.
