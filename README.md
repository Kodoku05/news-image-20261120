# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Kodoku05/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Kodoku05/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

The World Today — 20 November 2026: a program that sums up the world news
of Friday 20 November 2026 as a one-page newspaper front page (a 1024×1024
PNG). Lead story: Cyclone Akvan's landfall in Odisha; plus Trump's return
from Shenzhen, the Kyiv embassy row, 37 killed in Nyala drone strikes, the
Senate's 51–48 Iran vote, Nicholls' unbeaten 113, GTA VI's first full day,
COP31 talks, and World Children's Day.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out node main.ts
```

Writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`). Node 22,
standard library only. Deterministic: repeated runs produce identical bytes.
`draw_poster.py` (Python + Pillow) regenerates the poster from the news data
in `news.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=p2xp6s2q&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
