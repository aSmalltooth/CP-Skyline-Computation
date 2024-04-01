# Define nodes and conditional probability tables of CP-Net
cp_net = {
    'Response time': {
        'parents': [],
        'CPT': {'Response time<800': 1.0}
    },
    'Successability': {
        'parents': ['Response time'],
        'CPT': {'Response time<400': 'Successability>80', 'Response time>=400': 'Successability>90'}
    },
    'Throughput': {
        'parents': ['Response time'],
        'CPT': {'Response time<400': 'Throughput>5', 'Response time>=400': 'Throughput>8'}
    },
    'Latency': {
        'parents': ['Throughput'],
        'CPT': {'Throughput>5': 'Latency<20', 'Throughput>8': 'Latency<50'}
    }
}

class TreeNode:
    def __init__(self, condition=None, is_leaf=False, class_label=None):
        self.condition = condition
        self.is_leaf = is_leaf
        self.class_label = class_label
        self.children = {}

    def add_child(self, value, child):
        self.children[value] = child


def build_decision_tree(cp_net):
    root = TreeNode(condition='Response time < 800?')

    # Yes branch
    yes_node = TreeNode(condition='Response time < 400?')
    yes_node.add_child('Yes', TreeNode(condition='Successability > 80'))
    yes_node.children['Yes'].add_child('Throughput > 5', TreeNode(condition='Latency < 20', is_leaf=True, class_label='Class 1'))
    yes_node.children['Yes'].children['Throughput > 5'].add_child('Latency >= 20', TreeNode(is_leaf=True, class_label='Class 2'))
    yes_node.children['Yes'].add_child('Throughput <= 5', TreeNode(is_leaf=True, class_label='Class 3'))
    yes_node.add_child('No', TreeNode(condition='Successability > 90'))
    yes_node.children['No'].add_child('Throughput > 8', TreeNode(condition='Latency < 50', is_leaf=True, class_label='Class 4'))
    yes_node.children['No'].children['Throughput > 8'].add_child('Latency >= 50', TreeNode(is_leaf=True, class_label='Class 5'))
    yes_node.children['No'].add_child('Throughput <= 8', TreeNode(is_leaf=True, class_label='Class 6'))

    # No branch
    root.add_child('No', TreeNode(is_leaf=True, class_label='Class 7'))

    root.add_child('Yes', yes_node)

    return root


def classify_instance(instance, tree):
    if tree.is_leaf:
        return tree.class_label

    condition = tree.condition

    if condition in instance and instance[condition]:
        value = instance[condition]
        if value in tree.children:
            return classify_instance(instance, tree.children[value])
    return None


# 示例数据
data = [
    {'Response time < 800?': True, 'Response time < 400?': True, 'Successability > 80': True, 'Throughput > 5': True, 'Latency < 20': True},
    {'Response time < 800?': True, 'Response time < 400?': True, 'Successability > 80': True, 'Throughput > 5': True, 'Latency < 20': False},
    {'Response time < 800?': True, 'Response time < 400?': True, 'Successability > 80': True, 'Throughput > 5': False},
    {'Response time < 800?': True, 'Response time < 400?': False, 'Successability > 90': True, 'Throughput > 8': True, 'Latency < 50': True},
    {'Response time < 800?': True, 'Response time < 400?': False, 'Successability > 90': True, 'Throughput > 8': True, 'Latency < 50': False},
    {'Response time < 800?': True, 'Response time < 400?': False, 'Successability > 90': True, 'Throughput > 8': False},
    {'Response time < 800?': False}
]

# Build classification tree
decision_tree = build_decision_tree(cp_net)

# Classify sample data
for instance in data:
    class_label = classify_instance(instance, decision_tree)
    print(f"Instance: {instance}  Class: {class_label}")

# Print the nodes and conditional probability tables of CP-Net
for node, info in cp_net.items():
    print(f"{node}:")
    print(f"Parents: {info['parents']}")
    print("CPT:")
    for condition, result in info['CPT'].items():
        print(f"  {condition}: {result}")
    print()