### Create deeplink
Create deeplink url using branch.io (python/django)

#### Steps
1. Copy branch_io.py anywhere you want to place it (in django parallel to manage.py)
2. Import method create_deep_link() in file where you want to use it
> from branch_io import create_deep_link
3. Call method to generate deeplink url
```
status, deep_link = create_deep_link()
if status:
    # Save deeplink url in DB
```

