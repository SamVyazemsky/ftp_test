import unittest
import ftplib
import os
import configparser


def upload_file(ftp, filename):
    ftp.cwd('test')
    file = open("C:/test.txt", 'r')
    ftp.storlines('STOR' + 'test123.txt', file)
    file.close()


def download_file(ftp, filename):
    ftp.cwd('test')
    filelist = ftp.nlst()
    if len(filelist) != 0:
        ftp.retrbinary("RETR " + filelist[0] ,open(filename, 'wb').write)
    filename.close()


class TestFtp(unittest.TestCase):
    """
    Tests for ftp
    """

    def setUp(self):
        """
        config ftp
        all settings are in settings.ini
        :return:
        """

        config = configparser.ConfigParser()
        config.read('settings.ini')
        ftp_settings = config['FTP']
        self.hostname = ftp_settings['hostname']
        self.login = ftp_settings['login']
        self.password = ftp_settings['password']
        self.name = ftp_settings['filename']
        self.ftp = ftplib.FTP(self.hostname)
        self.ftp.login(self.login, self.password)

    def test_upload_file(self):
        """
        test for uploading files to ftp-server
        path to file for upload in settings.ini(filename)
        ftp settings are in settings.ini
        :return:
        """
        upload_file(self.ftp, self.name)
        ftp = ftplib.FTP(self.hostname)
        ftp.login()
        file_list = ftp.nlst()
        (head, tail) = os.path.split( self.name )
        assert tail in file_list

    def test_download_file(self):
        """
        test for downloading file from ftp
        :return:
        """
        download_file(self.ftp, 'test.txt')
        assert 'test.txt' in os.listdir()

    def tearDown(self):
        """
        close ftp connection after tests finished
        :return:
        """
        self.ftp.close()


if __name__=='__main__':
    unittest.main()
