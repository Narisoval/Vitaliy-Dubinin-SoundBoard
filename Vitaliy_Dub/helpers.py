from kivy.core.audio import SoundLoader
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem
def change_dict_gachi():
    dict["phrase4"]["audio"] = SoundLoader.load("./audio/rip-ears.mp3")

def change_dict_ungachi():
    dict["phrase4"]["audio"] = SoundLoader.load("./audio/tata.mp3")

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
            ScrollView
                MDGridLayout:
                    cols:2
                    padding : [25,'60dp',30,30]
                    spacing : ['1.5dp','1.5dp']
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
                source: './icons/vetal.jpeg'
            ScrollView:
                MDList:
                    id: list

     '''
dict = {
"phrase1":{
        "text": "Ходили за пивом",
        "audio" : SoundLoader.load("./audio/mi_xodili_za_pivom.mp3")},
"phrase2": {
        "text":"Бывшые военные",
        "audio" : SoundLoader.load("./audio/letchiki.mp3")},
"phrase3": {
            "text" : "Козлы",
            "audio": SoundLoader.load("./audio/kozli.mp3")},
"phrase4": {
            "text" : "Рэп",
            "audio": SoundLoader.load("./audio/tata.mp3")},
"phrase5": {
            "text" : "Сколько вам лет?",
            "audio": SoundLoader.load("./audio/vosrast.mp3")},
"phrase6": {
            "text" : "Я хочу рэп спеть",
            "audio": SoundLoader.load("./audio/xochu_rep_spet.mp3")},
"phrase7": {
           "text" : "Рэп 2",
            "audio": SoundLoader.load("./audio/rap2.mp3")},
"phrase8": {
           "text" : "Очаковское",
            "audio": SoundLoader.load("./audio/ochakovo.mp3")},
"phrase9": {
           "text" : "Улица роз",
            "audio": SoundLoader.load("./audio/ulica_roz.mp3")},
"phrase10": {
           "text" : "Коллапс",
            "audio": SoundLoader.load("./audio/collaps.mp3")},
"phrase11": {
           "text" : "Виталик",
            "audio": SoundLoader.load("./audio/vitalic.mp3")},
"phrase12": {
           "text" : "Апельсин",
            "audio": SoundLoader.load("./audio/apelcin.mp3")},
"phrase13": {
           "text" : "Стопарь",
            "audio": SoundLoader.load("./audio/stopar.mp3")},
"phrase14": {
           "text" : "Все время",
            "audio": SoundLoader.load("./audio/menya_zactavlyt.mp3")},
"phrase15": {
           "text" : "Я повязан",
            "audio": SoundLoader.load("./audio/povyazan.mp3")},
"phrase16": {
           "text" : "Как учили",
            "audio": SoundLoader.load("./audio/strelbisha.mp3")},
"phrase17" : {
            "text" : "Телевизор",
            "audio" : SoundLoader.load("./audio/televizor.mp3")},
"phrase18" : {
            "text" : "Заливается...",
            "audio" : SoundLoader.load("./audio/vilivayetsa.mp3")}

}


class krichLabel(MDLabel):
    def __init__(self, num):
        super().__init__(text = dict[f"phrase{num}"]["text"],
                    font_style = 'Caption',
                    theme_text_color = 'Primary')
