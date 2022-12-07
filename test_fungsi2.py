from fungsi2 import *
# from unittest.mock import Mock
# import main
# =============================================

# dibaris line 32 pada fungsi2.py jika di exec( file ) dimatikan dan diganti dengan line 33 akan jalan semua 
# tetapi jika di line 32 nya yang dinyalakan maka tidak akan jalan 
# kemungkinan exec( file ) akan mengeksekusi dari file test_fungsi.py nya atau file test nya

# ketika exec( file ) dinyalakan maka test_script yang jalan hanya:
# - test_getNumberOfUppercaseWords
# - test_PrintFunction
# - test_coba3
# - test_coba7


def test_getNumberOfUppercaseWords(): # script jalan 1
    # number_of_character = "abc" # text chek nya harus ada huruf besar dan huruf kecil dan , .  seperti dibawah ini
    number_of_character = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."
    assert getNumberOfUppercaseWords(number_of_character)

def test_PrintFunction(): # script jalan 2
    data = getNumberOfUppercaseWords
    assert data

# def test_coba(): # script jalan 3
#     _list = line
#     assert getNumberOfUppercaseWords(_list)

# def test_coba1(): # script jalan 4
#     _list = counter
#     # print(_list)
#     assert getNumberOfUppercaseWords(_list)

# def test_coba2(): # script jalan 5
#     print(tokens)

def test_coba3(): # script jalan 6
    tokens = stemmer.stem
    print(tokens)
    # assert tokens

# def test_coba4(): # script warning tapi jalan
#     assert (counter, number_of_character, number_of_dollars, number_of_numeric, line, tokens, number_of_uppercase_word)


# def test_coba5(): # script jalan 7 (tidak manggil fungsi fungsi2.py)
#     # tokens = stemmer.stem
#     number_of_character = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."

#         # number_of_character = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."
#     tokens = line.split()
#     # line, number_of_character, tokens = getNumberOfUppercaseWords
#     assert number_of_character, tokens


# def test_coba6(): # script jalan 8
#     print(getNumberOfUppercaseWords(counter))

# def test_coba7(): # script jalan 9 
#     # file = test_getNumberOfUppercaseWords()
#     file = getNumberOfUppercaseWords
#     # text = file.insert(0,number_of_character)
#     # text = sys.stdin
#     # sys.stdin= file
#     text = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."
#     file = sys.stdin
#     assert file, text

def test_coba10():
    assert getNumberOfUppercaseWords

# def test_print_name(): # script gagal
#     name = 'Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...'
#     data = {'name': name}
#     file = Mock(get_json=Mock(return_value=data), args=data)

#     # Call tested function
#     assert getNumberOfUppercaseWords(file) == 'Hello {}!'.format(name)
