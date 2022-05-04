from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/8dcaa6d74a2345e9a79123cc62d1f5ba"

web3_baglanti = Web3(Web3.HTTPProvider(infura_url))

# bağlantıyı kontrol et
print(web3_baglanti.isConnected())

# son block numarası
print(web3_baglanti.eth.blockNumber)

# balance - hesaptaki eth miktarı

eth_hesabi = Web3.toChecksumAddress("0xda9dfa130df4de4673b89022ee50ff26f6ea73cf")
balance = web3_baglanti.eth.getBalance(eth_hesabi)
print(balance)

print(web3_baglanti.fromWei(balance,'ether'))
