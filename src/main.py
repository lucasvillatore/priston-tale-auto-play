import time
from src.dependency_provider import DependencyProvider
from src.infra.win32 import keys

def main():

    dependency_provider = DependencyProvider()
    
    rebuff_use_case = dependency_provider.get_rebuff_use_case()
    fill_potions_use_case = dependency_provider.get_fill_potions_use_case()
    attack_use_case = dependency_provider.get_attack_use_case()
    use_potion_use_case = dependency_provider.get_use_potion_use_case()
    collect_dropped_item_use_case = dependency_provider.get_collect_dropped_item_use_case()
    actions_queue = dependency_provider.get_actions_queue()

    buffs = [
        keys.VK_F2,  
        keys.VK_F3,  
        keys.VK_F4,  
        keys.VK_F5, 
        keys.VK_F6,  
    ]


    actions_queue.add_action(fill_potions_use_case, None, delay=5)

    for buff in buffs:
        print(f"Adding buff {buff} to actions queue")
        actions_queue.add_action(rebuff_use_case, buff, delay=1.5)
    actions_queue.add_action(attack_use_case, keys.VK_F1, (929, 500), delay=0.5)
    actions_queue.add_action(use_potion_use_case, keys.VK_1, delay=0.5)
    actions_queue.add_action(collect_dropped_item_use_case, (1175, 125), delay=5)
    time.sleep(2)

    while True:
        print("Waiting for actions...")
        if actions_queue.has_action():
            action = actions_queue.get_next_action()
            if action is not None:
                use_case = action.get('action')
                args = action.get('args', None)
                delay = action.get('delay', 0)

                if use_case is not None:
                    if args is not None:
                        use_case.execute(*args)
                    else:
                        use_case.execute()
                    time.sleep(delay)
