# -*- coding: utf-8 -*-
from webium.controls.click import Clickable


__author__ = 'Roman Syrtsov (r_syrtsov@wargaming.net)'


class Checkbox(Clickable):
    """
    Implements logic to work with UI elements of type Checkbox
    """

    def check(self):
        """
        Performs click on Checkbox object if it is not already checked
        """
        self.set_checked(True)

    def uncheck(self):
        """
        Performs click on Checkbox object to uncheck selection marker
        """
        self.set_checked(False)

    def set_checked(self, value):
        u"""
        Sets the value of the checkbox to the given value.

        :Parameters:
          word : type=bool, required=True
            The value to be set.
        """
        if value != self.is_selected():
            self.click()
