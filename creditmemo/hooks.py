# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "creditmemo"
app_title = "Credit Memo"
app_publisher = "AgriTheory"
app_description = "Credit Memo"
app_icon = "assets/creditmemo/images/aticonw.svg",
app_color = "#000000",
app_email = "tyler@agritheory.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/creditmemo/css/creditmemo.css"
# app_include_js = "/assets/creditmemo/js/creditmemo.js"
# app_include_js = "/assets/creditmemo/images/aticon.svg"

# include js, css files in header of web template
# web_include_css = "/assets/creditmemo/css/creditmemo.css"
# web_include_js = "/assets/creditmemo/js/creditmemo.js"
# web_include_js = "/assets/creditmemo/images/aticon.svg"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "creditmemo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "creditmemo.install.before_install"
# after_install = "creditmemo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "creditmemo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"creditmemo.tasks.all"
# 	],
# 	"daily": [
# 		"creditmemo.tasks.daily"
# 	],
# 	"hourly": [
# 		"creditmemo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"creditmemo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"creditmemo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "creditmemo.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "creditmemo.event.get_events"
# }
