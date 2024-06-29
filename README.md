# beets-utaitedb

Plugin for beets to use UtaiteDB as an autotagger source.

## Configuration

The plugin uses beets default language list to determine which language to use
for tags.

```yaml
utaitedb:
  source_weight: 0.5    # Penalty to be added to all matches (0 disabled, 1 highest)
  prefer_romaji: false  # Prefer romanized if they exist rather than Japanese
  translated_lyrics: false  # Always get translated lyrics if they're available
```

### Advanced configuration

Source name and URLs can be changed inside the plugin source code in case
another site uses the same software as UtaiteDB (VocaDB, TouhouDB)

```python
UTAITEDB_NAME = "UtaiteDB"
UTAITEDB_BASE_URL = "https://utaitedb.net/"
UTAITEDB_API_URL = "https://utaitedb.net/api/"
```
