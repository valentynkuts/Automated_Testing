from testowa import Testowa


class TestWindows:
    w = Testowa('Windows')

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
