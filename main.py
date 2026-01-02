from fasthtml.common import *
from faststrap import *

app = FastHTML()


add_bootstrap(
    app,
    mode="dark",
)

ICONS = {
    "home": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
    "info": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-info"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
}


def Icon(
    name: str,  # name of the icon MUST be in icon_dict
    size=24,  # value to be passed to height and width of the icon
    stroke=1.5,  # stroke width
    cls=None,  # css class
    icon_dict: dict = ICONS,  # Dict of icons {"name":"<svg...>"}
    **kwargs,  # passed to through to FT
) -> "Any":  # Follow recomendation from fastHTML docs
    """
    Creates a custom html compliant <icon-{name}>...
    Intended to be used with a Global Dict of icons {"home": "<svg...", "info": "<svg..."}
    Icon('home') -> <icon-home> ....  </icon-home>
    """
    if name not in icon_dict:
        raise ValueError(f"Icon '{name}' not found")

    # count=1 Replace only the first occurrence of width & height 99% of time this is what you want
    svg_string = icon_dict[name]
    svg_string = re.sub(r'width="\d+"', f'width="{size}"', svg_string, count=1)
    svg_string = re.sub(r'height="\d+"', f'height="{size}"', svg_string, count=1)
    svg_string = re.sub(r'stroke-width="\d+"', f'stroke-width="{stroke}"', svg_string)

    return ft(f"icon-{name}", NotStr(svg_string), cls=cls, **kwargs)


@app.route("/")
def home():
    return (
        Container(
            Row(
                Col(
                    Card(
                        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
                        header="Hello World 👋",
                        footer=Button("Get Started", variant="primary"),
                    ),
                    cols=12,
                    md=6,
                    lg=4,
                ),
                Col(
                    Card(
                        Input(
                            "email",
                            input_type="email",
                            label="Email Address",
                            required=True,
                            help_text="We'll never share your email with anyone else.",
                        ),
                        Select(
                            "country",
                            ("us", "USA"),
                            ("uk", "UK"),
                            label="Country",
                            help_text="Select your country of residence.",
                        ),
                        footer=Button(
                            "Save",
                            variant="primary",
                            hx_post="/save",
                            hx_target="#result",
                        ),
                    ),
                    cols=12,
                    md=6,
                    lg=4,
                ),
                Col(
                    Tabs(
                        ("home", Icon("home"), True),
                        ("info", Icon("info"), False),
                        ("profile", "Profile", False),
                        ("settings", "Settings", False),
                        # variant="pills",
                    ),
                    Div(
                        TabPane(
                            "This is the home tab content.",
                            tab_id="home",
                            active=True,
                        ),
                        TabPane(
                            "This is the info tab content.",
                            tab_id="info",
                        ),
                        TabPane(
                            "This is the profile tab content.",
                            tab_id="profile",
                        ),
                        TabPane(
                            "This is the settings tab content.",
                            tab_id="settings",
                        ),
                        cls="tab-content",
                    ),
                ),
                cols=12,
                md=12,
                lg=4,
            ),
        ),
    )


serve()
