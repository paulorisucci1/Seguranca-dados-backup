import datetime
import shutil
import threading


class BackupManager:

    def __init__(self, backup_path, managed_files=[]):
        self.__backup_path = backup_path
        self.__managed_files = managed_files

    def add_managed_file (self, managed_file):
        self.__managed_files.append(managed_file)

    def remove_managed_file(self, managed_file_name):
        for index, file in enumerate(self.__managed_files):
            if file.name == managed_file_name:
                self.__managed_files.pop(index)
                break

    def do_backup(self, chosen_backup):
        available_backup = {
            "complete": self.complete_backup,
            "incremental": self.incremental_backup,
            "diferential": self.diferential_backup,
            "copy": self.copy_backup,
            "daily": self.daily_backup
        }

        if chosen_backup not in available_backup.keys():
            raise Exception('Backup invalido')

        available_backup[chosen_backup]()

    def complete_backup(self):
        for file in self.__managed_files:
            file.watch_modifications()
            shutil.copy(file.name, self.__backup_path)
            print('file ' + file.name + ' was succesfully copied!')

    def incremental_backup(self):
        for file in self.__managed_files:
            file.watch_modifications()
            if file.was_modified:
                shutil.copy(file.name, self.__backup_path)
                print('file '+file.name+ ' was succesfully copied!')

    def diferential_backup(self):
        for file in self.__managed_files:
            if file.was_modified:
                shutil.copy(file.name, self.__backup_path)
                print('file '+file.name+ ' was succesfully copied!')

    def copy_backup(self):
        for file in self.__managed_files:
            shutil.copy(file.name, self.__backup_path)
            print('file ' + file.name + ' was succesfully copied!')

    def daily_backup(self):
        date_time = str(input('Type the backup datetime: '))
        threading.Thread(target=self.__daily_backup, args=(date_time, )).start()

    def __daily_backup(self, date_time):
        try:
            backup_date_time = self.__threat_date_time(date_time)
            while datetime.datetime.today() < backup_date_time:
                continue
            self.diferential_backup()

        except Exception as e:
            print(e)

    # date-time example: 25-10-2022 00:55:00
    def __threat_date_time(self, date_time):
        date, time = date_time.split(' ')[0], date_time.split(' ')[1]

        day, month, year = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        hour, minute, second = time.split(':')[0], time.split(':')[1], time.split(':')[2]

        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
