"""The news of Friday 20 November 2026, as data.

Kept apart from the renderer so the front page can be refreshed with the
full day's news before the deadline (22 Nov 07:00 WIB) by editing this
file alone and re-running draw_poster.py.

Sources (checked 20 Nov 2026 ~07:30 WIB): IMD bulletins and Indian press
for Cyclone Akvan; Daily Caller for Trump's Friday press conference;
Reuters/AFP/CNN/The Times for the Kyiv embassy fallout; NZ press for the
Wellington Test; UN for World Children's Day; APEC/COP31 coverage.
"""

MASTHEAD = "THE WORLD TODAY"
DATE_LINE = "FRIDAY 20 NOVEMBER 2026"

LEAD_TITLE = "CYCLONE AKVAN SLAMS INTO ODISHA"
LEAD_DECK = (
    "Severe storm crosses the coast near Gopalpur by noon with gusts to "
    "110 kmph; more than 100,000 people moved to shelters."
)

# (headline, deck) — two-column grid, in reading order.
STORIES = (
    (
        "TRUMP FLIES HOME TO FACE PRESS",
        "President returns from the Shenzhen summit and holds a White House news conference on Friday.",
    ),
    (
        "KYIV EMBASSY ROW GROWS",
        "The Netherlands summons Moscow's envoy after drone strikes damage Dutch and Austrian embassies; one killed in Kyiv.",
    ),
    (
        "37 KILLED IN NYALA DRONE STRIKES",
        "Drone bombardment hits Darfur's largest city; the UN says drones caused nearly three-quarters of civilian deaths this year.",
    ),
    (
        "SENATE BACKS TRUMP ON IRAN WAR",
        "Senators vote 51–48 to reject a war powers resolution in the first Iran vote since the midterm elections.",
    ),
    (
        "NICHOLLS HOLDS FIRM FOR NZ",
        "Henry Nicholls unbeaten on 113 as New Zealand resume day two of the first Test against India on 243–5 in Wellington.",
    ),
    (
        "GTA VI'S FIRST FULL DAY",
        "A day after its midnight launch, Rockstar's blockbuster is in players' hands worldwide; preorders topped $1.5bn.",
    ),
    (
        "COP31 TALKS PRESS ON",
        "Climate negotiators in Türkiye push on financing and disaster-resilient infrastructure; India presses its case.",
    ),
    (
        "WORLD MARKS CHILDREN'S DAY",
        "20 November is World Children's Day, the UN's day for children's rights around the globe.",
    ),
)

FOOTER_LINES = (
    "Cyclone Akvan: schools shut in six Odisha districts through Saturday as rain lashes the coast",
    "Shenzhen declaration sets no timelines for nuclear talks or UN reform",
)
