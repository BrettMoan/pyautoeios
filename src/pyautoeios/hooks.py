import collections

THook = collections.namedtuple("THook", "cls field desc multiplier")

def hook(c: str, f: str, d: str, m: int):
    return THook(c.encode("utf8"), f.encode("utf8"), d.encode("utf8"), m)

NODE_UID = hook("gn", "cm", "J", 1)
NODE_PREV = hook("gn", "ct", "Lgn;", 1)
NODE_NEXT = hook("gn", "cb", "Lgn;", 1)

# {NodeDeque: ja}
NODEDEQUE_HEAD = hook("ja", "f", "Lgn;", 1)
NODEDEQUE_CURRENT = hook("ja", "b", "Lgn;", 1)

# {Cacheable: gp}
CACHEABLE_NEXT = hook("gp", "cj", "Lgp;", 1)
CACHEABLE_PREV = hook("gp", "cd", "Lgp;", 1)

# {LinkedList: js}
LINKEDLIST_HEAD = hook("js", "f", "Lgn;", 1)
LINKEDLIST_CURRENT = hook("js", "b", "Lgn;", 1)

# {HashTable: lp}
HASHTABLE_HEAD = hook("lp", "l", "Lgn;", 1)
HASHTABLE_TAIL = hook("lp", "m", "Lgn;", 1)
HASHTABLE_BUCKETS = hook("lp", "b", "[Lgn;", 1)
HASHTABLE_INDEX = hook("lp", "z", "I", 1)
HASHTABLE_SIZE = hook("lp", "f", "I", 1)

# {IterableHashTable: ll}
ITERABLEHASHTABLE_HEAD = hook("ll", "l", "Lgn;", 1)
ITERABLEHASHTABLE_TAIL = hook("ll", "m", "Lgn;", 1)
ITERABLEHASHTABLE_BUCKETS = hook("ll", "b", "[Lgn;", 1)
ITERABLEHASHTABLE_INDEX = hook("ll", "z", "I", 1)
ITERABLEHASHTABLE_SIZE = hook("ll", "f", "I", 1)

# {Queue: jt}
QUEUE_HEAD = hook("jt", "b", "Lgp;", 1)

# {Cache: ev}
CACHE_HASHTABLE = hook("ev", "m", "Lll;", 1)
CACHE_QUEUE = hook("ev", "z", "Ljt;", 1)
CACHE_REMAINING = hook("ev", "l", "I", 1)
CACHE_CAPACITY = hook("ev", "b", "I", 1)

# {ClassData: dv}
CLASSDATA_BYTES = hook("dv", "m", "[[[B", 1)
CLASSDATA_METHODS = hook("dv", "c", "[Ljava/lang/reflect/Method;", 1)
CLASSDATA_FIELDS = hook("dv", "k", "[Ljava/lang/reflect/Field;", 1)

# {Rasteriser: lm}
RASTERISER_PIXELS = hook("lm", "ac", "[I", 1)
RASTERISER_WIDTH = hook("lm", "ao", "I", 1)
RASTERISER_HEIGHT = hook("lm", "af", "I", 1)

# {Rasteriser3D: et}
RASTERISER3D_SHADOWDECAY = hook("et", "g", "[I", 1)
RASTERISER3D_SINETABLE = hook("et", "i", "[I", 1)
RASTERISER3D_COSINETABLE = hook("et", "ab", "[I", 1)

# {Typeface: ky}
TYPEFACE_CHARACTERPIXELS = hook("ky", "f", "[[B", 1)

# {IndexedRGB: le}
INDEXEDRGB_PIXELS = hook("le", "b", "[I", 1)
INDEXEDRGB_PALETTE = hook("le", "f", "[B", 1)

# {ImageRGB: lc}
IMAGERGB_PIXELS = hook("lc", "f", "[I", 1)
IMAGERGB_WIDTH = hook("lc", "b", "I", 1)
IMAGERGB_HEIGHT = hook("lc", "l", "I", 1)
IMAGERGB_MAXWIDTH = hook("lc", "q", "I", 1)
IMAGERGB_MAXHEIGHT = hook("lc", "k", "I", 1)

# {Keyboard: bp}

# {GameShell: ba}

# {Buffer: kb}
BUFFER_PAYLOAD = hook("kb", "q", "[B", 1)
BUFFER_CRC = hook("kb", "c", "[I", 1)

# {BufferedConnection: fa}
BUFFEREDCONNECTION_INPUTSTREAM = hook("fa", "f", "Ljava/io/InputStream;", 1)
BUFFEREDCONNECTION_OUTPUTSTREAM = hook("fa", "b", "Ljava/io/OutputStream;", 1)
BUFFEREDCONNECTION_SOCKET = hook("fa", "l", "Ljava/net/Socket;", 1)
BUFFEREDCONNECTION_PAYLOAD = hook("fa", "k", "[B", 1)
BUFFEREDCONNECTION_ISCLOSED = hook("fa", "m", "Z", 1)

# {CollisionMap: fh}
COLLISIONMAP_WIDTH = hook("fh", "ak", "I", -2103042709)
COLLISIONMAP_HEIGHT = hook("fh", "au", "I", 442513137)
COLLISIONMAP_ADJACENCY = hook("fh", "ai", "[[I", 1)

# {NameInfo: km}
NAMEINFO_NAME = hook("km", "f", "Ljava/lang/String;", 1)
NAMEINFO_DECODEDNAME = hook("km", "b", "Ljava/lang/String;", 1)

# {Renderable: ej}
RENDERABLE_MODELHEIGHT = hook("ej", "cu", "I", 1647777713)

# {Region: ef}
REGION_SCENETILES = hook("ef", "q", "[[[Leo;", 1)
REGION_INTERACTABLEOBJECTS = hook("ef", "u", "[Lel;", 1)

# {AnimableNode: ck}
ANIMABLENODE_ID = hook("ck", "f", "I", -550843083)
ANIMABLENODE_ANIMATIONSEQUENCE = hook("ck", "k", "Ljg;", 1)
ANIMABLENODE_FLAGS = hook("ck", "b", "I", 174390429)
ANIMABLENODE_ORIENTATION = hook("ck", "l", "I", 89407283)
ANIMABLENODE_PLANE = hook("ck", "m", "I", -1374963731)
ANIMABLENODE_X = hook("ck", "z", "I", -2010464009)
ANIMABLENODE_Y = hook("ck", "q", "I", 647351421)

# {BoundaryObject: em}
BOUNDARYOBJECT_ID = hook("em", "c", "J", -3078711070799260957)
BOUNDARYOBJECT_FLAGS = hook("em", "u", "I", -810696597)
BOUNDARYOBJECT_PLANE = hook("em", "f", "I", 24178129)
BOUNDARYOBJECT_HEIGHT = hook("em", "z", "I", 237050093)
BOUNDARYOBJECT_LOCALX = hook("em", "b", "I", 840836709)
BOUNDARYOBJECT_LOCALY = hook("em", "l", "I", 511451679)
BOUNDARYOBJECT_ORIENTATION = hook("em", "m", "I", 1059090271)
BOUNDARYOBJECT_RENDERABLE = hook("em", "q", "Lej;", 1)
BOUNDARYOBJECT_RENDERABLE2 = hook("em", "k", "Lej;", 1)

# {WallDecoration: ey}
WALLDECORATION_ID = hook("ey", "t", "J", -3894207238426267157)
WALLDECORATION_FLAGS = hook("ey", "e", "I", -237175035)
WALLDECORATION_PLANE = hook("ey", "f", "I", -1368883061)
WALLDECORATION_HEIGHT = hook("ey", "z", "I", -1005575771)
WALLDECORATION_LOCALX = hook("ey", "b", "I", 1255836875)
WALLDECORATION_LOCALY = hook("ey", "l", "I", 1394186747)
WALLDECORATION_RELATIVEX = hook("ey", "q", "I", 287109355)
WALLDECORATION_RELATIVEY = hook("ey", "k", "I", -872509349)
WALLDECORATION_ORIENTATION = hook("ey", "m", "I", -1069815711)
WALLDECORATION_RENDERABLE = hook("ey", "c", "Lej;", 1)
WALLDECORATION_RENDERABLE2 = hook("ey", "u", "Lej;", 1)

# {FloorDecoration: ek}
FLOORDECORATION_ID = hook("ek", "m", "J", 2791850332732375269)
FLOORDECORATION_FLAGS = hook("ek", "q", "I", -1457303601)
FLOORDECORATION_LOCALX = hook("ek", "b", "I", -191694913)
FLOORDECORATION_LOCALY = hook("ek", "l", "I", 489421685)
FLOORDECORATION_PLANE = hook("ek", "f", "I", 1613676277)
FLOORDECORATION_RENDERABLE = hook("ek", "z", "Lej;", 1)

# {GameObject: el}
GAMEOBJECT_RENDERABLE = hook("el", "z", "Lej;", 1)
GAMEOBJECT_ID = hook("el", "n", "J", -2637081015005136759)
GAMEOBJECT_FLAGS = hook("el", "x", "I", -735597717)
GAMEOBJECT_ORIENTATION = hook("el", "m", "I", -1596359689)
GAMEOBJECT_PLANE = hook("el", "f", "I", -1412668883)
GAMEOBJECT_HEIGHT = hook("el", "b", "I", -1556347637)
GAMEOBJECT_LOCALX = hook("el", "l", "I", 954361615)
GAMEOBJECT_LOCALY = hook("el", "q", "I", 1994666041)
GAMEOBJECT_WORLDX = hook("el", "k", "I", 207668277)
GAMEOBJECT_WORLDY = hook("el", "u", "I", 1266358135)
GAMEOBJECT_OFFSETX = hook("el", "c", "I", -1940452637)
GAMEOBJECT_OFFSETY = hook("el", "t", "I", 1643778515)

# {SceneTile: eo}
SCENETILE_BOUNDARYOBJECT = hook("eo", "k", "Lem;", 1)
SCENETILE_SCENETILEOBJECT = hook("eo", "a", "Leo;", 1)
SCENETILE_GAMEOBJECT = hook("eo", "o", "[Lel;", 1)
SCENETILE_WALLDECORATION = hook("eo", "c", "Ley;", 1)
SCENETILE_GROUNDDECORATION = hook("eo", "u", "Lek;", 1)
SCENETILE_LOCALX = hook("eo", "b", "I", 1121105615)
SCENETILE_LOCALY = hook("eo", "l", "I", -541915111)
SCENETILE_PLANE = hook("eo", "m", "I", 102326407)

# {GrandExchange: j}
TRADINGPOST_STATUS = hook("j", "f", "B", 1)
TRADINGPOST_ITEMID = hook("j", "b", "I", 1175311391)
TRADINGPOST_PRICE = hook("j", "l", "I", 1620049031)
TRADINGPOST_QUANTITY = hook("j", "m", "I", -658451115)
TRADINGPOST_TRANSFERRED = hook("j", "z", "I", 682864265)
TRADINGPOST_SPENT = hook("j", "q", "I", 1)
TRADINGPOST_QUERYIDS = hook("j", "N/A", "N/A", 1)

# {Model: eh}
MODEL_INDICESX = hook("eh", "t", "[I", 1)
MODEL_INDICESY = hook("eh", "e", "[I", 1)
MODEL_INDICESZ = hook("eh", "o", "[I", 1)
MODEL_INDICESLENGTH = hook("eh", "u", "I", 1)
MODEL_VERTICESX = hook("eh", "q", "[I", 1)
MODEL_VERTICESY = hook("eh", "k", "[I", 1)
MODEL_VERTICESZ = hook("eh", "c", "[I", 1)
MODEL_VERTICESLENGTH = hook("eh", "z", "I", 1)
MODEL_TEXINDICESX = hook("eh", "n", "[I", 1)
MODEL_TEXINDICESY = hook("eh", "x", "[I", 1)
MODEL_TEXINDICESZ = hook("eh", "p", "[I", 1)
MODEL_TEXVERTICESX = hook("eh", "d", "[I", 1)
MODEL_TEXVERTICESY = hook("eh", "a", "[I", 1)
MODEL_TEXVERTICESZ = hook("eh", "g", "[I", 1)
MODEL_TEXVERTICESLENGTH = hook("eh", "v", "I", 1)
MODEL_SKINS = hook("eh", "h", "[[I", 1)
MODEL_SHADOWINTENSITY = hook("eh", "af", "I", 1)
MODEL_FITSSINGLETILE = hook("eh", "ab", "Z", 1)

# {AnimationSequence: jg}
ANIMATIONSEQUENCE_FRAMES = hook("jg", "q", "[I", 1)
ANIMATIONSEQUENCE_SEQUENCECACHE = hook("jg", "m", "Lev;", 1)
ANIMATIONSEQUENCE_FRAMECACHE = hook("jg", "z", "Lev;", 1)

# {AnimationFrames: ex}
ANIMATIONFRAMES_FRAMES = hook("ex", "f", "[Ler;", 1)

# {AnimationSkeleton: ei}
ANIMATIONSKELETON_ID = hook("ei", "f", "I", 2017085485)
ANIMATIONSKELETON_TRANSFORMATIONCOUNT = hook("ei", "b", "I", 244564821)
ANIMATIONSKELETON_TRANSFORMATIONTYPES = hook("ei", "l", "[I", 1)
ANIMATIONSKELETON_TRANSFORMATIONS = hook("ei", "m", "[[I", 1)

# {Animation: er}
ANIMATION_FRAMECOUNT = hook("er", "q", "I", 1)
ANIMATION_FRAMES = hook("er", "k", "[I", 1)
ANIMATION_TRANSFORMX = hook("er", "c", "[I", 1)
ANIMATION_TRANSFORMY = hook("er", "u", "[I", 1)
ANIMATION_TRANSFORMZ = hook("er", "t", "[I", 1)
ANIMATION_SKELETON = hook("er", "z", "Lei;", 1)

# {CombatInfo1: ce}
COMBATINFO1_HEALTH = hook("ce", "l", "I", -733805573)
COMBATINFO1_HEALTHRATIO = hook("ce", "b", "I", 1850182953)

# {CombatInfo2: ix}
COMBATINFO2_HEALTHSCALE = hook("ix", "p", "I", 185744125)

# {CombatInfoList: js}
COMBATINFOLIST_HEAD = hook("js", "f", "Lgn;", 1)
COMBATINFOLIST_CURRENT = hook("js", "b", "Lgn;", 1)

# {CombatInfoHolder: cx}
COMBATINFOHOLDER_COMBATINFOLIST = hook("cx", "m", "Ljs;", 1)
COMBATINFOHOLDER_COMBATINFO2 = hook("cx", "l", "Lix;", 1)

# {Actor: cs}
ACTOR_ANIMATION = hook("cs", "bt", "I", -254649357)
ACTOR_ANIMATIONDELAY = hook("cs", "y", "I", -370859363)
ACTOR_ANIMATIONFRAME = hook("cs", "bw", "I", 1925242573)
ACTOR_MOVEMENTSEQUENCE = hook("cs", "bo", "I", 1355414019)
ACTOR_MOVEMENTFRAME = hook("cs", "be", "I", 878455421)
ACTOR_CURRENTSEQUENCE = hook("cs", "ak", "I", 790102969)
ACTOR_SPOKENTEXT = hook("cs", "am", "Ljava/lang/String;", 1)
ACTOR_HITDAMAGES = hook("cs", "ad", "[I", 1)
ACTOR_HITTYPES = hook("cs", "bb", "[I", 1)
ACTOR_HITCYCLE = hook("cs", "bf", "[I", 1)
ACTOR_QUEUEX = hook("cs", "cy", "[I", 1)
ACTOR_QUEUEY = hook("cs", "cx", "[I", 1)
ACTOR_QUEUETRAVERSED = hook("cs", "ca", "[B", 1)
ACTOR_QUEUESIZE = hook("cs", "ci", "I", -1827352877)
ACTOR_LOCALX = hook("cs", "af", "I", -952501591)
ACTOR_LOCALY = hook("cs", "av", "I", 1794864455)
ACTOR_COMBATCYCLE = hook("cs", "N/A", "N/A", 1)
ACTOR_INTERACTINGINDEX = hook("cs", "bj", "I", -49521303)
ACTOR_ORIENTATION = hook("cs", "cp", "I", 501904063)
ACTOR_ISWALKING = hook("cs", "ay", "Z", 1)
ACTOR_TARGETINDEX = hook("cs", "bj", "I", -49521303)
ACTOR_COMBATINFOLIST = hook("cs", "bc", "Ljs;", 1)
ACTOR_SPOTANIMATION = hook("cs", "bv", "I", 1626363285)
ACTOR_SPOTANIMATIONFRAME = hook("cs", "br", "I", -1912022721)
ACTOR_SPOTANIMATIONFRAMECYCLE = hook("cs", "bs", "I", 806708579)
ACTOR_GRAPHICSID = hook("cs", "N/A", "N/A", 1)
ACTOR_HEIGHT = hook("cs", "cg", "I", 1789811467)

# {NPCDefinition: jn}
NPCDEFINITION_ID = hook("jn", "z", "I", -241449157)
NPCDEFINITION_NAME = hook("jn", "q", "Ljava/lang/String;", 1)
NPCDEFINITION_ACTIONS = hook("jn", "v", "[Ljava/lang/String;", 1)
NPCDEFINITION_MODELIDS = hook("jn", "c", "[I", 1)
NPCDEFINITION_COMBATLEVEL = hook("jn", "a", "I", 1396717947)
NPCDEFINITION_VISIBLE = hook("jn", "i", "Z", 1)
NPCDEFINITION_MODELCACHE = hook("jn", "m", "Lev;", 1)
NPCDEFINITION_TRANSFORMATIONS = hook("jn", "av", "[I", 1)
NPCDEFINITION_MODELTILESIZE = hook("jn", "k", "i", 2022516453)
NPCDEFINITION_MODELSCALEWIDTH = hook("jn", "g", "i", 9158797)
NPCDEFINITION_MODELSCALEHEIGHT = hook("jn", "h", "i", -174548931)

# {NPC: ca}
NPC_DEFINITION = hook("ca", "f", "Ljn;", 1)

# {PlayerDefinition: hu}
PLAYERDEFINITION_NPCTRANSFORMID = hook("hu", "m", "I", 1998131209)
PLAYERDEFINITION_ISFEMALE = hook("hu", "l", "Z", 1)
PLAYERDEFINITION_ANIMATEDMODELID = hook("hu", "z", "J", -3297432427762095127)
PLAYERDEFINITION_MODELID = hook("hu", "q", "J", -3842356906884846791)
PLAYERDEFINITION_EQUIPMENT = hook("hu", "f", "[I", 1)
PLAYERDEFINITION_MODELCACHE = hook("hu", "o", "Lev;", 1)

# {Player: bi}
PLAYER_NAME = hook("bi", "f", "Lkm;", 1)
PLAYER_MODEL = hook("bi", "p", "Leh;", 1)
PLAYER_VISIBLE = hook("bi", "w", "Z", 1)
PLAYER_DEFINITION = hook("bi", "b", "Lhu;", 1)
PLAYER_COMBATLEVEL = hook("bi", "k", "I", -953649939)
PLAYER_INDEX = hook("bi", "g", "I", -1613823593)
PLAYER_ISANIMATING = hook("bi", "w", "Z", 1)

# {ObjectDefinition: je}
OBJECTDEFINITION_ID = hook("je", "u", "I", 1144020119)
OBJECTDEFINITION_DEFINITIONCACHE = hook("je", "m", "Lev;", 1)
OBJECTDEFINITION_MODELCACHE = hook("je", "k", "Lev;", 1)
OBJECTDEFINITION_MODELIDS = hook("je", "t", "[I", 1)
OBJECTDEFINITION_MODELS = hook("je", "e", "[I", 1)
OBJECTDEFINITION_NAME = hook("je", "o", "Ljava/lang/String;", 1)
OBJECTDEFINITION_ACTIONS = hook("je", "ao", "[Ljava/lang/String;", 1)
OBJECTDEFINITION_TRANSFORMATIONS = hook("je", "an", "[I", 1)
OBJECTDEFINITION_TRANSFORMATIONVARBIT = hook("je", "am", "I", 1763689999)
OBJECTDEFINITION_TRANSFORMATIONVARP = hook("je", "aa", "I", -945520639)

# {WidgetNode: bs}
WIDGETNODE_ID = hook("bs", "f", "I", 1986621351)

# {Widget: ht}
WIDGET_NAME = hook("ht", "dg", "Ljava/lang/String;", 1)
WIDGET_TEXT = hook("ht", "ce", "Ljava/lang/String;", 1)
WIDGET_WIDGETID = hook("ht", "j", "I", -583486671)
WIDGET_PARENTID = hook("ht", "ai", "I", 1412750483)
WIDGET_PARENT = hook("ht", "dv", "Lht;", 1)
WIDGET_ITEMID = hook("ht", "el", "I", -659047965)
WIDGET_INVIDS = hook("ht", "ed", "[I", 1)
WIDGET_STACKSIZES = hook("ht", "ey", "[I", 1)
WIDGET_ITEMAMOUNT = hook("ht", "es", "I", 1581915613)
WIDGET_TEXTUREID = hook("ht", "bf", "I", 372301921)
WIDGET_ACTIONS = hook("ht", "cw", "[Ljava/lang/String;", 1)
WIDGET_ACTIONTYPE = hook("ht", "d", "I", 1601942739)
WIDGET_TYPE = hook("ht", "v", "I", -1823014479)
WIDGET_ISHIDDEN = hook("ht", "ax", "Z", 1)
WIDGET_ABSOLUTEX = hook("ht", "ac", "I", -1326300873)
WIDGET_ABSOLUTEY = hook("ht", "ao", "I", 1422648317)
WIDGET_RELATIVEX = hook("ht", "ar", "I", 371785153)
WIDGET_RELATIVEY = hook("ht", "ay", "I", 766965945)
WIDGET_SCROLLX = hook("ht", "ag", "I", -182885719)
WIDGET_SCROLLY = hook("ht", "aq", "I", 192866787)
WIDGET_WIDTH = hook("ht", "ah", "I", 410180701)
WIDGET_HEIGHT = hook("ht", "az", "I", -1661593933)
WIDGET_CHILDREN = hook("ht", "ee", "[Lht;", 1)
WIDGET_BOUNDSINDEX = hook("ht", "fy", "I", 651630769)
WIDGET_WIDGETCYCLE = hook("ht", "ff", "I", -536480473)

# {ItemDefinition: jk}
ITEMDEFINITION_ID = hook("jk", "x", "I", 205656235)
ITEMDEFINITION_NAME = hook("jk", "r", "Ljava/lang/String;", 1)
ITEMDEFINITION_ISMEMBERS = hook("jk", "ao", "Z", 1)
ITEMDEFINITION_GROUNDACTIONS = hook("jk", "af", "[Ljava/lang/String;", 1)
ITEMDEFINITION_ACTIONS = hook("jk", "av", "[Ljava/lang/String;", 1)
ITEMDEFINITION_CACHE = hook("jk", "t", "Lev;", 1)

# {Item: cb}
ITEM_ID = hook("cb", "f", "I", -459870843)
ITEM_STACKSIZES = hook("cb", "b", "I", 724722271)

# {ItemNode: bv}
ITEMNODE_ITEMIDS = hook("bv", "b", "[I", 1)
ITEMNODE_ITEMQUANTITIES = hook("bv", "l", "[I", 1)
ITEMNODE_CACHE = hook("bv", "f", "Llp;", 1)

# {Varps: hs}
VARPS_MASKS = hook("hs", "f", "[I", 1)
VARPS_MAIN = hook("hs", "l", "[I", 1)

# {VarbitDefinition: iy}
VARBITDEFINITION_CACHE = hook("iy", "b", "Lev;", 1)
VARBITDEFINITION_BASE = hook("iy", "l", "I", 1810404981)
VARBITDEFINITION_STARTBIT = hook("iy", "m", "I", -581436309)
VARBITDEFINITION_ENDBIT = hook("iy", "z", "I", 1763957303)

# {Client: client}
CLIENT_REVISION = hook("client", "192", "I", 1)
CLIENT_CLIENT = hook("client", "ap", "Lclient;", 1)
CLIENT_LOCALNPCS = hook("client", "fo", "[Lca;", 1)
CLIENT_NPCINDICES = hook("client", "ff", "[I", 1)
CLIENT_NPCCOUNT = hook("client", "fy", "I", -2146265857)
CLIENT_LOCALPLAYERS = hook("client", "ku", "[Lbi;", 1)
CLIENT_PLAYERINDICES = hook("cv", "k", "[I", 1)
CLIENT_PLAYERCOUNT = hook("client", "N/A", "N/A", 1)
CLIENT_LOCALPLAYER = hook("in", "kz", "Lbi;", 1)
CLIENT_PLAYERINDEX = hook("client", "kl", "I", 1876036055)
CLIENT_LOOPCYCLE = hook("client", "cn", "I", -1633145881)
CLIENT_GAMESTATE = hook("client", "bq", "I", 1008452177)
CLIENT_LOGINSTATE = hook("cj", "au", "I", 1682315035)
CLIENT_ISLOADING = hook("client", "ca", "Z", 1)
CLIENT_CROSSHAIRCOLOR = hook("client", "jv", "I", -1792879987)
CLIENT_ANIMATIONFRAMECACHE = hook("jg", "z", "Lev;", 1)
CLIENT_GROUNDITEMS = hook("client", "ky", "[[[Lja;", 1)
CLIENT_COLLISIONMAP = hook("client", "w", "[Lfh;", 1)
CLIENT_TRADINGPOSTOFFERS = hook("client", "sn", "[Lj;", 1)
CLIENT_CAMERAX = hook("bv", "hu", "I", -966847555)
CLIENT_CAMERAY = hook("at", "hr", "I", 104039997)
CLIENT_CAMERAZ = hook("cr", "hx", "I", -690692767)
CLIENT_CAMERAPITCH = hook("cf", "ht", "I", 1159940701)
CLIENT_CAMERAYAW = hook("ew", "hm", "I", 1308821627)
CLIENT_REGION = hook("gc", "gy", "Lef;", 1)
CLIENT_ISREGIONINSTANCED = hook("client", "gu", "Z", 1)
CLIENT_REGIONINSTANCES = hook("client", "gb", "[III", 1)
CLIENT_PLANE = hook("w", "kt", "I", 2060435919)
CLIENT_BASEX = hook("ek", "gs", "I", 1831338455)
CLIENT_BASEY = hook("h", "gm", "I", 1706879037)
CLIENT_DESTINATIONX = hook("client", "qy", "I", 12933011)
CLIENT_DESTINATIONY = hook("client", "qb", "I", 1660756197)
CLIENT_SINE = hook("et", "i", "[I", 1)
CLIENT_COSINE = hook("et", "ab", "[I", 1)
CLIENT_TILEHEIGHTS = hook("bw", "f", "[[[I", 1)
CLIENT_TILESETTINGS = hook("bw", "b", "[[[B", 1)
CLIENT_ITEMNODECACHE = hook("bv", "f", "Llp;", 1)
CLIENT_WIDGETS = hook("ht", "k", "[[Lht;", 1)
CLIENT_GAMESETTINGS = hook("hs", "l", "[I", 1)
CLIENT_WIDGETNODECACHE = hook("client", "mm", "Llp;", 1)
CLIENT_WIDGETPOSITIONX = hook("client", "ol", "[I", 1)
CLIENT_WIDGETPOSITIONY = hook("client", "oh", "[I", 1)
CLIENT_WIDGETWIDTHS = hook("client", "ob", "[I", 1)
CLIENT_WIDGETHEIGHTS = hook("client", "on", "[I", 1)
CLIENT_VALIDWIDGETS = hook("ht", "c", "[Z", 1)
CLIENT_WIDGETROOTINTERFACE = hook("client", "mn", "I", -906778899)
CLIENT_VIEWPORTWIDTH = hook("client", "sm", "I", -1821649225)
CLIENT_VIEWPORTHEIGHT = hook("client", "sq", "I", 637100393)
CLIENT_VIEWPORTSCALE = hook("client", "sl", "I", -462473275)
CLIENT_MAPANGLE = hook("client", "hc", "I", 694250825)
CLIENT_MAPSCALE = hook("client", "N/A", "N/A", 1)
CLIENT_MAPOFFSET = hook("client", "N/A", "N/A", 1)
CLIENT_MENUCOUNT = hook("client", "lb", "I", -315201447)
CLIENT_MENUACTIONS = hook("client", "la", "[Ljava/lang/String;", 1)
CLIENT_MENUOPTIONS = hook("client", "ll", "[Ljava/lang/String;", 1)
CLIENT_ISMENUOPEN = hook("client", "lg", "Z", 1)
CLIENT_MENUX = hook("hw", "lv", "I", 1585489899)
CLIENT_MENUY = hook("ak", "lx", "I", -654673941)
CLIENT_MENUWIDTH = hook("bp", "ld", "I", 1074315087)
CLIENT_MENUHEIGHT = hook("gw", "lt", "I", 271502915)
CLIENT_CURRENTLEVELS = hook("client", "kb", "[I", 1)
CLIENT_REALLEVELS = hook("client", "kh", "[I", 1)
CLIENT_EXPERIENCES = hook("client", "ln", "[I", 1)
CLIENT_CURRENTWORLD = hook("client", "bb", "I", 380841186)
CLIENT_ENERGY = hook("client", "mq", "I", 1875055983)
CLIENT_WEIGHT = hook("client", "mt", "I", 373944835)
