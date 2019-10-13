def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    for i in plaintext:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if ('a' <= i <= 'w') or ('A' <= i <= 'W'):
                n = chr(ord(i)+3)
            else:
                n = chr(ord(i)-23)
        else:
                i += n
        plaintext = plaintext.replace(i, n)

    return plaintext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    for i in ciphertext:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if ('d' <= i <= 'z') or ('D' <= i <= 'Z'):
                n = chr(ord(i)-3)
            else:
                n = chr(ord(i)+23)
        else:
                i += n
        ciphertext = ciphertext.replace(i, n)
    return ciphertext