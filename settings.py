# thin-wrapper settings.py
import runpy, os

from wger.settings_global import WGER_SETTINGS

g = globals()
g.update(runpy.run_path("extras/docker/production/settings.py"))

WGER_SETTINGS["PROFILE_MIN_AGE_YEARS"] = int(os.getenv("PROFILE_MIN_AGE_YEARS", 0))
WGER_SETTINGS["PROFILE_MAX_AGE_YEARS"] = int(os.getenv("PROFILE_MAX_AGE_YEARS", -1)) # -1 = unlimited
