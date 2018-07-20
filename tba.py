from typing import Dict, Any
import requests
import json
import re
import enum

import configuration as c


class Phases(enum.Enum):
    NOT_STARTED = 0
    QUAL = 1
    ALLIANCE = 2
    PLAYOFF = 3
    LOST_IN_QUAL = 4
    LOST_IN_PLAYOFF = 5
    WINNER = 6


def get_current_phase() -> Dict[str, Any]:
    req_url = "https://www.thebluealliance.com/api/v3/team/{}/event/{}/status".format(c.TEAM_KEY, c.MATCH_KEY)
    req_headers = {"X-TBA-Auth-Key": c.X_TBA_AUTH_KEY}

    resp = requests.get(req_url, req_headers)
    if resp.status_code == 200:
        data = json.loads(resp.text)
    else:
        raise RuntimeError("Bad error code: " + str(resp.status_code))

    out = {"cache-time": int(re.search(r"max-age=(\d+)", resp.headers["Cache-Control"]).group(1))}

    if "playoff" in data:
        if data["playoff"]["status"] == "playing":
            out["phase"] = Phases.PLAYOFF
        elif data["playoff"]["status"] == "won":
            out["phase"] = Phases.WINNER
        else:
            out["phase"] = Phases.LOST_IN_PLAYOFF
    elif "qual" in data:
        if data["qual"]["status"] == "completed":
            out["phase"] = Phases.LOST_IN_QUAL
        else:
            out["phase"] = Phases.QUAL
    else:
        out["phase"] = Phases.NOT_STARTED

    return out
