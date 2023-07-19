class encryptionTools:
    def customEncryptString(str):
        for letter in str:
            add=[7,2,4,2,6,8,2,9,6,2,1,0,5,3,4,9]
            index=index+1
            num=ord(letter)+add[index]
            letter=chr(num)
            key=key+letter
        return key
    def customDecryptString(str):
        for letter in str:
            add=[7,2,4,2,6,8,2,9,6,2,1,0,5,3,4,9]
            index=index+1
            num=ord(letter)-add[index]
            letter=chr(num)
            key=key+letter
        return key