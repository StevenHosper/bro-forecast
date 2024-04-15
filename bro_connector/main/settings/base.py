"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ("schema",)

from main.localsecret import *

ENVIRONMENT = "staging"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1b2-79o0!+@%9d6gt@7k5-8=8(r@&x-(15!o7+zo-zgwg4)gbv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "main",
    "gld",
    "gmw",
    "gmn",
    "frd",
    "rest_framework",
    "reversion",
    "reversion_compare",
    "admin_reorder",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django_admin_generator",
    "django_extensions",
    "django_plotly_dash.apps.DjangoPlotlyDashConfig",
    "django_static_jquery",
]

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        # ("mapCenterLocationName", "london"),
        (
            "GooglePlaceAutocompleteOptions",
            {"componentRestrictions": {"country": "netherlands"}},
        ),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "<google-api-key>",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "admin_reorder.middleware.ModelAdminReorder",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "django_plotly_dash.middleware.ExternalRedirectionMiddleware",
    "django_plotly_dash.middleware.BaseMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

if ENVIRONMENT == "production":
    demo = False
    welcome_sign = "Inloggen"
else:
    demo = True
    welcome_sign = "Inloggen (testomgeving)"


# BROCONVERTER SETTINGS
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
    "additions_dir": os.path.join(BASE_DIR, "gld/additions"),
    "startregistrations_dir": os.path.join(BASE_DIR, "gld/startregistrations"),
    "api_version": "v2",
}

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
    "registrations_dir": os.path.join(BASE_DIR, "gmw\\registrations"),
    "api_version": "v2",
}

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
    "additions_dir": os.path.join(BASE_DIR, "gmn/additions"),
    "registrations_dir": os.path.join(BASE_DIR, "gmn\\registrations"),
    "removals_dir": os.path.join(BASE_DIR, "gmn/removals"),
    "closures_dir": os.path.join(BASE_DIR, "gmn/closures"),
}

FRD_SETTINGS = {
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
    "api_version": "v2",
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASE_ROUTERS = ['database_routers.zeeland_gld.PostgresRouter']

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "test_db",
        "USER": s_user,
        "PASSWORD": s_password,
        "HOST": s_host,
        "PORT": s_port,
        "OPTIONS": {"options": "-c search_path=django_admin,public,gmw"},
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_FILES_LOCATION = "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

X_FRAME_OPTIONS = "SAMEORIGIN"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ADMIN_REORDER = (
    {
        "app": "gmn",
        "label": "Grondwatermonitoringnet (GMN)",
        "models": (
            "gmn.GroundwaterMonitoringNet",
            "gmn.MeasuringPoint",
            "gmn.IntermediateEvent",
            "gmn.gmn_bro_sync_log",
        ),
    },
    {
        "app": "gmw",
        "label": "Grondwatermonitoringput (GMW)",  # Provincie Zeeland GWM - Data
        "models": (
            "gmw.Map",
            "gmw.GroundwaterMonitoringWellStatic",
            "gmw.GroundwaterMonitoringWellDynamic",
            "gmw.GroundwaterMonitoringTubeStatic",
            "gmw.GroundwaterMonitoringTubeDynamic",
            "gmw.GeoOhmCable",
            "gmw.ElectrodeStatic",
            "gmw.ElectrodeDynamic",
            "gmw.Event",
            "gmw.Picture",
            "gmw.MaintenanceParty",
            "gmw.Maintenance",
            "gmw.Instantie",
        ),
    },
    {
        "app": "gld",
        "label": "Grondwaterstandsonderzoek (GLD)",
        "models": (
            "gld.Observation",
            "gld.GroundwaterLevelDossier",
            "gld.MeasurementPointMetadata",
            "gld.MeasurementTvp",
            "gld.ObservationMetadata",
            "gld.ObservationProcess",
            "gld.ResponsibleParty",
            "gld.TypeAirPressureCompensation",
            "gld.TypeCensoredReasonCode",
            "gld.TypeEvaluationProcedure",
            "gld.TypeInterpolationCode",
            "gld.TypeMeasurementInstrumentType",
            "gld.TypeObservationType",
            "gld.TypeProcessReference",
            "gld.TypeProcessType",
            "gld.TypeStatusCode",
            "gld.TypeStatusQualityControl",
            "gld.gld_registration_log",
            "gld.gld_addition_log",
        ),
    },
    {
        "app": "frd",
        "label": "Formatieweestand (FRD)",
        "models": (
            "frd.FormationResistanceDossier",
            "frd.CalculatedFormationresistanceMethod",
            "frd.FormationresistanceSeries",
            "frd.FormationresistanceRecord",
            "frd.GeoOhmMeasurementMethod",
            "frd.ElectromagneticMeasurementMethod",
            "frd.InstrumentConfiguration",
            "frd.MeasurementConfiguration",
            "frd.ElectrodePair",
            "frd.GMWElectodeReference",
            "frd.ElectromagneticSeries",
            "frd.ElectromagneticRecord",
            "frd.GeoOhmMeasurementValue",
            "frd.FrdSyncLog",
        ),
    },
)

if ENVIRONMENT == "production":
    demo = False
    welcome_sign = "Inloggen"
else:
    demo = True
    welcome_sign = "Inloggen (testomgeving)"


JAZZMIN_SETTINGS = {
    # "site_logo": os.path.join(BASE_DIR, "static/img/broconnector.png"),
    "site_logo": "img/broconnector.png",
    "welcome_sign": welcome_sign,
    # Links to put along the top menu
    "topmenu_links": [
        # model admin to link to (Permissions checked against model)
        {"name": "Map", "url": "/map", "permissions": ["auth.view_user"]},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "gmw"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "gmn"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "gld"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "frd"},
    ],
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/nens/bro-connector",
            "new_window": True,
        },
        {"model": "auth.user"},
    ],
    # Whether to aut expand the menu
    "navigation_expanded": False,
    "order_with_respect_to": [
        "auth",
        "gmn",
        "gmw",
        "gld",
        "frd",
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "gld": "fas fa-book-open",
        "gld.gld_registration_log": "fas fa-book",
        "gld.gld_addition_log": "fas fa-book-medical",
        "gld.Observation": "fas fa-search-location",
        "gld.GroundwaterLevelDossier": "fas fa-solid fa-folder",
        "gld.MeasurementPointMetadata": "fas fa-info",
        "gld.MeasurementTvp": "fas fa-exchange-alt",
        "gld.ObservationMetadata": "fas fa-info",
        "gld.ResponsibleParty": "fas fa-solid fa-building",
        "gld.TypeAirPressureCompensation": "fas fa-book-open",
        "gld.TypeCensoredReasonCode": "fas fa-book-open",
        "gld.TypeEvaluationProcedure": "fas fa-book-open",
        "gld.TypeInterpolationCode": "fas fa-book-open",
        "gld.TypeMeasurementInstrumentType": "fas fa-book-open",
        "gld.TypeObservationType": "fas fa-book-open",
        "gld.TypeProcessReference": "fas fa-book-open",
        "gld.TypeProcessType": "fas fa-book-open",
        "gld.TypeStatusCode": "fas fa-book-open",
        "gld.ObservationProcess": "fas fa-book-open",
        "gld.TypeStatusQualityControl": "fas fa-book-open",
        "gmw": "fas fa-search-location",
        "gmw.Map: fas fa-book-open"
        "gmw.GroundwaterMonitoringWellStatic": "fas fa-ruler-vertical",
        "gmw.GroundwaterMonitoringWellDynamic": "fas fa-ruler-vertical",
        "gmw.GroundwaterMonitoringTubeStatic": "fas fa-vials",
        "gmw.GroundwaterMonitoringTubeDynamic": "fas fa-vials",
        "gmw.GeoOhmCable": "fas fa-ethernet",
        "gmw.ElectrodeStatic": "fas fa-bolt",
        "gmw.ElectrodeDynamic": "fas fa-bolt",
        "gmw.Event": "fas fa-book-open",
        "gmw.Instantie": "fas fa-solid fa-building",
        "gmn": "fas fa-regular fa-object-group",
        "gmn.GroundwaterMonitoringNet": "fas fa-project-diagram",
        "gmn.MeasuringPoint": "fas fa-ruler-vertical",
        "gmn.IntermediateEvent": "fas fa-calendar",
        "gmn.gmn_bro_sync_log": "fas fa-sync",
        "frd": "fas fa-regular fa-bolt",
        "frd.FormationResistanceDossier": "fas fa-solid fa-folder",
        "frd.InstrumentConfiguration": "fas fa-server",
        "frd.ElectromagneticMeasurementMethod": "fas fa-book-open",
        "frd.GeoOhmMeasurementMethod": "fas fa-book-open",
        "frd.GeoOhmMeasurementValue": "fas fa-chart-line",
        "frd.GMWElectrodeReference": "fas fa-external-link-alt",
        "frd.ElectrodePair": "fas fa-vials",
        "frd.MeasurementConfiguration": "fas fa-server",
        "frd.ElectromagneticSeries": "fas fa-book-open",
        "frd.FormationresistanceSeries": "fas fa-book-open",
        "frd.ElectromagneticRecord": "fas fa-chart-line",
        "frd.FormationresistanceRecord": "fas fa-chart-line",
        # "gmw.GroundwaterMonitoringTubes": "fas fa-prescription-bottle",
    },
    "changeform_format_overrides": {"gmw.GroundwaterMonitoringWellStatic": "single"},
}

GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal307.dll"
GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"
