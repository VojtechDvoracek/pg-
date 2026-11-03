
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    with open(file_name, 'rb') as f:
        header = f.read(header_length)
    return header


def is_jpeg(file_name):
       # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    # vyhodnoť zda je soubor jpeg
    if header == jpeg_header:
        return True
    return False


def is_gif(file_name):

    # načti hlavičku souboru
    header = read_header(file_name, len(gif_header1))

    # vyhodnoť zda je soubor gif
    if header == gif_header1 or header == gif_header2:
        return True
    return False


def is_png(file_name):
    # načti hlavičku souboru
    header = read_header(file_name, len(png_header))

    # vyhodnoť zda je soubor png
    if header == png_header:
        return True
    return False


def print_file_type(file_name):
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    file_name = "kitten"
    print_file_type(file_name)