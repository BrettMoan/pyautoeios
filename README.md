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

- [x] EIOS_ReleaseTarget (`eios.EIOS.release_target`)
- [x] EIOS_GetTargetDimensions (`eios.EIOS.get_target_dimensions`)
- [x] EIOS_GetImageBuffer (`eios.EIOS.get_image_buffer`)
- [x] EIOS_GetDebugImageBuffer (`eios.EIOS.get_debug_image_buffer`)
- [x] EIOS_SetGraphicsDebugging (`eios.EIOS.set_graphics_debugging`)
- [x] EIOS_UpdateImageBuffer (`eios.EIOS.update_image_buffer`)
- [x] EIOS_HasFocus (`eios.EIOS.has_focus`)
- [x] EIOS_GainFocus (`eios.EIOS.gain_focus`)
- [x] EIOS_LoseFocus (`eios.EIOS.lose_focus`)
- [x] EIOS_IsInputEnabled (`eios.EIOS.is_input_enabled`)
- [x] EIOS_SetInputEnabled (`eios.EIOS.set_input_enabled`)
- [x] EIOS_GetMousePosition (`eios.EIOS.get_mouse_position`)
- [x] EIOS_GetRealMousePosition (`eios.EIOS.get_real_mouse_position`)
- [x] EIOS_MoveMouse (`eios.EIOS.move_mouse`)
- [x] EIOS_HoldMouse (`eios.EIOS.hold_mouse`)
- [x] EIOS_ReleaseMouse (`eios.EIOS.release_mouse`)
- [x] EIOS_ScrollMouse (`eios.EIOS.scroll_mouse`)
- [ ] ~~EIOS_IsMouseButtonHeld (`eios.EIOS.is_mouse_button_held`)~~ *python says function doesn't exist in dll*
- [x] EIOS_SendString (`eios.EIOS.send_string`)
- [x] EIOS_HoldKey (`eios.EIOS.hold_key`)
- [x] EIOS_ReleaseKey (`eios.EIOS.release_key`)
- [ ] EIOS_IsKeyHeld (`eios.EIOS.is_key_held`) *written. just needs tested*
- [ ] EIOS_GetKeyboardSpeed (`eios.EIOS.get_keyboard_speed`) *written. just needs tested*
- [ ] EIOS_SetKeyboardSpeed (`eios.EIOS.set_keyboard_speed`) *written. just needs tested*
- [ ] EIOS_GetKeyboardRepeatDelay (`eios.EIOS.get_keyboard_repeat_delay`) *written. just needs tested*
- [ ] EIOS_SetKeyboardRepeatDelay (`eios.EIOS.set_keyboard_repeat_delay`) *written. just needs tested*
- [x] EIOS_PairClient (`eios.EIOS.pair_client`)
- [ ] EIOS_KillClientPID (`eios.EIOS.kill_client_pid`) *written. just needs tested*
- [ ] EIOS_KillClient (`eios.EIOS.kill_client`) *written. just needs tested*
- [ ] EIOS_KillZombieClients (`eios.EIOS.kill_zombie_clients`) *written. just needs tested*
- [x] EIOS_GetClients (`eios.EIOS.get_clients`)
- [x] EIOS_GetClientPID (`eios.EIOS.get_client_pid`)
- [x] EIOS_Inject (eios.E`IOS.inject)`
- [ ] EIOS_Inject_PID (`eios.EIOS.inject_pid`) *written. just needs tested*
- [x] Reflect_GetEIOS (`eios.EIOS.get_eios`)
- [x] Reflect_Object (`eios.EIOS.get_object`)
- [ ] Reflect_IsSame_Object (`eios.EIOS.is_same_object`) *written. just needs tested*
- [ ] Reflect_InstanceOf (`eios.EIOS.instance_of`) *written. just needs tested*
- [x] Reflect_Release_Object (`eios.EIOS.release_object`)
- [ ] Reflect_Release_Objects (`eios.EIOS.release_objects`) *written. just needs tested*
- [x] Reflect_Bool (`eios.EIOS.get_bool`)
- [ ] Reflect_Char (`eios.EIOS.get_char`) *written. just needs tested*
- [ ] Reflect_Byte (`eios.EIOS.get_byte`) *written. just needs tested*
- [ ] Reflect_Short (`eios.EIOS.get_short`) *written. just needs tested*
- [x] Reflect_Int (`eios.EIOS.get_int)`
- [ ] Reflect_Long (`eios.EIOS.get_long`) *written. just needs tested*
- [ ] Reflect_Float (`eios.EIOS.get_float`) *written. just needs tested*
- [ ] Reflect_Double (`eios.EIOS.get_double`) *written. just needs tested*
- [x] Reflect_String (`eios.EIOS.get_string`)
- [x] Reflect_Array (`eios.EIOS.get_array`)
- [x] Reflect_Array_With_Size (`eios.EIOS.get_array_with_size`)
- [x] Reflect_Array_Size (`eios.EIOS.get_array_size`)
- [x] Reflect_Array_Index (`eios.EIOS.get_array_from_pointer` and `eios.EIOS.get_array_index_from_pointer`)
- [ ] Reflect_Array_Index2d (`eios.EIOS.get_2d_array_index_from_pointer`) *written. just needs tested*
- [ ] Reflect_Array_Index3d (`eios.EIOS.get_3d_array_index_from_pointer`) *written. just needs tested*
- [ ] Reflect_Array_Index4d (`eios.EIOS.get_4d_array_index_from_pointer`) *written. just needs tested*


#### Progess of porting [reflection] ![25%](https://progress-bar.dev/25)

- [ ] `Antiban.simba` [link](src/pyautoeios/antiban.py) ![0%](https://progress-bar.dev/0)
- [ ] `Bank.simba` [link](src/pyautoeios/bank.py) ![0%](https://progress-bar.dev/0)
- [ ] `Chat.simba` [link](src/pyautoeios/chat.py) ![0%](https://progress-bar.dev/0)
- [ ] `Combat.simba` [link](src/pyautoeios/combat.py) ![0%](https://progress-bar.dev/0)
- [x] `Constants.simba` [link](src/pyautoeios/_internal/constants.py) ![100%](https://progress-bar.dev/100)
- [ ] `Equipment.simba` [link](src/pyautoeios/equipment.py) ![0%](https://progress-bar.dev/0)
- [ ] `GameTab.simba` [link](src/pyautoeios/game_tab.py) ![0%](https://progress-bar.dev/0)
- [ ] `Ground.simba` [link](src/pyautoeios/ground.py) ![0%](https://progress-bar.dev/0)
- [ ] `Interfaces.simba` [link](src/pyautoeios/interfaces.py) ![0%](https://progress-bar.dev/0)
- [ ] `Internal`
  - [ ] `Internal/Functions.simba` *merging into rs_structures* ![75%](https://progress-bar.dev/75)
  - [x] `Internal/Hooks.simba`  [link](src/pyautoeios/hooks.py)  ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSActor.simba` [link](src/pyautoeios/_internal/rs_actor.py) ![25%](https://progress-bar.dev/25)
  - [x] `Internal/RSAnimableNode.simba` [link](src/pyautoeios/_internal/rs_animable_node.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSAnimatedModel.simba` [link](src/pyautoeios/_internal/rs_animated_model.py) ![10%](https://progress-bar.dev/0)
  - [x] `Internal/RSAnimation.simba` [link](src/pyautoeios/_internal/rs_animation.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSAnimationFrame.simba` [link](src/pyautoeios/_internal/rs_animation_frame.py) ![10%](https://progress-bar.dev/0)
  - [ ] `Internal/RSAnimationSequence.simba` [link](src/pyautoeios/_internal/rs_animation_sequence.py) ![10%](https://progress-bar.dev/0)
  - [ ] `Internal/RSAnimationSkeleton.simba` [link](src/pyautoeios/_internal/rs_animation_skeleton.py) ![10%](https://progress-bar.dev/0)
  - [x] `Internal/RSCache.simba` [link](src/pyautoeios/_internal/rs_cache.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSCamera.simba` [link](src/pyautoeios/_internal/rs_camera.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSClient.simba` [link](src/pyautoeios/_internal/rs_client.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSCombatInfo.simba` [link](src/pyautoeios/_internal/rs_combat_info.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSConstants.simba` [link](src/pyautoeios/_internal/constants.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSEntity.simba` [link](src/pyautoeios/_internal/rs_entity.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSGameShell.simba` [link](src/pyautoeios/_internal/rs_game_shell.py) ![10%](https://progress-bar.dev/0)
  - [ ] `~~Internal/RSGraphics.simba`~~ *No plans to implement*
  - [ ] `Internal/RSGroundObject.simba` [link](src/pyautoeios/_internal/rs_ground_object.py) ![10%](https://progress-bar.dev/0)
  - [ ] `Internal/RSHashTable.simba` [link](src/pyautoeios/_internal/rs_hash_table.py) ![60%](https://progress-bar.dev/60)
  - [ ] `Internal/RSItem.simba` [link](src/pyautoeios/_internal/rs_item.py) ![80%](https://progress-bar.dev/80)
  - [ ] `Internal/RSItemDefinition.simba` [link](src/pyautoeios/_internal/rs_item_definition.py) ![80%](https://progress-bar.dev/80)
  - [x] `Internal/RSItemNode.simba` [link](src/pyautoeios/_internal/rs_item_node.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSIterableHashTable.simba` [link](src/pyautoeios/_internal/rs_iterable_hash_table.py) ![60%](https://progress-bar.dev/60)
  - [x] `Internal/RSLinkedList.simba` [link](src/pyautoeios/_internal/rs_linked_list.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSLocalPlayer.simba` [link](src/pyautoeios/_internal/rs_local_player.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSMath.simba`  *merging logic into static and relevant classes* ![0%](https://progress-bar.dev/0)
  - [ ] `Internal/RSModel.simba` [link](src/pyautoeios/_internal/rs_model.py) ![20%](https://progress-bar.dev/20)
  - [x] `Internal/RSNameInfo.simba` [link](src/pyautoeios/_internal/rs_name_info.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSNode.simba` [link](src/pyautoeios/_internal/rs_node.py) ![100%](https://progress-bar.dev/100)
  - [x] `Internal/RSNodeDeque.simba` [link](src/pyautoeios/_internal/rs_node_deque.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSNPC.simba` [link](src/pyautoeios/_internal/rsnpc.py) ![10%](https://progress-bar.dev/10)
  - [ ] `Internal/RSNPCDefinition.simba` [link](src/pyautoeios/_internal/rsnpc_definition.py) ![80%](https://progress-bar.dev/80)
  - [ ] `Internal/RSObject.simba` [link](src/pyautoeios/_internal/rs_object.py) ![20%](https://progress-bar.dev/20)
  - [ ] `Internal/RSObjectDefinition.simba` [link](src/pyautoeios/_internal/rs_object_definition.py) ![80%](https://progress-bar.dev/80)
  - [ ] `Internal/RSPlayer.simba` [link](src/pyautoeios/_internal/rs_player.py) ![60%](https://progress-bar.dev/60)
  - [ ] `Internal/RSPlayerDefinition.simba` [link](src/pyautoeios/_internal/rs_player_definition.py) ![70%](https://progress-bar.dev/70)
  - [x] `Internal/RSQueue.simba` [link](src/pyautoeios/_internal/rs_queue.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSRegion.simba` [link](src/pyautoeios/_internal/rs_region.py) ![10%](https://progress-bar.dev/10)
  - [ ] `Internal/RSSceneTile.simba` [link](src/pyautoeios/_internal/rs_scene_tile.py) ![70%](https://progress-bar.dev/70)
  - [ ] `Internal/RSStructures.simba` [link](src/pyautoeios/_internal/rs_structures.py) ![90%](https://progress-bar.dev/90)
  - [x] `Internal/RSText.simba` *merged logic into static and relevant classes* ![100%](https://progress-bar.dev/0)
  - [ ] `Internal/RSTile.simba` [link](src/pyautoeios/_internal/rs_tile.py) ![30%](https://progress-bar.dev/30)
  - [ ] `Internal/RSVarbitDefinition.simba` [link](src/pyautoeios/_internal/rs_varbit_definition.py) ![80%](https://progress-bar.dev/80)
  - [x] `Internal/RSVarps.simba` [link](src/pyautoeios/_internal/rs_varps.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/RSWidget.simba` [link](src/pyautoeios/_internal/rs_widget.py) ![65%](https://progress-bar.dev/65)
  - [x] `Internal/RSWidgetNode.simba` [link](src/pyautoeios/_internal/rs_widget_node.py) ![100%](https://progress-bar.dev/100)
  - [ ] `Internal/Setup.simba` *merging logic into eios class* ![0%](https://progress-bar.dev/0)
  - [ ] `Internal/Static.simba` [link](src/pyautoeios/_internal/static.py) ![0%](https://progress-bar.dev/0)
  - [x] `Internal/Structures.simba` [link](src/pyautoeios/_internal/structures.py) ![100%](https://progress-bar.dev/100)
- [ ] `Inventory.simba` [link](src/pyautoeios/inventory.py) ![0%](https://progress-bar.dev/0)
- [ ] `Login.simba` [link](src/pyautoeios/login.py) ![0%](https://progress-bar.dev/0)
- [ ] `Magic.simba` [link](src/pyautoeios/magic.py) ![0%](https://progress-bar.dev/0)
- [ ] `Mainscreen.simba` [link](src/pyautoeios/mainscreen.py) ![0%](https://progress-bar.dev/0)
- [ ] `Menu.simba` [link](src/pyautoeios/menu.py) ![0%](https://progress-bar.dev/0)
- [ ] `Model.simba` [link](src/pyautoeios/model.py) ![0%](https://progress-bar.dev/0)
- [ ] `Mouse.simba` [link](src/pyautoeios/mouse.py) ![0%](https://progress-bar.dev/0)
- [ ] `NPC.simba` [link](src/pyautoeios/npc.py) ![0%](https://progress-bar.dev/0)
- [ ] `Objects.simba` [link](src/pyautoeios/objects.py) ![0%](https://progress-bar.dev/0)
- [ ] `Player.simba` [link](src/pyautoeios/player.py) ![0%](https://progress-bar.dev/0)
- [ ] `Prayer.simba` [link](src/pyautoeios/prayer.py) ![0%](https://progress-bar.dev/0)
- [x] `Reflection.simba` *this becomes the `__init__.py`*
- [ ] `Skills.simba` [link](src/pyautoeios/skills.py) ![0%](https://progress-bar.dev/0)
- [ ] `Timing.simba` [link](src/pyautoeios/timing.py) ![0%](https://progress-bar.dev/0)
- [ ] `Walking.simba` [link](src/pyautoeios/walking.py) ![0%](https://progress-bar.dev/0)


## Foot notes

### Systems used in testing


**So far tests have been done entirely under the following conditions:**

| python_build | processor | python_compiler | python_version | python_implementation | platform |
| --- | --- | --- | --- | --- | --- |
| CPython | 3.8.6 | ('tags/v3.8.6:db45529', 'Sep 23 2020 15:37:30') | MSC v.1927 32 bit (Intel) | Windows-10-10.0.18362-SP0 | Intel64 Family 6 Model 158 Stepping 9, GenuineIntel |

[to print this information run this script](examples/get_system_information.py)



[reflection]: https://github.com/Brandon-T/Reflection
