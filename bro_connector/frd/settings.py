from main.localsecret import *
import os
import pathlib

demo = os.environ.get("BRO_ENVIRONMENT", True)
frd_dir = pathlib.Path(__file__).parent.resolve()


frd_SETTINGS = {
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
    "demo": demo,
    "registrations_dir": os.path.join(frd_dir, "/registrations"),
    "api_version": "v2",
}