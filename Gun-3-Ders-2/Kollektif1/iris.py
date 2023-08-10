import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from solcx import compile_standard
from web3 import Web3

# Iris veri setini yükleme
iris = load_iris()
X, y = iris.data, iris.target

# Eğitim ve Test veri kümelerini ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#42 sadece id dir ve aynı test verileryle test edileceği anlamına gelir

# Ağ üzerinde kaç düğümün olacağını tanımlama
num_nodes = 10

# Her düğüm için modelleri depolamak üzere bir liste oluşturma
nodes = []
print(type(X_train))
# Her düğümdeki modelleri eğitme
for node_id in range(num_nodes):
    model = RandomForestClassifier()
    start_idx = node_id * len(X_train) // num_nodes
    end_idx = (node_id + 1) * len(X_train) // num_nodes

    inputs = X_train[start_idx:end_idx]
    labels = y_train[start_idx:end_idx]

    model.fit(inputs, labels)
    nodes.append(model)

# Solcx kullanarak Solidity akıllı sözleşmelerini derleyin
def compile_contract(contract_source_code):
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "contract.sol": {
                    "content": contract_source_code,
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "evm.bytecode"]
                    }
                }
            }
        }
    )
    return compiled_sol

# Solidity akıllı sözleşme kaynak kodu
contract_source_code = """
pragma solidity ^0.8.0;

contract RandomForestClassifier {
    uint256 private constant NUM_FEATURES = 4;
    uint256 private constant NUM_CLASSES = 3;
    uint256 private constant NUM_NODES = 5;
    
    uint256[NUM_NODES][NUM_FEATURES] private nodeModels;

    function train(uint256[NUM_FEATURES] memory input, uint256 label) public {
        uint256 node_id = input[0] % NUM_NODES;
        
        for (uint256 i = 0; i < NUM_FEATURES; i++) {
            nodeModels[node_id][i] = input[i];
        }
    }

    function predict(uint256[NUM_FEATURES] memory input) public view returns (uint256) {
        uint256 node_id = input[0] % NUM_NODES;

        uint256 predictedClass = 0;
        uint256 maxVotes = 0;
        uint256[NUM_CLASSES] memory combinedPredictions;

        for (uint256 i = 0; i < NUM_NODES; i++) {
            uint256 nodeClass = input[0] % NUM_CLASSES;
            combinedPredictions[nodeClass] += 1;

            if (combinedPredictions[nodeClass] > maxVotes) {
                maxVotes = combinedPredictions[nodeClass];
                predictedClass = nodeClass;
            }
        }

        return predictedClass;
    }
}

"""



# # uint256 private constant NUM_FEATURES = 4;
# # uint256 private constant NUM_CLASSES = 3;
# # uint256 private constant NUM_NODES = 5;

# #Bu özel sabitler, sınıflandırıcı modelinin boyutunu tanımlar. NUM_FEATURES, 
# #girdi özelliklerinin sayısını, NUM_CLASSES, sınıf sayısını ve NUM_NODES, rastgele ormanın düğüm sayısını belirtir.
# #Node dan kasıt evm node değil RFC için decision tree lerin ağaç node ları

# ###########################################################################################



# # uint256[NUM_NODES][NUM_FEATURES] private nodeModels;
# # Bu, her bir düğüm için özellik modelinin saklandığı bir 2 boyutlu dizi tanımlar. 
# # nodeModels[mode_id][feature_id], düğüm_id'ye sahip düğümün özellik modelini temsil eder.




# ###########################################################################################
# ###########################################################################################




# Solidity akıllı sözleşmesini derleme
compiled_contract = compile_contract(contract_source_code)

# Compile sözleşme ABI ve byte kodunu alma
contract_abi = compiled_contract["contracts"]["contract.sol"]["RandomForestClassifier"]["abi"]
contract_bytecode = compiled_contract["contracts"]["contract.sol"]["RandomForestClassifier"]["evm"]["bytecode"]["object"]



ganache_url = "http://localhost:7545"

# Yerel blockchain ağına bağlanın
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Varsayılan hesabı ayarlama (sözleşme deploy için gereklidir)
account = web3.eth.accounts[0]  # Update with your desired account index
web3.eth.defaultAccount = account

# Compile edilmiş sözleşmeyi blokzincire deploy etme
contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = contract.constructor().transact({'from': account})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt["contractAddress"]

print("Sözleşmenin Deploy Edildiği Adres:", contract_address)

# Düğümler arasındaki iletişimi ve senkronizasyonu yapılandırma (ör. mesajlaşma veya konsensüs mekanizmalarını kullanarak)
# Bu örnekte, ana düğümün model parametrelerini diğer düğümlere dağıttığı basit bir merkezi yaklaşım kullanılıyor

# Ana düğümü lider olarak tanımlama
is_leader = True

# Verileri ve eğitim sürecini düğümler arasında dağıtma
batch_size = len(X_train) // num_nodes  # Düğüm başına yığın boyutu

# “batch_size” parametresi; eğitim veya test sırasında girdi bilgilerinin tek tek değil bir grup halinde eğitime sokulmasını sağlamaktadır. Verilen değerler ağın başarısına göre değiştirilebilmektedir. 
# “epochs” parametresi; veri setinin modele kaç kez gireceğini belirtmek için kullanılmaktadır.

# Her düğümde eğitim gerçekleştirme
for epoch in range(10):  # Eğitim tur sayısı
    # Iterate over the training data on each node
    for node_id in range(num_nodes):
        start_idx = node_id * batch_size
        end_idx = start_idx + batch_size

        inputs = X_train[start_idx:end_idx]
        labels = y_train[start_idx:end_idx]

        if is_leader:
            # Lider düğümün modelini eğitin
            nodes[node_id].fit(inputs, labels)
        else:
            # Diğer düğümlerin modellerini eğitin
            # Düğüm ID sini, girişleri ve etiketleri geçen sözleşmenin eğitim fonksiyonun çağırma
            contract.functions.train(node_id, inputs[0], labels[0]).transact({'from': account})

    if is_leader:
        # Model parametrelerini düğümler arasında senkronize etme
        global_weights = [node.get_params() for node in nodes]

        for node_id in range(num_nodes):
            # Her düğümde güncellenen model parametrelerini ayarlama
            nodes[node_id].set_params(**global_weights[node_id])


    else:
        # Receive the updated model parameters from the leader node
        leader_params = contract.functions.getParams().call()
        nodes[0].set_params(leader_params)

# Modeli test verileri üzerinde değerlendirme
predictions = nodes[0].predict(X_test)
accuracy = sum(predictions == y_test) / len(y_test)
print("Test Doğruluğu:", accuracy)
