import urllib.parse

def decode(text):
    #encoded_str = 'Hell%C3%B6%20W%C3%B6rld%40Python'
    #encoded_str = input("Enter string to decode: ")
    #decoded_str = urllib.parse.unquote(encoded_str)
    return urllib.parse.unquote(text)
