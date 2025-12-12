from fasthtml.common import FastHTML, serve
from faststrap import *

app = FastHTML()


add_bootstrap(
    app,
    theme="dark",
)


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
                        ("home", "Home", True),
                        ("profile", "Profile"),
                        ("settings", "Settings"),
                    ),
                ),
                cols=12,
                md=12,
                lg=4,
            ),
        ),
    )


serve()
