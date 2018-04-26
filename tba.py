from typing import Dict, Any
import requests
import json
import re

import constants as c


def get_current_phase() -> Dict[str, Any]:
    req_url = "https://www.thebluealliance.com/api/v3/team/{}/event/{}/status".format(c.TEAM_KEY, c.MATCH_KEY)
    req_headers = {"X-TBA-Auth-Key": c.X_TBA_AUTH_KEY}

    resp = requests.get(req_url, req_headers)
    if resp.status_code == 200:
        data = json.loads(resp.text)
    else:
        raise RuntimeError("Bad error code: " + str(resp.status_code))

    out = {"cache-time": int(re.search(r"max-age=(\d+)", resp.headers["Cache-Control"]).group(1))}

    if data["qual"]["status"] == "playing":
        out["phase"] = "qual"
    else:
        out["phase"] = "playoffs"

    return out
