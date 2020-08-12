#encoding: utf-8
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivy.core.audio import Sound
from kivymd.uix.dialog import MDDialog
from helpers import *




class mainApp(MDApp):

    def mybutton(self,num):
        return MDIconButton(icon=self.main_icon,
                            on_press=lambda e: self.play_sound(dict[f"phrase{num}"]["audio"]))
    def build_config(self,config):
        config.setdefaults('section1',{
            'Theme' : 'Light',
             'Icon' : './icons/dd.png'
        })
    def build(self):
        config = self.config
        self.theme_cls.theme_style = config.get('section1','Theme')
        self.main_icon = config.get('section1','Icon')
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = '700'
        #TEMPS
        self.check_list = []
        self.previous_path = ""
        return Builder.load_string(helper)

    def theme_icon(self):
        if self.theme_cls.theme_style == 'Light':
            return './icons/chern.png'
        else:
            return './icons/bel.png'

    def on_start(self):
        for i in range(1,18,2):
            btn1 = self.mybutton(i)
            btn2 = self.mybutton(i+1)
            lbl1 = krichLabel(i)
            lbl2 = krichLabel(i+1)
            self.root.ids.layout.add_widget(btn1)
            self.root.ids.layout.add_widget(btn2)
            self.root.ids.layout.add_widget(lbl1)
            self.root.ids.layout.add_widget(lbl2)
        #NAV DRAWER(LIST) 
        theme_changer = Item(text= 'Изменить темку', source = self.theme_icon(), on_press = self.change_theme)
        self.icon_changer = Item(text = 'Изменить значок', source = self.main_icon, on_press = self.show_dialog)

        self.root.ids.list.add_widget(theme_changer)
        self.root.ids.list.add_widget(self.icon_changer)

    def change_theme(self,obj):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
           self.theme_cls.theme_style = 'Light'
        self.root.ids.list.clear_widgets()
        theme_changer = Item(text= 'Изменить темку', source = self.theme_icon(), on_press = self.change_theme)
        self.root.ids.list.add_widget(theme_changer)
        self.root.ids.list.add_widget(self.icon_changer)

    dialog = None
    def show_dialog(self, obj):
        self.dialog = MDDialog(
            type="simple",
            size_hint = (.7,.8),
            items=[
                Item(text = 'Стандартная картинка', source = './icons/dd.png', on_press = lambda e : self.checkIcon('./icons/dd.png')),
                Item(text = 'Виталий Алексеевич', source = './icons/Vetal.png', on_press =  self.vitalic),
                Item(text = 'Ария лого', source = './icons/Aria.png', on_press = lambda e : self.checkIcon('./icons/Aria.png')),
                Item(text='Знак Анархии', source= './icons/A.png', on_press = lambda e : self.checkIcon('./icons/A.png')),
                Item(text = 'ALT11', source = './icons/male.png', on_press = self.gachi),
                Item(text = 'Коза', source = './icons/koza.png', on_press = lambda e : self.checkIcon('./icons/koza.png')),
                Item(text = 'Бас', source = './icons/Bass.png', on_press = lambda e : self.checkIcon('./icons/Bass.png')),
                Item(text = 'Очаково', source = './icons/ochakovo.png', on_press = self.ochakovo)
            ])
        self.dialog.open()
    def change_icon(self,real_path):
        self.root.ids.layout.clear_widgets()
        self.root.ids.list.clear_widgets()
        self.main_icon = real_path
        self.on_start()
        self.dialog.dismiss()
    def checkIcon(self,path):
        if self.main_icon == path:
            self.dialog.dismiss()
            chosen = MDDialog(text = 'Этот значок уже выбран!', radius = [20,7,20,7])
            chosen.open()
        elif self.previous_path != './icons/male.png':
            self.change_icon(path)
        else:
            change_dict_ungachi()
            self.change_icon(path)


    #SPECIAL CASES
    def gachi(self,obj):
        change_dict_gachi()
        self.checkIcon('./icons/male.png')

    def vitalic(self,obj):
        self.checkIcon('./icons/Vetal.png')
        dict["phrase11"]["audio"].volume = 0.5
        dict["phrase11"]["audio"].play()


    def ochakovo(self,obj):
        self.checkIcon('./icons/ochakovo.png')
        dict["phrase8"]["audio"].volume = 0.5
        dict["phrase8"]["audio"].play()


    def play_sound(self, sound):
        self.check_list.append(sound)
        sound.volume = 0.5
        if len(self.check_list) == 2:
            self.check_list[0].stop()
            self.check_list[1].play()

            self.check_list.pop(0)

        elif len(self.check_list) == 1:
            self.check_list[0].play()
    def on_stop(self):
        self.config.setall('section1',{
            'Theme' : self.theme_cls.theme_style,
            'Icon'  : self.main_icon
        })
        with open('main.ini', 'w') as config:
            self.config.write()

 #ffmpeg -i rap2.wav -ss 0 -to 10 rap2.wav

if __name__ == "__main__":
    mainApp().run()
