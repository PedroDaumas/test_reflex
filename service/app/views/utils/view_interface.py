#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on sex mar 03 18:28:15 2023
@author ccavalcante
"""

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
