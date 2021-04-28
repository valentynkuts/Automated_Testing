from utils.testowa import Testowa
import pytest


class TestLinux:
    l = Testowa('Linux')
    testdata = [('hello /w', 'Something wrong.No description'),
                ('', 'Something wrong.No description'),
                ('ls -a', 'To display all files including the hidden files.'),
                ('cd ~', 'Navigate to HOME directory')]
    testData = [('Apple', 'Something wrong.No description'),
                ('Ubuntu', 'Something wrong.No description'),
                ('', 'Something wrong.No description')]

    # lab7
    @pytest.mark.parametrize("os, description", testData)
    def test_notLinux_OS(self, os, description):
        nl = Testowa(os)
        assert nl.userCommandDescription('ls -a') == description

    @pytest.mark.parametrize("command, description", testdata)
    def test_linux_command(self, command, description):
        assert self.l.userCommandDescription(command) == description

    # lab6
    def test_notLinux(self):
        nl = Testowa('Apple')
        description = "Something wrong.No description"
        assert nl.userCommandDescription('ls -a') == description

    def test_wrongCommand(self):
        description = "Something wrong.No description"
        assert self.l.userCommandDescription('hello /w') == description

    def test_ls(self):
        description = "To display all files including the hidden files."
        assert self.l.userCommandDescription('ls -a') == description

    def test_cd(self):
        description = "Navigate to HOME directory"
        assert self.l.userCommandDescription('cd ~') == description

    def test_ps(self):
        data = self.l.getData()
        assert self.l.userCommandDescription('ps --ppid') == data['ps']['--ppid']
