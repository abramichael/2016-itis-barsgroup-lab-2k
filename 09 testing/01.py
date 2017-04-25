from datetime import datetime

from mock import Mock

mock_file = Mock()
mock_file.name = 'my_filename.doc'
mock_file.__iter__ = Mock(return_value=iter(["str1", "str2", "str3"]))

for line in mock_file:
    print line
