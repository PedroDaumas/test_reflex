#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import reflex as rx

from typing import List, Dict

from app.views.utils.main_state import MainState


def empty(val):
    """
    Force the result to be None
    """
    # pylint: disable=unused-argument
    return None


class HomeState(MainState):
    """Manage user list info"""

    _mapped_users: Dict[str, Dict[str, Dict[str, str]]] = {}

    count: int = 0
    show: bool = False

    _columns = [
        ["user_id", empty],
        ["a", "gray"],
        ["b", "gray"],
        ["c", "gray"],
        ["d", "gray"],
        ["e", "gray"],
    ]

    @rx.var
    def users(self) -> List[Dict[str, Dict[str, str]]]:
        """
        Returns the users info from the _mapped_users attribute

        Return
        ------
            List[Dict]
        """

        if self._mapped_users == {}:
            return []

        return list(self._mapped_users.values())

    def clean_users(self):
        """
        Clean the mapped users
        """
        self._mapped_users = {}

    async def update_users(self, limit: int = 10, filters: dict = {}):
        """
        Update the users list
        """

        print(type(limit))  # THIS IS THE BUG
        print(type(filters))  # THIS IS THE BUG

        if self._mapped_users != {}:
            self.clean_users()

        yield

        self.count = 10
        data = {
            121: {
                "user_id": {"data": 121, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "not_enough_data", "color": "gray"},
            },
            346: {
                "user_id": {"data": 346, "color": None},
                "a": {"data": "low", "color": "green"},
                "b": {"data": 1, "color": "#a3baf6"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "low", "color": "green"},
            },
            568: {
                "user_id": {"data": 568, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "not_enough_data", "color": "gray"},
            },
            784: {
                "user_id": {"data": 784, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "low", "color": "green"},
            },
            910: {
                "user_id": {"data": 910, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "low", "color": "green"},
            },
            123: {
                "user_id": {"data": 123, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "low", "color": "green"},
            },
            456: {
                "user_id": {"data": 456, "color": None},
                "a": {"data": "not_enough_data", "color": "gray"},
                "b": {"data": 0, "color": "gray"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "low", "color": "green"},
            },
            789: {
                "user_id": {"data": 789, "color": None},
                "a": {"data": "low", "color": "green"},
                "b": {"data": 1, "color": "#a3baf6"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "high", "color": "red"},
            },
            154: {
                "user_id": {"data": 154, "color": None},
                "a": {"data": "low", "color": "green"},
                "b": {"data": 1, "color": "#a3baf6"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "medium", "color": "#f3d565"},
            },
            853: {
                "user_id": {"data": 853, "color": None},
                "a": {"data": "low", "color": "green"},
                "b": {"data": 1, "color": "#a3baf6"},
                "c": {"data": "not_enough_data", "color": "gray"},
                "d": {"data": "not_enough_data", "color": "gray"},
                "e": {"data": "medium", "color": "#f3d565"},
            },
        }

        self._mapped_users = {k: data[k] for k in list(data)[: int(limit)]}

        yield
