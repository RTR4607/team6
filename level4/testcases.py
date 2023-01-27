from level1.search_file import SearchFile
from level1.drive_finder import SystemDriveFinder
class TestCase:
    def test_Searchfile(self):
        obj=SearchFile()
        d=obj.find_file('one.txt','C:/')
        self.expected_filename=d[0]
        self.acutal_res='C:/Users\\user787\\PycharmProjects\\one.txt'
        assert self.expected_filename==self.acutal_res
    def test_searchdrive(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected == self.actual