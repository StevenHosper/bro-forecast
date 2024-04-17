from main.localsecret import *
import os
import pathlib

demo = os.environ.get("BRO_ENVIRONMENT", True)
gld_dir = pathlib.Path(__file__).parent.resolve()

gld_SETTINGS = {
    "bro_info_demo": {
        "projectnummer": 1,
        "token": {
            "user": bro_demo_user,
            "pass": bro_demo_password,
        },
    },
    "bro_info_bro_connector": {
        "token": {
            "user": bro_user,
            "pass": bro_password,
        },
    },
    "monitoringnetworks": None,
    "demo": demo,
    "additions_dir": os.path.join(gld_dir, "/additions"),
    "startregistrations_dir": os.path.join(gld_dir, "/startregistrations"),
    "api_version": "v2",
}
