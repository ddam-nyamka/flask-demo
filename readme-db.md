## Migration

```sh

# initially (unnecessary to run if db migrated once)
flask db stamp head
flask db migrate

# latest migration changes (necessary to run)
flask db upgrade
```
