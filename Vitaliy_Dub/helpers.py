from kivy.core.audio import SoundLoader
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem
def change_dict_gachi():
    dict["phrase4"]["audio"] = SoundLoader.load("./audio/rip-ears.wav")

def change_dict_ungachi():
    dict["phrase4"]["audio"] = SoundLoader.load("./audio/tata.wav")

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()
helper = '''
<Item>
    ImageLeftWidget:
        source: root.source
NavigationLayout:
    ScreenManager:
        Screen:
            MDGridLayout:
                cols:2 
                padding : [25,68,30,30]
                spacing : [15,15]
                id : layout
                

            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    title : "Вставте текст!"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                Widget:
            
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            padding : '8dp'
            spacing : '8dp'
            orientation: 'vertical'
            Image:
                source: './icons/vetal.jpg'
            ScrollView:
                MDList:
                    id: list
                
                                            
    
                        
     '''
dict = {
"phrase1":{
        "text": "Ходили за пивом", 
        "audio" : SoundLoader.load("./audio/mi_xodili_za_pivom.wav")},
"phrase2": {
        "text":"Бывшые военные",
        "audio" : SoundLoader.load("./audio/letchiki.wav")},
"phrase3": {
            "text" : "Козлы",
            "audio": SoundLoader.load("./audio/kozli.wav")},
"phrase4": {
            "text" : "Рэп",
            "audio": SoundLoader.load("./audio/tata.wav")},
"phrase5": {
            "text" : "Сколько вам лет?",
            "audio": SoundLoader.load("./audio/vosrast.wav")},
"phrase6": {
            "text" : "Я хочу рэп спеть",
            "audio": SoundLoader.load("./audio/xochu_rep_spet.wav")},
"phrase7": {
           "text" : "Рэп 2",
            "audio": SoundLoader.load("./audio/rap2.wav")},
"phrase8": {
           "text" : "Очаковское",
            "audio": SoundLoader.load("./audio/ochakovo.wav")},
"phrase9": {
           "text" : "Улица роз",
            "audio": SoundLoader.load("./audio/ulica_roz.wav")},
"phrase10": {
           "text" : "Коллапс",
            "audio": SoundLoader.load("./audio/collaps.wav")},
"phrase11": {
           "text" : "Виталик",
            "audio": SoundLoader.load("./audio/vitalic.wav")},
"phrase12": {
           "text" : "Апельсин",
            "audio": SoundLoader.load("./audio/apelcin.wav")},
"phrase13": {
           "text" : "Стопарь",
            "audio": SoundLoader.load("./audio/stopar.wav")},           
"phrase14": {
           "text" : "Все время",
            "audio": SoundLoader.load("./audio/menya_zactavlyt.wav")},
"phrase15": {
           "text" : "Я повязан",
            "audio": SoundLoader.load("./audio/povyazan.wav")},
"phrase16": {
           "text" : "Как учили",
            "audio": SoundLoader.load("./audio/strelbisha.wav")}
}


class krichLabel(MDLabel):
    def __init__(self, num):
        super().__init__(text = dict[f"phrase{num}"]["text"],
                    font_style = 'Caption',
                    theme_text_color = 'Primary')