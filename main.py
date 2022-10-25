from backup_manager import BackupManager
from file import File

file_test = File('/home/paulo/Documents/QUARTO_PERIODO/seguranca_dados/backup_project/directory/test.txt')

managed_files = []
managed_files.append(file_test)

backup_path = '/home/paulo/Documents/QUARTO_PERIODO/seguranca_dados/backup_project/backup'
backup_manager = BackupManager(backup_path, managed_files)


while True:
    try:
        chose_backup = input('Which backup would you like to do? ')
        backup_manager.do_backup(chose_backup)
    except Exception as e:
        print(e)
