"""
Service Package
Initializes Flask app with Talisman security headers and CORS policies
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers using Talisman
talisman = Talisman(app, force_https=False)

# CORS policy
CORS(app)

# Content Security Policy
csp = {
    'default-src': '\'self\'',
    'style-src': '\'self\'',
    'script-src': '\'self\''
}

talisman = Talisman(
    app,
    force_https=False,
    content_security_policy=csp
)

from service import routes  # noqa: E402, F401
