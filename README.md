# pyautoeios

Wrapper for libRemoteInput library and port of the lape library from [Brandon-T/Reflection][reflection].

### Alpha Status

**everything** is subject to change in
future releases. This is because I want the 1.0.0 release to actually be
something people like using.

That said. I welcome your usage and feedback so we can make this a good library
for boting.

Even if things will change before the 1.0.0 release, once something is in version
control or pypi, its there forever. I have no intention of deleteing commits from
github. (unless I am forced to by some lawyer somewhere)


### why are you making this?

I think programming should be fun and enjoyable. For me, python is the fun
language and botting games is a fun activiity. It allows an individual to remove
the un fun "grind" of the game.


### what are the features?

- [x] Works with python 3.8
- [x] installable via pip
- [x] Wraps well liked [pyautogui](https://github.com/asweigart/pyautogui/) interface
- [x] Transparent Image finding *when opencv is installed*
- [x] Injecting into multiple clients (so threads can be used for multi-boxing)
- [x] no *known* memory leaks.
- [x] pytest for unit testing as I go
- [x] login method


### what are you planning on adding?


###### top priority features

- [ ] Pip install dependancies for you (for now use the [Pipfile](/Pipfile))
- [ ] Examples?
- [ ] porting of "reflection" modules from https://github.com/Brandon-T/Reflection

###### lower priority

- [ ] Login screen world switcher logic
- [ ] integration of color and other methods https://github.com/BenLand100/srbot/tree/master/srbot
- [ ] porting modules from https://github.com/SRL/SRL or https://github.com/ollydev/SRL-Development


### how would I use this?

check the [examples](examples) folder for various little snippets.
I add new examples as I port more and more of [reflection] and add new methods.

here's something simple:

```python
import getpass
import pyautoeios as pyauto

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    password = getpass.getpass()
    email = input("enter your username:")
    im = pyauto.screenshot()
    im.show()
    pyauto.static.login(client, email, password)
    im = pyauto.screenshot()
    im.show()
```


## Progess Tracking


#### General Plan of TODOs:
- [ ] write more tests for code already written (goal is at least 80% test coverage)
- [ ] Finish port of `Internal`

- [ ] Interfaces for grand exchange

- [ ] Port Interfaces for bank standing skills
  - [ ] Port `Inventory.simba` -> `inventory.py`
  - [ ] Port `Bank.simba` -> `bank.py`

- [ ] Port Interfaces for smithing skills
  - [ ] Port `Interfaces.simba` -> `interfaces.py`
  - [ ] Port `Bank.simba` -> `bank.py`



#### Progess of wrapping of Remote Input[¹] ![66%](https://progress-bar.dev/66)

| DLL Method | Python Method | Percent | Notes |
| --- | --- | --- | --- |
| `EIOS_ReleaseTarget` | `eios.EIOS.release_target` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetTargetDimensions` | `eios.EIOS.get_target_dimensions` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetImageBuffer` | `eios.EIOS.get_image_buffer` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetDebugImageBuffer` | `eios.EIOS.get_debug_image_buffer` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_SetGraphicsDebugging` | `eios.EIOS.set_graphics_debugging` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_UpdateImageBuffer` | `eios.EIOS.update_image_buffer` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_HasFocus` | `eios.EIOS.has_focus` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GainFocus` | `eios.EIOS.gain_focus` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_LoseFocus` | `eios.EIOS.lose_focus` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_IsInputEnabled` | `eios.EIOS.is_input_enabled` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_SetInputEnabled` | `eios.EIOS.set_input_enabled` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetMousePosition` | `eios.EIOS.get_mouse_position` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetRealMousePosition` | `eios.EIOS.get_real_mouse_position` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_MoveMouse` | `eios.EIOS.move_mouse` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_HoldMouse` | `eios.EIOS.hold_mouse` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_ReleaseMouse` | `eios.EIOS.release_mouse` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_ScrollMouse` | `eios.EIOS.scroll_mouse` | ![100%](https://progress-bar.dev/100) |  |
| ~~`EIOS_IsMouseButtonHeld`~~ | ~~`eios.EIOS.is_mouse_button_held`~~ | ![0%](https://progress-bar.dev/0) | *function doesn't exist in dll* |
| `EIOS_SendString` | `eios.EIOS.send_string` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_HoldKey` | `eios.EIOS.hold_key` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_ReleaseKey` | `eios.EIOS.release_key` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_IsKeyHeld` | `eios.EIOS.is_key_held` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_GetKeyboardSpeed` | `eios.EIOS.get_keyboard_speed` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_SetKeyboardSpeed` | `eios.EIOS.set_keyboard_speed` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_GetKeyboardRepeatDelay` | `eios.EIOS.get_keyboard_repeat_delay` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_SetKeyboardRepeatDelay` | `eios.EIOS.set_keyboard_repeat_delay` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_PairClient` | `eios.EIOS.pair_client` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_KillClientPID` | `eios.EIOS.kill_client_pid` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_KillClient` | `eios.EIOS.kill_client` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_KillZombieClients` | `eios.EIOS.kill_zombie_clients` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `EIOS_GetClients` | `eios.EIOS.get_clients` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_GetClientPID` | `eios.EIOS.get_client_pid` | ![100%](https://progress-bar.dev/100) |  |
| `EIOS_Inject` | `eios.EIOS.inject | | ![100%](https://progress-bar.dev/100) ` |
| `EIOS_Inject_PID` | `eios.EIOS.inject_pid` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_GetEIOS` | `eios.EIOS.get_eios` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Object` | `eios.EIOS.get_object` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_IsSame_Object` | `eios.EIOS.is_same_object` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_InstanceOf` | `eios.EIOS.instance_of` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Release_Object` | `eios.EIOS.release_object` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Release_Objects` | `eios.EIOS.release_objects` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Bool` | `eios.EIOS.get_bool` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Char` | `eios.EIOS.get_char` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Byte` | `eios.EIOS.get_byte` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Short` | `eios.EIOS.get_short` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Int` | `eios.EIOS.get_int | | ![100%](https://progress-bar.dev/100) ` |
| `Reflect_Long` | `eios.EIOS.get_long` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Float` | `eios.EIOS.get_float` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Double` | `eios.EIOS.get_double` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_String` | `eios.EIOS.get_string` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Array` | `eios.EIOS.get_array` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Array_With_Size` | `eios.EIOS.get_array_with_size` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Array_Size` | `eios.EIOS.get_array_size` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Array_Index` | `eios.EIOS.get_array_from_pointer` and `eios.EIOS.get_array_index_from_pointer` | ![100%](https://progress-bar.dev/100) |  |
| `Reflect_Array_Index2d` | `eios.EIOS.get_2d_array_index_from_pointer` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Array_Index3d` | `eios.EIOS.get_3d_array_index_from_pointer` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |
| `Reflect_Array_Index4d` | `eios.EIOS.get_4d_array_index_from_pointer` | ![50%](https://progress-bar.dev/50) | *written. needs tested* |



#### Progess of porting [reflection] ![25%](https://progress-bar.dev/25)

| Simba File | Python file | Percent | Notes |
| --- | --- | --- | --- |
| `Antiban.simba` | [antiban.py](src/pyautoeios/antiban.py) | ![0%](https://progress-bar.dev/0) | |
| `Bank.simba` | [bank.py](src/pyautoeios/bank.py) | ![0%](https://progress-bar.dev/0) | |
| `Chat.simba` | [chat.py](src/pyautoeios/chat.py) | ![0%](https://progress-bar.dev/0) | |
| `Combat.simba` | [combat.py](src/pyautoeios/combat.py) | ![0%](https://progress-bar.dev/0) | |
| `Constants.simba` | [_internal/constants.py](src/pyautoeios/_internal/constants.py) | ![100%](https://progress-bar.dev/100) | |
| `Equipment.simba` | [equipment.py](src/pyautoeios/equipment.py) | ![0%](https://progress-bar.dev/0) | |
| `GameTab.simba` | [game_tab.py](src/pyautoeios/game_tab.py) | ![0%](https://progress-bar.dev/0) | |
| `Ground.simba` | [ground.py](src/pyautoeios/ground.py) | ![0%](https://progress-bar.dev/0) | |
| `Interfaces.simba` | [interfaces.py](src/pyautoeios/interfaces.py) | ![0%](https://progress-bar.dev/0) | |
| `Internal/Functions.simba` | N/A | ![75%](https://progress-bar.dev/75) |  *merging into rs_structures* |
| `Internal/Hooks.simba`  | [hooks.py](src/pyautoeios/hooks.py)  | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSActor.simba` | [_internal/rs_actor.py](src/pyautoeios/_internal/rs_actor.py) | ![25%](https://progress-bar.dev/25) | |
| `Internal/RSAnimableNode.simba` | [_internal/rs_animable_node.py](src/pyautoeios/_internal/rs_animable_node.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSAnimatedModel.simba` | [_internal/rs_animated_model.py](src/pyautoeios/_internal/rs_animated_model.py) | ![10%](https://progress-bar.dev/0) | |
| `Internal/RSAnimation.simba` | [_internal/rs_animation.py](src/pyautoeios/_internal/rs_animation.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSAnimationFrame.simba` | [_internal/rs_animation_frame.py](src/pyautoeios/_internal/rs_animation_frame.py) | ![10%](https://progress-bar.dev/0) | |
| `Internal/RSAnimationSequence.simba` | [_internal/rs_animation_sequence.py](src/pyautoeios/_internal/rs_animation_sequence.py) | ![10%](https://progress-bar.dev/0) | |
| `Internal/RSAnimationSkeleton.simba` | [_internal/rs_animation_skeleton.py](src/pyautoeios/_internal/rs_animation_skeleton.py) | ![10%](https://progress-bar.dev/0) | |
| `Internal/RSCache.simba` | [_internal/rs_cache.py](src/pyautoeios/_internal/rs_cache.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSCamera.simba` | [_internal/rs_camera.py](src/pyautoeios/_internal/rs_camera.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSClient.simba` | [_internal/rs_client.py](src/pyautoeios/_internal/rs_client.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSCombatInfo.simba` | [_internal/rs_combat_info.py](src/pyautoeios/_internal/rs_combat_info.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSConstants.simba` | [_internal/constants.py](src/pyautoeios/_internal/constants.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSEntity.simba` | [_internal/rs_entity.py](src/pyautoeios/_internal/rs_entity.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSGameShell.simba` | [_internal/rs_game_shell.py](src/pyautoeios/_internal/rs_game_shell.py) | ![10%](https://progress-bar.dev/0) | |
| ~~`Internal/RSGraphics.simba`~~ | N/A | ![0%](https://progress-bar.dev/0) | *No plans to implement* |
| `Internal/RSGroundObject.simba` | [_internal/rs_ground_object.py](src/pyautoeios/_internal/rs_ground_object.py) | ![10%](https://progress-bar.dev/0) | |
| `Internal/RSHashTable.simba` | [_internal/rs_hash_table.py](src/pyautoeios/_internal/rs_hash_table.py) | ![60%](https://progress-bar.dev/60) | |
| `Internal/RSItem.simba` | [_internal/rs_item.py](src/pyautoeios/_internal/rs_item.py) | ![80%](https://progress-bar.dev/80) | |
| `Internal/RSItemDefinition.simba` | [_internal/rs_item_definition.py](src/pyautoeios/_internal/rs_item_definition.py) | ![80%](https://progress-bar.dev/80) | |
| `Internal/RSItemNode.simba` | [_internal/rs_item_node.py](src/pyautoeios/_internal/rs_item_node.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSIterableHashTable.simba` | [_internal/rs_iterable_hash_table.py](src/pyautoeios/_internal/rs_iterable_hash_table.py) | ![60%](https://progress-bar.dev/60) | |
| `Internal/RSLinkedList.simba` | [_internal/rs_linked_list.py](src/pyautoeios/_internal/rs_linked_list.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSLocalPlayer.simba` | [_internal/rs_local_player.py](src/pyautoeios/_internal/rs_local_player.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSMath.simba` | N/A | ![0%](https://progress-bar.dev/0) |  *merging logic into static and relevant classes* |
| `Internal/RSModel.simba` | [_internal/rs_model.py](src/pyautoeios/_internal/rs_model.py) | ![20%](https://progress-bar.dev/20) | |
| `Internal/RSNameInfo.simba` | [_internal/rs_name_info.py](src/pyautoeios/_internal/rs_name_info.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSNode.simba` | [_internal/rs_node.py](src/pyautoeios/_internal/rs_node.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSNodeDeque.simba` | [_internal/rs_node_deque.py](src/pyautoeios/_internal/rs_node_deque.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSNPC.simba` | [_internal/rsnpc.py](src/pyautoeios/_internal/rsnpc.py) | ![10%](https://progress-bar.dev/10) | |
| `Internal/RSNPCDefinition.simba` | [_internal/rsnpc_definition.py](src/pyautoeios/_internal/rsnpc_definition.py) | ![80%](https://progress-bar.dev/80) | |
| `Internal/RSObject.simba` | [_internal/rs_object.py](src/pyautoeios/_internal/rs_object.py) | ![20%](https://progress-bar.dev/20) | |
| `Internal/RSObjectDefinition.simba` | [_internal/rs_object_definition.py](src/pyautoeios/_internal/rs_object_definition.py) | ![80%](https://progress-bar.dev/80) | |
| `Internal/RSPlayer.simba` | [_internal/rs_player.py](src/pyautoeios/_internal/rs_player.py) | ![60%](https://progress-bar.dev/60) | |
| `Internal/RSPlayerDefinition.simba` | [_internal/rs_player_definition.py](src/pyautoeios/_internal/rs_player_definition.py) | ![70%](https://progress-bar.dev/70) | |
| `Internal/RSQueue.simba` | [_internal/rs_queue.py](src/pyautoeios/_internal/rs_queue.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSRegion.simba` | [_internal/rs_region.py](src/pyautoeios/_internal/rs_region.py) | ![10%](https://progress-bar.dev/10) | |
| `Internal/RSSceneTile.simba` | [_internal/rs_scene_tile.py](src/pyautoeios/_internal/rs_scene_tile.py) | ![70%](https://progress-bar.dev/70) | |
| `Internal/RSStructures.simba` | [_internal/rs_structures.py](src/pyautoeios/_internal/rs_structures.py) | ![90%](https://progress-bar.dev/90) | |
| `Internal/RSText.simba` | N/A | ![100%](https://progress-bar.dev/0) |  *merged logic into static and relevant classes* |
| `Internal/RSTile.simba` | [_internal/rs_tile.py](src/pyautoeios/_internal/rs_tile.py) | ![30%](https://progress-bar.dev/30) | |
| `Internal/RSVarbitDefinition.simba` | [_internal/rs_varbit_definition.py](src/pyautoeios/_internal/rs_varbit_definition.py) | ![80%](https://progress-bar.dev/80) | |
| `Internal/RSVarps.simba` | [_internal/rs_varps.py](src/pyautoeios/_internal/rs_varps.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/RSWidget.simba` | [_internal/rs_widget.py](src/pyautoeios/_internal/rs_widget.py) | ![65%](https://progress-bar.dev/65) | |
| `Internal/RSWidgetNode.simba` | [_internal/rs_widget_node.py](src/pyautoeios/_internal/rs_widget_node.py) | ![100%](https://progress-bar.dev/100) | |
| `Internal/Setup.simba` | N/A | ![0%](https://progress-bar.dev/0) |  *merging logic into eios class* |
| `Internal/Static.simba` | [_internal/static.py](src/pyautoeios/_internal/static.py) | ![0%](https://progress-bar.dev/0) | |
| `Internal/Structures.simba` | [_internal/structures.py](src/pyautoeios/_internal/structures.py) | ![100%](https://progress-bar.dev/100) | |
| `Inventory.simba` | [inventory.py](src/pyautoeios/inventory.py) | ![0%](https://progress-bar.dev/0) | |
| `Login.simba` | [login.py](src/pyautoeios/login.py) | ![0%](https://progress-bar.dev/0) | |
| `Magic.simba` | [magic.py](src/pyautoeios/magic.py) | ![0%](https://progress-bar.dev/0) | |
| `Mainscreen.simba` | [mainscreen.py](src/pyautoeios/mainscreen.py) | ![0%](https://progress-bar.dev/0) | |
| `Menu.simba` | [menu.py](src/pyautoeios/menu.py) | ![0%](https://progress-bar.dev/0) | |
| `Model.simba` | [model.py](src/pyautoeios/model.py) | ![0%](https://progress-bar.dev/0) | |
| `Mouse.simba` | [mouse.py](src/pyautoeios/mouse.py) | ![0%](https://progress-bar.dev/0) | |
| `NPC.simba` | [npc.py](src/pyautoeios/npc.py) | ![0%](https://progress-bar.dev/0) | |
| `Objects.simba` | [objects.py](src/pyautoeios/objects.py) | ![0%](https://progress-bar.dev/0) | |
| `Player.simba` | [player.py](src/pyautoeios/player.py) | ![0%](https://progress-bar.dev/0) | |
| `Prayer.simba` | [prayer.py](src/pyautoeios/prayer.py) | ![0%](https://progress-bar.dev/0) | |
| `Reflection.simba` | [\_\_init\_\_.py](src/pyautoeios/__init__.py) | ![100%](https://progress-bar.dev/100) | |
| `Skills.simba` | [skills.py](src/pyautoeios/skills.py) | ![0%](https://progress-bar.dev/0) | |
| `Timing.simba` | [timing.py](src/pyautoeios/timing.py) | ![0%](https://progress-bar.dev/0) | |
| `Walking.simba` | [walking.py](src/pyautoeios/walking.py) | ![0%](https://progress-bar.dev/0) | |



## Foot notes

### ¹ Systems used in testing
[¹]: #Systems-used-in-testing

**So far tests have been done entirely under the following conditions:**

to print this information run [examples/get_system_information.py](examples/get_system_information.py)

| python_build | processor | python_compiler | python_version | python_implementation | platform |
| --- | --- | --- | --- | --- | --- |
| CPython | 3.8.6 | ('tags/v3.8.6:db45529', 'Sep 23 2020 15:37:30') | MSC v.1927 32 bit (Intel) | Windows-10-10.0.18362-SP0 | Intel64 Family 6 Model 158 Stepping 9, GenuineIntel |




[reflection]: https://github.com/Brandon-T/Reflection
