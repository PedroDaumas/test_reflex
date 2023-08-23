#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on ter mar 21 21:39:31 2023
@author ccavalcante
"""
import reflex as rx

from app.views.utils.view_interface import ViewInterface


class NavbarView(ViewInterface):
    """Builds the app navbar"""

    def build(self):
        """Inheritdoc"""

        home_link = rx.link(
            rx.heading("APP", color="white", size="lg"),
            href="/",
            padding_left="2rem",
            padding_top="2px",
            padding_bottom="2px",
        )

        return rx.hstack(
            home_link,
            rx.spacer(),
            border_bottom_width="2px",
            background_color="white",
            position="fixed",
            width="100%",
            top="0px",
            bg_color="#b32a00",
            z_index="999",
        )
