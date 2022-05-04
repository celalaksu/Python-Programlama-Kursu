from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3_ganache = Web3(Web3.HTTPProvider(ganache_url))
print(web3_ganache)

print(web3_ganache.eth.blockNumber)

gonderen_hesap = "0x562B2B98aaCF41BD5C61F6cc96A46ab0361a23f2"

alici_hesap = "0x7A2EF77c10a1844E16678fB097b5F589747e4E15"

private_key_gonderen_hesap = "905a856588e4698d56be4d876b76cfd245e08362afbe1f59a1e6b55824b8069d"

nonce = web3_ganache.eth.getTransactionCount(gonderen_hesap)

tx = {
    'nonce': nonce,
    'to': alici_hesap,
    'value': web3_ganache.toWei(2,'ether'),
    'gas':2000000,
    'gasPrice': web3_ganache.toWei('50','gwei')
}
# 1 ether 1000000000 gwei
signed_tx = web3_ganache.eth.account.signTransaction(tx, private_key_gonderen_hesap)

tx_hash = web3_ganache.eth.sendRawTransaction(signed_tx.rawTransaction)

print(tx_hash)
print(web3_ganache.toHex(tx_hash))
