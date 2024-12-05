"""
 Implement a Linked List
 """
 

def create_node(value):
    return {'value': value, 'next': None}

def insert_at_beginning(linked_list, value):
    new_node = create_node(value)
    new_node['next'] = linked_list['head']
    linked_list['head'] = new_node

def insert_at_end(linked_list, value):
    new_node = create_node(value)
    if linked_list['head'] is None:
        linked_list['head'] = new_node
    else:
        current = linked_list['head']
        while current['next'] is not None:
            current = current['next']
        current['next'] = new_node

def delete_node(linked_list, value):
    current = linked_list['head']
    prev = None
    while current is not None:
        if current['value'] == value:
            if prev is None:
                linked_list['head'] = current['next']
            else:
                prev['next'] = current['next']
            return
        prev = current
        current = current['next']

def traverse(linked_list):
    current = linked_list['head']
    while current is not None:
        print(current['value'], end=" -> ")
        current = current['next']
    print("None")

# Example usage:
if __name__ == '__main__':
    linked_list = {'head': None}
    
    insert_at_beginning(linked_list, 10)
    insert_at_end(linked_list, 20)
    insert_at_end(linked_list, 30)
    insert_at_beginning(linked_list, 5)
    
    print("Linked List:")
    traverse(linked_list)
    
    print("\nDeleting node with value 20:")
    delete_node(linked_list, 20)
    traverse(linked_list)
    
    print("\nDeleting node with value 5:")
    delete_node(linked_list, 5)
    traverse(linked_list)
