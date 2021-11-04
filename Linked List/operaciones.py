from node import Node

def first():
    head = None

    for count in range(1, 6):
        head = Node(count, head)

    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

    # búsqueda
    probe = head
    target_item = 2

    while probe != None and target_item != probe.data:
        probe = probe.next

    if probe != None:
        print(f'Target item {target_item} has been found')
    else:
        print(f'Target item {target_item} has not been found')

    
    # Reemplazo
    probe = head
    target_item = 3
    new_item = 'Z'

    while probe != None and target_item != probe.data:
        probe = probe.next
    
    if probe != None:
        probe.data = new_item
        print(f'{new_item} replaced the old value in the node number {target_item}')
    else:
        print(f'The target item {target_item} is not in the linked list')
    
    # Inserta al final
    head = Node('F', head)
    new_node = Node('K')

    if head is None:
        head = new_node
    else:
        probe = head

        while probe.next != None:
            probe = probe.next
        
        probe.next = new_node
    
    remove_item = head.data
    head = head.next
    print(remove_item)

    # Eliminar el último
    remove_item = head.data

    if head.next is None: # Si solo hay un nodo borra todo
        head = None
    else:
        probe = head

        while probe.next.next != None:
            probe = probe.next
        
        remove_item = probe.next.data
        probe.next = None
    print(remove_item)

    # Agregar un valor en una posición determinada
    new_item = input("Enter a new item")
    index = int(input("Enter the position to insert the new item: "))

    if head is None or index < 0:
        head = Node(new_item, head)
    else:
        probe = head

        while index > 1 and probe.next != None:
            probe = probe.next
            index-=1
        
        probe.next = Node(new_item, probe.next)

    # eliminar por indice
    index = 3
    if index <= 0 or head.next is None:
        remove_item = head.data
        head = head.next
        print(remove_item)
    else:
        probe = head

        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -=1
        
        removed_item = probe.next.data
        probe.next = probe.next.next

        print(removed_item)
    

first()
