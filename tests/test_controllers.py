#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

tests/test_controllers.py - Units tests for the controllers package
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import getpass

import models
import controllers
from utils import Database

#-----------------------------------------------------------------------------
# Tests for : controllers.Config
#-----------------------------------------------------------------------------
class TestConfig:
    """
    Tests for the config controller
    """

    def test_run_valid(self, monkeypatch):
        """
        Tests the configuration assistant with valid parameters.
        Success conditions :
        - The database has been created and contains the new data
        """
        # Monkeypatch : inputs
        def input_monkeypatched(phrase):
            """
            Returns what input() should have returned : valid inputs
            """
            if phrase == "Shall we use a buzzer (Y/N) : ":
                return "Y"

            if phrase == "On which GPIO port is the buzzer connected : ":
                return "7"

            if phrase == "Camera resolution, WIDTH (500 by default) : ":
                return "500"

            if phrase == "Camera resolution, HEIGHT (500 by default) : ":
                return "500"

            if phrase == "Please define a password for Jean-Pierre : ":
                return "1234abcd"

        monkeypatch.setitem(__builtins__, 'input', input_monkeypatched)
        getpass.getpass == input_monkeypatched

        # Connect to the dummy database
        Database.on(is_test=True)

        # Launch
        controllers.Config.execute()

        # Test
        params = models.Params()
        assert params.buzzer_on == 1
        assert params.buzzer_port == 7
        assert params.camera_res_x == 500
        assert params.camera_res_y == 500
        assert params.user_password
        assert params.flask_secret_key

    @classmethod
    def input_monkeypatched_valid(cls, phrase):
        """
        Returns what input() should have returned : valid inputs
        """
        if phrase == "Shall we use a buzzer (Y/N) : ":
            return 'Y'

        if phrase == "On which GPIO port is the buzzer connected : ":
            return '7'

        if phrase == "Camera resolution, WIDTH (500 by default) : ":
            return 500

        if phrase == "Camera resolution, HEIGHT (500 by default) : ":
            return 500

        if phrase == "Please define a password for Jean-Pierre : ":
            return "1234abcd"
