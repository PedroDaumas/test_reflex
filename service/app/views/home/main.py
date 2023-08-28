#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import reflex as rx

from typing import List

from app.views.utils.view_interface import ViewInterface
from app.views.navbar import NavbarView
from app.views.footer import FooterView

from app.views.home.state import HomeState
from app.views.home.states.filter import FilterState
from app.views.home.states.export import ExportState

class HomePage(ViewInterface):
    """List users"""

    columns = [
        "User ID",
        "a",
        "b",
        "c",
        "d",
        "e",
    ]

    def create_user_table(self):
        """
        Builds the user table
        """

        return rx.table_container(
            rx.table(
                rx.thead(rx.tr(*[rx.th(column) for column in self.columns])),
                self.make_tbody(),
                variant="striped",
            ),
            width="100%",
        )

    def make_export_button(
        self, label_text, bg_color, size="sm", tag="add", is_disabled=False
    ):
        """
        Makes a new reflex button
        """
        # pylint: disable=too-many-arguments

        label = rx.hstack(rx.text(label_text, as_="b"), rx.icon(tag=tag))

        return rx.el.a(
            rx.button(
                label, size=size, bg=bg_color, is_disabled=is_disabled
            ),
            href="http://localhost:8000/export",
            target="_blank",
        )
    
    def make_heading_element(self, data, color="black", bg_color=None):
        """
        Returns the formatted heading
        """

        return rx.heading(
            data,
            color=color,
            bg=bg_color,
            font_size="10px",
            padding="2px 5px 2px 5px",
            width="100px",
            border_radius="15px",
            align="center",
        )

    def make_body_row(self, user: List[str]):
        """
        makes the table row using the user list data
        """

        user_id = rx.link(
            self.make_heading_element(user["user_id"]["data"], color="rgb(107,99,246)"),
            _as="button",
            is_external=True,
        )

        summary_columns = [
            "a",
            "b",
            "c",
            "d",
            "e",
        ]

        summaries = []

        for col in summary_columns:
            summaries.append(
                self.make_heading_element(
                    user[col]["data"],
                    color="white",
                    bg_color=user[col]["color"],
                )
            )

        data = [user_id, *summaries]

        return rx.tr(
            *[
                rx.td(d, key=user["user_id"]["data"], border_right="solid 2px #dedddc !important")
                for d in data
            ]
        )

    def make_tbody(self):
        """
        Makes the table body
        """
        # pylint: disable=unnecessary-lambda

        data = rx.foreach(HomeState.users, lambda user: self.make_body_row(user))

        return rx.tbody(data)

    def make_page_header(self):
        """
        Make the page header to show information about the data and other interaction buttons
        """

        user_count = rx.hstack(rx.text("Users found:", as_="b"), rx.text(HomeState.count, as_="b"))

        limit_select = rx.select(
            [1, 3, 10],
            value=FilterState.current_limit,
            on_change=FilterState.set_limit,
        )

        export_button = self.make_export_button(
            "Export",
            bg_color="orange",
            tag="download",
        )

        return rx.hstack(user_count, rx.spacer(), limit_select, export_button, width="100%")

    def build(self):
        """Build the view"""

        page_header = self.make_page_header()

        users_table = self.create_user_table()

        page = rx.vstack(
            page_header,
            users_table,
            padding_top="5rem",
            padding_left="10%",
            width="90%",
        )

        return rx.box(NavbarView().build(), page, FooterView().build())
