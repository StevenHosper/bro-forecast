from main.localsecret import *
import os
import pathlib

demo = os.environ.get("BRO_ENVIRONMENT", True)
gmw_dir = pathlib.Path(__file__).parent.resolve()

gmw_SETTINGS = {
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
    "registrations_dir": os.path.join(gmw_dir, "\\registrations"),
    "api_version": "v2",
}

if __name__ == "__main__":
    print(gmw_dir)