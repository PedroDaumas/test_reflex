#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint:disable=unused-import

"""
Reflex set up
"""
import os

import reflex as rx

# Frontend variables
frontend_port = os.environ.get("FE_PORT", 3000)

print("--------------- Frontend Configuration ------------------------")
print("Port: ", frontend_port)

# Websocket variables
backend_hostname = os.environ.get("WS_HOSTNAME", "0.0.0.0")
backend_port = os.environ.get("WS_PORT", 8000)
backend_protocol = os.environ.get("WS_PROTOCOL", "http")

url_hostname = "localhost" if backend_hostname == "0.0.0.0" else backend_hostname
backend_url = f"{backend_protocol}://{url_hostname}:{backend_port}"

print("--------------- Backend Configuration ------------------------")

print("Host: ", backend_hostname)
print("Port: ", backend_port)
print("Protocol: ", backend_protocol)
print("URL: ", backend_url)

print("--------------- Configuration Instance ------------------------")

config = rx.Config(
    app_name="app",
    frontend_port=frontend_port,
    backend_host=backend_hostname,
    backend_port=backend_port,
    api_url=backend_url,
    env=rx.Env.DEV,
)
