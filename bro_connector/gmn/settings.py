from main.localsecret import *
import os
import pathlib

demo = os.environ.get("BRO_ENVIRONMENT", True)
gmn_dir = pathlib.Path(__file__).parent.resolve()

gmn_SETTINGS = {
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
    "additions_dir": os.path.join(gmn_dir, "/additions"),
    "registrations_dir": os.path.join(gmn_dir, "/registrations"),
    "removals_dir": os.path.join(gmn_dir, "/removals"),
    "closures_dir": os.path.join(gmn_dir, "/closures"),
}