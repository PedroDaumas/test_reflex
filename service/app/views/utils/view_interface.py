#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ViewInterface(ABC):
    """Interface to create views"""

    @abstractmethod
    def build(self):
        """
        Function to build the Streamlit UI

        Returns
        -------
            self
        """
        raise NotImplementedError()
