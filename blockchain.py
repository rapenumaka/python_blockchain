blockchain =[[1]]

def add_value():
    blockchain.append(5.3)
    blockchain.append(3.4)
    print(blockchain)

# block chain model

def add_blockvalue():
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)


#add_value()

add_blockvalue()
add_blockvalue()
add_blockvalue()
add_blockvalue()


