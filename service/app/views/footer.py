#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: skip-file

"""
Created on ter mar 21 21:39:31 2023
@author ccavalcante
"""
import json

import reflex as rx

from app.views.utils.view_interface import ViewInterface


class FooterView(ViewInterface):
    """Builds the app navbar"""

    def build(self):
        """Inheritdoc"""

        file = open("version.json", encoding="utf-8")

        v_file = json.load(file)

        home_link = rx.text(
            "Version: " + v_file["version"],
            font_size="10px",
            as_="b",
            padding_right="30px",
            padding_bottom="10px",
        )

        return rx.hstack(
            rx.spacer(),
            home_link,
            position="fixed",
            width="100%",
            bottom="0px",
            z_index="999",
        )
