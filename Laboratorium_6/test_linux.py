from testowa import Testowa


class TestLinux:
    l = Testowa('Linux')

    def test_notLinux(self):
        nl = Testowa('Apple')
        description = "Something wrong.No description"
        assert nl.userCommandDescription('') == description

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
