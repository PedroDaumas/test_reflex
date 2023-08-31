#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on sáb jul 29 14:29:39 2023
@author ccavalcante
"""
import reflex as rx

from app.views.home.state import HomeState


class FilterState(HomeState):
    """
    State used to manage filter configuration
    """

    limit: int = 10

    user_filter = {}

    @rx.var
    def current_limit(self) -> str:
        """
        Returns the active page converted to string
        """
        return str(self.limit)

    def set_limit(self, limit=10):
        """
        Set a new filter limit and update the users data
        """
        self.limit = limit

        return self.update_users(self.limit, self.user_filter)
