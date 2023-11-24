def get_record():
    record_file = open('record.txt', encoding='utf-8')
    record = int(record_file.read())
    record_file.close()
    return record


def write_record(new_record):
    record = get_record()
    record_file = open('record.txt', 'w', encoding='utf-8')
    if new_record > record:
        record_file.write(str(new_record))
        print('Новый рекорд!')
    else:
        record_file.write(str(record))
        print('Текущий рекорд:', record)
    record_file.close()
