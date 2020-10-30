import collections

THook = collections.namedtuple('THook', 'cls field desc multiplier')

NODE_UID: THook =                                 THook('gn', 'cm', 'J', 1)
NODE_PREV: THook =                                THook('gn', 'ct', 'Lgn;', 1)
NODE_NEXT: THook =                                THook('gn', 'cb', 'Lgn;', 1)

# {NodeDeque: ja}
NODEDEQUE_HEAD: THook =                           THook('ja', 'f', 'Lgn;', 1)
NODEDEQUE_CURRENT: THook =                        THook('ja', 'b', 'Lgn;', 1)

# {Cacheable: gp}
CACHEABLE_NEXT: THook =                           THook('gp', 'cj', 'Lgp;', 1)
CACHEABLE_PREV: THook =                           THook('gp', 'cd', 'Lgp;', 1)

# {LinkedList: js}
LINKEDLIST_HEAD: THook =                          THook('js', 'f', 'Lgn;', 1)
LINKEDLIST_CURRENT: THook =                       THook('js', 'b', 'Lgn;', 1)

# {HashTable: lp}
HASHTABLE_HEAD: THook =                           THook('lp', 'l', 'Lgn;', 1)
HASHTABLE_TAIL: THook =                           THook('lp', 'm', 'Lgn;', 1)
HASHTABLE_BUCKETS: THook =                        THook('lp', 'b', '[Lgn;', 1)
HASHTABLE_INDEX: THook =                          THook('lp', 'z', 'I', 1)
HASHTABLE_SIZE: THook =                           THook('lp', 'f', 'I', 1)

# {IterableHashTable: ll}
ITERABLEHASHTABLE_HEAD: THook =                   THook('ll', 'l', 'Lgn;', 1)
ITERABLEHASHTABLE_TAIL: THook =                   THook('ll', 'm', 'Lgn;', 1)
ITERABLEHASHTABLE_BUCKETS: THook =                THook('ll', 'b', '[Lgn;', 1)
ITERABLEHASHTABLE_INDEX: THook =                  THook('ll', 'z', 'I', 1)
ITERABLEHASHTABLE_SIZE: THook =                   THook('ll', 'f', 'I', 1)

# {Queue: jt}
QUEUE_HEAD: THook =                               THook('jt', 'b', 'Lgp;', 1)

# {Cache: ev}
CACHE_HASHTABLE: THook =                          THook('ev', 'm', 'Lll;', 1)
CACHE_QUEUE: THook =                              THook('ev', 'z', 'Ljt;', 1)
CACHE_REMAINING: THook =                          THook('ev', 'l', 'I', 1)
CACHE_CAPACITY: THook =                           THook('ev', 'b', 'I', 1)

# {ClassData: dv}
CLASSDATA_BYTES: THook =                          THook('dv', 'm', '[[[B', 1)
CLASSDATA_METHODS: THook =                        THook('dv', 'c', '[Ljava/lang/reflect/Method;', 1)
CLASSDATA_FIELDS: THook =                         THook('dv', 'k', '[Ljava/lang/reflect/Field;', 1)

# {Rasteriser: lm}
RASTERISER_PIXELS: THook =                        THook('lm', 'ac', '[I', 1)
RASTERISER_WIDTH: THook =                         THook('lm', 'ao', 'I', 1)
RASTERISER_HEIGHT: THook =                        THook('lm', 'af', 'I', 1)

# {Rasteriser3D: et}
RASTERISER3D_SHADOWDECAY: THook =                 THook('et', 'g', '[I', 1)
RASTERISER3D_SINETABLE: THook =                   THook('et', 'i', '[I', 1)
RASTERISER3D_COSINETABLE: THook =                 THook('et', 'ab', '[I', 1)

# {Typeface: ky}
TYPEFACE_CHARACTERPIXELS: THook =                 THook('ky', 'f', '[[B', 1)

# {IndexedRGB: le}
INDEXEDRGB_PIXELS: THook =                        THook('le', 'b', '[I', 1)
INDEXEDRGB_PALETTE: THook =                       THook('le', 'f', '[B', 1)

# {ImageRGB: lc}
IMAGERGB_PIXELS: THook =                          THook('lc', 'f', '[I', 1)
IMAGERGB_WIDTH: THook =                           THook('lc', 'b', 'I', 1)
IMAGERGB_HEIGHT: THook =                          THook('lc', 'l', 'I', 1)
IMAGERGB_MAXWIDTH: THook =                        THook('lc', 'q', 'I', 1)
IMAGERGB_MAXHEIGHT: THook =                       THook('lc', 'k', 'I', 1)

# {Keyboard: bp}

# {GameShell: ba}

# {Buffer: kb}
BUFFER_PAYLOAD: THook =                           THook('kb', 'q', '[B', 1)
BUFFER_CRC: THook =                               THook('kb', 'c', '[I', 1)

# {BufferedConnection: fa}
BUFFEREDCONNECTION_INPUTSTREAM: THook =           THook('fa', 'f', 'Ljava/io/InputStream;', 1)
BUFFEREDCONNECTION_OUTPUTSTREAM: THook =          THook('fa', 'b', 'Ljava/io/OutputStream;', 1)
BUFFEREDCONNECTION_SOCKET: THook =                THook('fa', 'l', 'Ljava/net/Socket;', 1)
BUFFEREDCONNECTION_PAYLOAD: THook =               THook('fa', 'k', '[B', 1)
BUFFEREDCONNECTION_ISCLOSED: THook =              THook('fa', 'm', 'Z', 1)

# {CollisionMap: fh}
COLLISIONMAP_WIDTH: THook =                       THook('fh', 'ak', 'I', -2103042709)
COLLISIONMAP_HEIGHT: THook =                      THook('fh', 'au', 'I', 442513137)
COLLISIONMAP_ADJACENCY: THook =                   THook('fh', 'ai', '[[I', 1)

# {NameInfo: km}
NAMEINFO_NAME: THook =                            THook('km', 'f', 'Ljava/lang/String;', 1)
NAMEINFO_DECODEDNAME: THook =                     THook('km', 'b', 'Ljava/lang/String;', 1)

# {Renderable: ej}
RENDERABLE_MODELHEIGHT: THook =                   THook('ej', 'cu', 'I', 1647777713)

# {Region: ef}
REGION_SCENETILES: THook =                        THook('ef', 'q', '[[[Leo;', 1)
REGION_INTERACTABLEOBJECTS: THook =               THook('ef', 'u', '[Lel;', 1)

# {AnimableNode: ck}
ANIMABLENODE_ID: THook =                          THook('ck', 'f', 'I', -550843083)
ANIMABLENODE_ANIMATIONSEQUENCE: THook =           THook('ck', 'k', 'Ljg;', 1)
ANIMABLENODE_FLAGS: THook =                       THook('ck', 'b', 'I', 174390429)
ANIMABLENODE_ORIENTATION: THook =                 THook('ck', 'l', 'I', 89407283)
ANIMABLENODE_PLANE: THook =                       THook('ck', 'm', 'I', -1374963731)
ANIMABLENODE_X: THook =                           THook('ck', 'z', 'I', -2010464009)
ANIMABLENODE_Y: THook =                           THook('ck', 'q', 'I', 647351421)

# {BoundaryObject: em}
BOUNDARYOBJECT_ID: THook =                        THook('em', 'c', 'J', -3078711070799260957)
BOUNDARYOBJECT_FLAGS: THook =                     THook('em', 'u', 'I', -810696597)
BOUNDARYOBJECT_PLANE: THook =                     THook('em', 'f', 'I', 24178129)
BOUNDARYOBJECT_HEIGHT: THook =                    THook('em', 'z', 'I', 237050093)
BOUNDARYOBJECT_LOCALX: THook =                    THook('em', 'b', 'I', 840836709)
BOUNDARYOBJECT_LOCALY: THook =                    THook('em', 'l', 'I', 511451679)
BOUNDARYOBJECT_ORIENTATION: THook =               THook('em', 'm', 'I', 1059090271)
BOUNDARYOBJECT_RENDERABLE: THook =                THook('em', 'q', 'Lej;', 1)
BOUNDARYOBJECT_RENDERABLE2: THook =               THook('em', 'k', 'Lej;', 1)

# {WallDecoration: ey}
WALLDECORATION_ID: THook =                        THook('ey', 't', 'J', -3894207238426267157)
WALLDECORATION_FLAGS: THook =                     THook('ey', 'e', 'I', -237175035)
WALLDECORATION_PLANE: THook =                     THook('ey', 'f', 'I', -1368883061)
WALLDECORATION_HEIGHT: THook =                    THook('ey', 'z', 'I', -1005575771)
WALLDECORATION_LOCALX: THook =                    THook('ey', 'b', 'I', 1255836875)
WALLDECORATION_LOCALY: THook =                    THook('ey', 'l', 'I', 1394186747)
WALLDECORATION_RELATIVEX: THook =                 THook('ey', 'q', 'I', 287109355)
WALLDECORATION_RELATIVEY: THook =                 THook('ey', 'k', 'I', -872509349)
WALLDECORATION_ORIENTATION: THook =               THook('ey', 'm', 'I', -1069815711)
WALLDECORATION_RENDERABLE: THook =                THook('ey', 'c', 'Lej;', 1)
WALLDECORATION_RENDERABLE2: THook =               THook('ey', 'u', 'Lej;', 1)

# {FloorDecoration: ek}
FLOORDECORATION_ID: THook =                       THook('ek', 'm', 'J', 2791850332732375269)
FLOORDECORATION_FLAGS: THook =                    THook('ek', 'q', 'I', -1457303601)
FLOORDECORATION_LOCALX: THook =                   THook('ek', 'b', 'I', -191694913)
FLOORDECORATION_LOCALY: THook =                   THook('ek', 'l', 'I', 489421685)
FLOORDECORATION_PLANE: THook =                    THook('ek', 'f', 'I', 1613676277)
FLOORDECORATION_RENDERABLE: THook =               THook('ek', 'z', 'Lej;', 1)

# {GameObject: el}
GAMEOBJECT_RENDERABLE: THook =                    THook('el', 'z', 'Lej;', 1)
GAMEOBJECT_ID: THook =                            THook('el', 'n', 'J', -2637081015005136759)
GAMEOBJECT_FLAGS: THook =                         THook('el', 'x', 'I', -735597717)
GAMEOBJECT_ORIENTATION: THook =                   THook('el', 'm', 'I', -1596359689)
GAMEOBJECT_PLANE: THook =                         THook('el', 'f', 'I', -1412668883)
GAMEOBJECT_HEIGHT: THook =                        THook('el', 'b', 'I', -1556347637)
GAMEOBJECT_LOCALX: THook =                        THook('el', 'l', 'I', 954361615)
GAMEOBJECT_LOCALY: THook =                        THook('el', 'q', 'I', 1994666041)
GAMEOBJECT_WORLDX: THook =                        THook('el', 'k', 'I', 207668277)
GAMEOBJECT_WORLDY: THook =                        THook('el', 'u', 'I', 1266358135)
GAMEOBJECT_OFFSETX: THook =                       THook('el', 'c', 'I', -1940452637)
GAMEOBJECT_OFFSETY: THook =                       THook('el', 't', 'I', 1643778515)

# {SceneTile: eo}
SCENETILE_BOUNDARYOBJECT: THook =                 THook('eo', 'k', 'Lem;', 1)
SCENETILE_SCENETILEOBJECT: THook =                THook('eo', 'a', 'Leo;', 1)
SCENETILE_GAMEOBJECT: THook =                     THook('eo', 'o', '[Lel;', 1)
SCENETILE_WALLDECORATION: THook =                 THook('eo', 'c', 'Ley;', 1)
SCENETILE_GROUNDDECORATION: THook =               THook('eo', 'u', 'Lek;', 1)
SCENETILE_LOCALX: THook =                         THook('eo', 'b', 'I', 1121105615)
SCENETILE_LOCALY: THook =                         THook('eo', 'l', 'I', -541915111)
SCENETILE_PLANE: THook =                          THook('eo', 'm', 'I', 102326407)

# {GrandExchange: j}
TRADINGPOST_STATUS: THook =                       THook('j', 'f', 'B', 1)
TRADINGPOST_ITEMID: THook =                       THook('j', 'b', 'I', 1175311391)
TRADINGPOST_PRICE: THook =                        THook('j', 'l', 'I', 1620049031)
TRADINGPOST_QUANTITY: THook =                     THook('j', 'm', 'I', -658451115)
TRADINGPOST_TRANSFERRED: THook =                  THook('j', 'z', 'I', 682864265)
TRADINGPOST_SPENT: THook =                        THook('j', 'q', 'I', 1)
TRADINGPOST_QUERYIDS: THook =                     THook('j', 'N/A', 'N/A', 1)

# {Model: eh}
MODEL_INDICESX: THook =                           THook('eh', 't', '[I', 1)
MODEL_INDICESY: THook =                           THook('eh', 'e', '[I', 1)
MODEL_INDICESZ: THook =                           THook('eh', 'o', '[I', 1)
MODEL_INDICESLENGTH: THook =                      THook('eh', 'u', 'I', 1)
MODEL_VERTICESX: THook =                          THook('eh', 'q', '[I', 1)
MODEL_VERTICESY: THook =                          THook('eh', 'k', '[I', 1)
MODEL_VERTICESZ: THook =                          THook('eh', 'c', '[I', 1)
MODEL_VERTICESLENGTH: THook =                     THook('eh', 'z', 'I', 1)
MODEL_TEXINDICESX: THook =                        THook('eh', 'n', '[I', 1)
MODEL_TEXINDICESY: THook =                        THook('eh', 'x', '[I', 1)
MODEL_TEXINDICESZ: THook =                        THook('eh', 'p', '[I', 1)
MODEL_TEXVERTICESX: THook =                       THook('eh', 'd', '[I', 1)
MODEL_TEXVERTICESY: THook =                       THook('eh', 'a', '[I', 1)
MODEL_TEXVERTICESZ: THook =                       THook('eh', 'g', '[I', 1)
MODEL_TEXVERTICESLENGTH: THook =                  THook('eh', 'v', 'I', 1)
MODEL_SKINS: THook =                              THook('eh', 'h', '[[I', 1)
MODEL_SHADOWINTENSITY: THook =                    THook('eh', 'af', 'I', 1)
MODEL_FITSSINGLETILE: THook =                     THook('eh', 'ab', 'Z', 1)

# {AnimationSequence: jg}
ANIMATIONSEQUENCE_FRAMES: THook =                 THook('jg', 'q', '[I', 1)
ANIMATIONSEQUENCE_SEQUENCECACHE: THook =          THook('jg', 'm', 'Lev;', 1)
ANIMATIONSEQUENCE_FRAMECACHE: THook =             THook('jg', 'z', 'Lev;', 1)

# {AnimationFrames: ex}
ANIMATIONFRAMES_FRAMES: THook =                   THook('ex', 'f', '[Ler;', 1)

# {AnimationSkeleton: ei}
ANIMATIONSKELETON_ID: THook =                     THook('ei', 'f', 'I', 2017085485)
ANIMATIONSKELETON_TRANSFORMATIONCOUNT: THook =    THook('ei', 'b', 'I', 244564821)
ANIMATIONSKELETON_TRANSFORMATIONTYPES: THook =    THook('ei', 'l', '[I', 1)
ANIMATIONSKELETON_TRANSFORMATIONS: THook =        THook('ei', 'm', '[[I', 1)

# {Animation: er}
ANIMATION_FRAMECOUNT: THook =                     THook('er', 'q', 'I', 1)
ANIMATION_FRAMES: THook =                         THook('er', 'k', '[I', 1)
ANIMATION_TRANSFORMX: THook =                     THook('er', 'c', '[I', 1)
ANIMATION_TRANSFORMY: THook =                     THook('er', 'u', '[I', 1)
ANIMATION_TRANSFORMZ: THook =                     THook('er', 't', '[I', 1)
ANIMATION_SKELETON: THook =                       THook('er', 'z', 'Lei;', 1)

# {CombatInfo1: ce}
COMBATINFO1_HEALTH: THook =                       THook('ce', 'l', 'I', -733805573)
COMBATINFO1_HEALTHRATIO: THook =                  THook('ce', 'b', 'I', 1850182953)

# {CombatInfo2: ix}
COMBATINFO2_HEALTHSCALE: THook =                  THook('ix', 'p', 'I', 185744125)

# {CombatInfoList: js}
COMBATINFOLIST_HEAD: THook =                      THook('js', 'f', 'Lgn;', 1)
COMBATINFOLIST_CURRENT: THook =                   THook('js', 'b', 'Lgn;', 1)

# {CombatInfoHolder: cx}
COMBATINFOHOLDER_COMBATINFOLIST: THook =          THook('cx', 'm', 'Ljs;', 1)
COMBATINFOHOLDER_COMBATINFO2: THook =             THook('cx', 'l', 'Lix;', 1)

# {Actor: cs}
ACTOR_ANIMATION: THook =                          THook('cs', 'bt', 'I', -254649357)
ACTOR_ANIMATIONDELAY: THook =                     THook('cs', 'y', 'I', -370859363)
ACTOR_ANIMATIONFRAME: THook =                     THook('cs', 'bw', 'I', 1925242573)
ACTOR_MOVEMENTSEQUENCE: THook =                   THook('cs', 'bo', 'I', 1355414019)
ACTOR_MOVEMENTFRAME: THook =                      THook('cs', 'be', 'I', 878455421)
ACTOR_CURRENTSEQUENCE: THook =                    THook('cs', 'ak', 'I', 790102969)
ACTOR_SPOKENTEXT: THook =                         THook('cs', 'am', 'Ljava/lang/String;', 1)
ACTOR_HITDAMAGES: THook =                         THook('cs', 'ad', '[I', 1)
ACTOR_HITTYPES: THook =                           THook('cs', 'bb', '[I', 1)
ACTOR_HITCYCLE: THook =                           THook('cs', 'bf', '[I', 1)
ACTOR_QUEUEX: THook =                             THook('cs', 'cy', '[I', 1)
ACTOR_QUEUEY: THook =                             THook('cs', 'cx', '[I', 1)
ACTOR_QUEUETRAVERSED: THook =                     THook('cs', 'ca', '[B', 1)
ACTOR_QUEUESIZE: THook =                          THook('cs', 'ci', 'I', -1827352877)
ACTOR_LOCALX: THook =                             THook('cs', 'af', 'I', -952501591)
ACTOR_LOCALY: THook =                             THook('cs', 'av', 'I', 1794864455)
ACTOR_COMBATCYCLE: THook =                        THook('cs', 'N/A', 'N/A', 1)
ACTOR_INTERACTINGINDEX: THook =                   THook('cs', 'bj', 'I', -49521303)
ACTOR_ORIENTATION: THook =                        THook('cs', 'cp', 'I', 501904063)
ACTOR_ISWALKING: THook =                          THook('cs', 'ay', 'Z', 1)
ACTOR_TARGETINDEX: THook =                        THook('cs', 'bj', 'I', -49521303)
ACTOR_COMBATINFOLIST: THook =                     THook('cs', 'bc', 'Ljs;', 1)
ACTOR_SPOTANIMATION: THook =                      THook('cs', 'bv', 'I', 1626363285)
ACTOR_SPOTANIMATIONFRAME: THook =                 THook('cs', 'br', 'I', -1912022721)
ACTOR_SPOTANIMATIONFRAMECYCLE: THook =            THook('cs', 'bs', 'I', 806708579)
ACTOR_GRAPHICSID: THook =                         THook('cs', 'N/A', 'N/A', 1)
ACTOR_HEIGHT: THook =                             THook('cs', 'cg', 'I', 1789811467)

# {NPCDefinition: jn}
NPCDEFINITION_ID: THook =                         THook('jn', 'z', 'I', -241449157)
NPCDEFINITION_NAME: THook =                       THook('jn', 'q', 'Ljava/lang/String;', 1)
NPCDEFINITION_ACTIONS: THook =                    THook('jn', 'v', '[Ljava/lang/String;', 1)
NPCDEFINITION_MODELIDS: THook =                   THook('jn', 'c', '[I', 1)
NPCDEFINITION_COMBATLEVEL: THook =                THook('jn', 'a', 'I', 1396717947)
NPCDEFINITION_VISIBLE: THook =                    THook('jn', 'i', 'Z', 1)
NPCDEFINITION_MODELCACHE: THook =                 THook('jn', 'm', 'Lev;', 1)
NPCDEFINITION_TRANSFORMATIONS: THook =            THook('jn', 'av', '[I', 1)
NPCDEFINITION_MODELTILESIZE: THook =              THook('jn', 'k', 'i', 2022516453)
NPCDEFINITION_MODELSCALEWIDTH: THook =            THook('jn', 'g', 'i', 9158797)
NPCDEFINITION_MODELSCALEHEIGHT: THook =           THook('jn', 'h', 'i', -174548931)

# {NPC: ca}
NPC_DEFINITION: THook =                           THook('ca', 'f', 'Ljn;', 1)

# {PlayerDefinition: hu}
PLAYERDEFINITION_NPCTRANSFORMID: THook =          THook('hu', 'm', 'I', 1998131209)
PLAYERDEFINITION_ISFEMALE: THook =                THook('hu', 'l', 'Z', 1)
PLAYERDEFINITION_ANIMATEDMODELID: THook =         THook('hu', 'z', 'J', -3297432427762095127)
PLAYERDEFINITION_MODELID: THook =                 THook('hu', 'q', 'J', -3842356906884846791)
PLAYERDEFINITION_EQUIPMENT: THook =               THook('hu', 'f', '[I', 1)
PLAYERDEFINITION_MODELCACHE: THook =              THook('hu', 'o', 'Lev;', 1)

# {Player: bi}
PLAYER_NAME: THook =                              THook('bi', 'f', 'Lkm;', 1)
PLAYER_MODEL: THook =                             THook('bi', 'p', 'Leh;', 1)
PLAYER_VISIBLE: THook =                           THook('bi', 'w', 'Z', 1)
PLAYER_DEFINITION: THook =                        THook('bi', 'b', 'Lhu;', 1)
PLAYER_COMBATLEVEL: THook =                       THook('bi', 'k', 'I', -953649939)
PLAYER_INDEX: THook =                             THook('bi', 'g', 'I', -1613823593)
PLAYER_ISANIMATING: THook =                       THook('bi', 'w', 'Z', 1)

# {ObjectDefinition: je}
OBJECTDEFINITION_ID: THook =                      THook('je', 'u', 'I', 1144020119)
OBJECTDEFINITION_DEFINITIONCACHE: THook =         THook('je', 'm', 'Lev;', 1)
OBJECTDEFINITION_MODELCACHE: THook =              THook('je', 'k', 'Lev;', 1)
OBJECTDEFINITION_MODELIDS: THook =                THook('je', 't', '[I', 1)
OBJECTDEFINITION_MODELS: THook =                  THook('je', 'e', '[I', 1)
OBJECTDEFINITION_NAME: THook =                    THook('je', 'o', 'Ljava/lang/String;', 1)
OBJECTDEFINITION_ACTIONS: THook =                 THook('je', 'ao', '[Ljava/lang/String;', 1)
OBJECTDEFINITION_TRANSFORMATIONS: THook =         THook('je', 'an', '[I', 1)
OBJECTDEFINITION_TRANSFORMATIONVARBIT: THook =    THook('je', 'am', 'I', 1763689999)
OBJECTDEFINITION_TRANSFORMATIONVARP: THook =      THook('je', 'aa', 'I', -945520639)

# {WidgetNode: bs}
WIDGETNODE_ID: THook =                            THook('bs', 'f', 'I', 1986621351)

# {Widget: ht}
WIDGET_NAME: THook =                              THook('ht', 'dg', 'Ljava/lang/String;', 1)
WIDGET_TEXT: THook =                              THook('ht', 'ce', 'Ljava/lang/String;', 1)
WIDGET_WIDGETID: THook =                          THook('ht', 'j', 'I', -583486671)
WIDGET_PARENTID: THook =                          THook('ht', 'ai', 'I', 1412750483)
WIDGET_PARENT: THook =                            THook('ht', 'dv', 'Lht;', 1)
WIDGET_ITEMID: THook =                            THook('ht', 'el', 'I', -659047965)
WIDGET_INVIDS: THook =                            THook('ht', 'ed', '[I', 1)
WIDGET_STACKSIZES: THook =                        THook('ht', 'ey', '[I', 1)
WIDGET_ITEMAMOUNT: THook =                        THook('ht', 'es', 'I', 1581915613)
WIDGET_TEXTUREID: THook =                         THook('ht', 'bf', 'I', 372301921)
WIDGET_ACTIONS: THook =                           THook('ht', 'cw', '[Ljava/lang/String;', 1)
WIDGET_ACTIONTYPE: THook =                        THook('ht', 'd', 'I', 1601942739)
WIDGET_TYPE: THook =                              THook('ht', 'v', 'I', -1823014479)
WIDGET_ISHIDDEN: THook =                          THook('ht', 'ax', 'Z', 1)
WIDGET_ABSOLUTEX: THook =                         THook('ht', 'ac', 'I', -1326300873)
WIDGET_ABSOLUTEY: THook =                         THook('ht', 'ao', 'I', 1422648317)
WIDGET_RELATIVEX: THook =                         THook('ht', 'ar', 'I', 371785153)
WIDGET_RELATIVEY: THook =                         THook('ht', 'ay', 'I', 766965945)
WIDGET_SCROLLX: THook =                           THook('ht', 'ag', 'I', -182885719)
WIDGET_SCROLLY: THook =                           THook('ht', 'aq', 'I', 192866787)
WIDGET_WIDTH: THook =                             THook('ht', 'ah', 'I', 410180701)
WIDGET_HEIGHT: THook =                            THook('ht', 'az', 'I', -1661593933)
WIDGET_CHILDREN: THook =                          THook('ht', 'ee', '[Lht;', 1)
WIDGET_BOUNDSINDEX: THook =                       THook('ht', 'fy', 'I', 651630769)
WIDGET_WIDGETCYCLE: THook =                       THook('ht', 'ff', 'I', -536480473)

# {ItemDefinition: jk}
ITEMDEFINITION_ID: THook =                        THook('jk', 'x', 'I', 205656235)
ITEMDEFINITION_NAME: THook =                      THook('jk', 'r', 'Ljava/lang/String;', 1)
ITEMDEFINITION_ISMEMBERS: THook =                 THook('jk', 'ao', 'Z', 1)
ITEMDEFINITION_GROUNDACTIONS: THook =             THook('jk', 'af', '[Ljava/lang/String;', 1)
ITEMDEFINITION_ACTIONS: THook =                   THook('jk', 'av', '[Ljava/lang/String;', 1)
ITEMDEFINITION_CACHE: THook =                     THook('jk', 't', 'Lev;', 1)

# {Item: cb}
ITEM_ID: THook =                                  THook('cb', 'f', 'I', -459870843)
ITEM_STACKSIZES: THook =                          THook('cb', 'b', 'I', 724722271)

# {ItemNode: bv}
ITEMNODE_ITEMIDS: THook =                         THook('bv', 'b', '[I', 1)
ITEMNODE_ITEMQUANTITIES: THook =                  THook('bv', 'l', '[I', 1)
ITEMNODE_CACHE: THook =                           THook('bv', 'f', 'Llp;', 1)

# {Varps: hs}
VARPS_MASKS: THook =                              THook('hs', 'f', '[I', 1)
VARPS_MAIN: THook =                               THook('hs', 'l', '[I', 1)

# {VarbitDefinition: iy}
VARBITDEFINITION_CACHE: THook =                   THook('iy', 'b', 'Lev;', 1)
VARBITDEFINITION_BASE: THook =                    THook('iy', 'l', 'I', 1810404981)
VARBITDEFINITION_STARTBIT: THook =                THook('iy', 'm', 'I', -581436309)
VARBITDEFINITION_ENDBIT: THook =                  THook('iy', 'z', 'I', 1763957303)

# {Client: client}
CLIENT_REVISION: THook =                          THook('client', '192', 'I', 1)
CLIENT_CLIENT: THook =                            THook('client', 'ap', 'Lclient;', 1)
CLIENT_LOCALNPCS: THook =                         THook('client', 'fo', '[Lca;', 1)
CLIENT_NPCINDICES: THook =                        THook('client', 'ff', '[I', 1)
CLIENT_NPCCOUNT: THook =                          THook('client', 'fy', 'I', -2146265857)
CLIENT_LOCALPLAYERS: THook =                      THook('client', 'ku', '[Lbi;', 1)
CLIENT_PLAYERINDICES: THook =                     THook('cv', 'k', '[I', 1)
CLIENT_PLAYERCOUNT: THook =                       THook('client', 'N/A', 'N/A', 1)
CLIENT_LOCALPLAYER: THook =                       THook('in', 'kz', 'Lbi;', 1)
CLIENT_PLAYERINDEX: THook =                       THook('client', 'kl', 'I', 1876036055)
CLIENT_LOOPCYCLE: THook =                         THook('client', 'cn', 'I', -1633145881)
CLIENT_GAMESTATE: THook =                         THook('client', 'bq', 'I', 1008452177)
CLIENT_LOGINSTATE: THook =                        THook('cj', 'au', 'I', 1682315035)
CLIENT_ISLOADING: THook =                         THook('client', 'ca', 'Z', 1)
CLIENT_CROSSHAIRCOLOR: THook =                    THook('client', 'jv', 'I', -1792879987)
CLIENT_ANIMATIONFRAMECACHE: THook =               THook('jg', 'z', 'Lev;', 1)
CLIENT_GROUNDITEMS: THook =                       THook('client', 'ky', '[[[Lja;', 1)
CLIENT_COLLISIONMAP: THook =                      THook('client', 'w', '[Lfh;', 1)
CLIENT_TRADINGPOSTOFFERS: THook =                 THook('client', 'sn', '[Lj;', 1)
CLIENT_CAMERAX: THook =                           THook('bv', 'hu', 'I', -966847555)
CLIENT_CAMERAY: THook =                           THook('at', 'hr', 'I', 104039997)
CLIENT_CAMERAZ: THook =                           THook('cr', 'hx', 'I', -690692767)
CLIENT_CAMERAPITCH: THook =                       THook('cf', 'ht', 'I', 1159940701)
CLIENT_CAMERAYAW: THook =                         THook('ew', 'hm', 'I', 1308821627)
CLIENT_REGION: THook =                            THook('gc', 'gy', 'Lef;', 1)
CLIENT_ISREGIONINSTANCED: THook =                 THook('client', 'gu', 'Z', 1)
CLIENT_REGIONINSTANCES: THook =                   THook('client', 'gb', '[III', 1)
CLIENT_PLANE: THook =                             THook('w', 'kt', 'I', 2060435919)
CLIENT_BASEX: THook =                             THook('ek', 'gs', 'I', 1831338455)
CLIENT_BASEY: THook =                             THook('h', 'gm', 'I', 1706879037)
CLIENT_DESTINATIONX: THook =                      THook('client', 'qy', 'I', 12933011)
CLIENT_DESTINATIONY: THook =                      THook('client', 'qb', 'I', 1660756197)
CLIENT_SINE: THook =                              THook('et', 'i', '[I', 1)
CLIENT_COSINE: THook =                            THook('et', 'ab', '[I', 1)
CLIENT_TILEHEIGHTS: THook =                       THook('bw', 'f', '[[[I', 1)
CLIENT_TILESETTINGS: THook =                      THook('bw', 'b', '[[[B', 1)
CLIENT_ITEMNODECACHE: THook =                     THook('bv', 'f', 'Llp;', 1)
CLIENT_WIDGETS: THook =                           THook('ht', 'k', '[[Lht;', 1)
CLIENT_GAMESETTINGS: THook =                      THook('hs', 'l', '[I', 1)
CLIENT_WIDGETNODECACHE: THook =                   THook('client', 'mm', 'Llp;', 1)
CLIENT_WIDGETPOSITIONX: THook =                   THook('client', 'ol', '[I', 1)
CLIENT_WIDGETPOSITIONY: THook =                   THook('client', 'oh', '[I', 1)
CLIENT_WIDGETWIDTHS: THook =                      THook('client', 'ob', '[I', 1)
CLIENT_WIDGETHEIGHTS: THook =                     THook('client', 'on', '[I', 1)
CLIENT_VALIDWIDGETS: THook =                      THook('ht', 'c', '[Z', 1)
CLIENT_WIDGETROOTINTERFACE: THook =               THook('client', 'mn', 'I', -906778899)
CLIENT_VIEWPORTWIDTH: THook =                     THook('client', 'sm', 'I', -1821649225)
CLIENT_VIEWPORTHEIGHT: THook =                    THook('client', 'sq', 'I', 637100393)
CLIENT_VIEWPORTSCALE: THook =                     THook('client', 'sl', 'I', -462473275)
CLIENT_MAPANGLE: THook =                          THook('client', 'hc', 'I', 694250825)
CLIENT_MAPSCALE: THook =                          THook('client', 'N/A', 'N/A', 1)
CLIENT_MAPOFFSET: THook =                         THook('client', 'N/A', 'N/A', 1)
CLIENT_MENUCOUNT: THook =                         THook('client', 'lb', 'I', -315201447)
CLIENT_MENUACTIONS: THook =                       THook('client', 'la', '[Ljava/lang/String;', 1)
CLIENT_MENUOPTIONS: THook =                       THook('client', 'll', '[Ljava/lang/String;', 1)
CLIENT_ISMENUOPEN: THook =                        THook('client', 'lg', 'Z', 1)
CLIENT_MENUX: THook =                             THook('hw', 'lv', 'I', 1585489899)
CLIENT_MENUY: THook =                             THook('ak', 'lx', 'I', -654673941)
CLIENT_MENUWIDTH: THook =                         THook('bp', 'ld', 'I', 1074315087)
CLIENT_MENUHEIGHT: THook =                        THook('gw', 'lt', 'I', 271502915)
CLIENT_CURRENTLEVELS: THook =                     THook('client', 'kb', '[I', 1)
CLIENT_REALLEVELS: THook =                        THook('client', 'kh', '[I', 1)
CLIENT_EXPERIENCES: THook =                       THook('client', 'ln', '[I', 1)
CLIENT_CURRENTWORLD: THook =                      THook('client', 'bb', 'I', 380841186)
CLIENT_ENERGY: THook =                            THook('client', 'mq', 'I', 1875055983)
CLIENT_WEIGHT: THook =                            THook('client', 'mt', 'I', 373944835)