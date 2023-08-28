#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on qua ago 02 08:51:56 2023
@author ccavalcante
"""

import reflex as rx

from app.views.home.states.filter import FilterState


class ExportState(FilterState):
    """
    State to manage export
    """

    def download(self):
        """
        Redirects to the export route
        """

        return rx.redirect("http://localhost:8000/export")
