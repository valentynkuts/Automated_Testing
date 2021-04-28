from utils.testowa import Testowa
import pytest


class TestWindows:
    w = Testowa('Windows')
    testdata = [('hello /w', 'Something wrong.No description'),
                ('', 'Something wrong.No description'),
                ('del /p', 'Prompts for confirmation before deleting the specified file.'),
                ('time /?', 'Displays help at the command prompt.')]
    testData = [('Apple', 'Something wrong.No description'),
                ('Ubuntu', 'Something wrong.No description'),
                ('', 'Something wrong.No description')]

    # lab7
    @pytest.mark.parametrize("os, description", testData)
    def test_notWindows_OS(self, os, description):
        nw = Testowa(os)
        assert nw.userCommandDescription('time /?') == description

    @pytest.mark.parametrize("command, description", testdata)
    def test_windows_command(self, command, description):
        assert self.w.userCommandDescription(command) == description

    # lab6
    def test_notWindows(self):
        nw = Testowa('Apple')
        description = "Something wrong.No description"
        assert nw.userCommandDescription('time /?') == description

    def test_wrongCommand(self):
        description = "Something wrong.No description"
        assert self.w.userCommandDescription('hello /w') == description

    def test_del(self):
        description = "Prompts for confirmation before deleting the specified file."
        assert self.w.userCommandDescription('del /p') == description

    def test_time(self):
        description = "Displays help at the command prompt."
        assert self.w.userCommandDescription('time /?') == description

