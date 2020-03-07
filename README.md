## Welcome to Kissanime Notifier

You can fork the [commit](https://github.com/1hef001/Kissanime-notifier/) and change it as seen necessary. It is a work in progress, and any modifications in the right direction are welcomed.


### Essentials

Since the [site](https://www.kissanime.ru) is a cloudflare protected site, we need to bypass the cloudflare security to scrape the content.
Furthermore, if the video can be temporarily downloaded and played from local storage, it is appreciated.

```markdown
**Import statements necessary as of now:**

import cloudscraper
from bs4 import BeautifulSoup

```

### TO DO:

1. Scrape dynamic content (timer, etc.)
2. Maintain user favorites and notify
