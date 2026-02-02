from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
from kivy.core.window import Window

# إعدادات حجم الشاشة لتناسب الموبايل
Window.softinput_mode = "below_target"

class HeimaOS(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" # الوضع الليلي
        self.theme_cls.primary_palette = "BlueGray" # لون احترافي
        
        screen = MDScreen()
        
        # التخطيط الرئيسي
        main_layout = MDBoxLayout(orientation='vertical')
        
        # 1. شريط العنوان (Top Bar)
        toolbar = MDTopAppBar(title="Heima OS Control Center")
        main_layout.add_widget(toolbar)
        
        # 2. منطقة عرض الحالة (Status Panel)
        status_card = MDCard(
            orientation='vertical',
            padding="20dp",
            size_hint=(0.9, 0.2),
            pos_hint={"center_x": 0.5, "top": 0.8},
            elevation=4,
            radius=[20, 20, 20, 20]
        )
        self.status_label = MDLabel(
            text="نظام Heima جاهز للعمل\nالأدوات النشطة: 0",
            halign="center",
            theme_text_color="Secondary"
        )
        status_card.add_widget(self.status_label)
        main_layout.add_widget(status_card)

        # 3. شبكة الأزرار (Action Buttons)
        buttons_layout = MDBoxLayout(
            orientation='vertical', 
            spacing="15dp", 
            padding="40dp",
            size_hint_y=0.6
        )

        # زر رادار الصيد
        btn_radar = MDFillRoundFlatIconButton(
            icon="radar", text="تشغيل رادار الصيد التلقائي",
            size_hint_x=1, on_release=self.start_radar
        )
        
        # زر الذكاء الاصطناعي
        btn_ai = MDFillRoundFlatIconButton(
            icon="brain", text="تفعيل مخ الذكاء الاصطناعي",
            size_hint_x=1, on_release=self.start_ai
        )
        
        # زر فحص النظام
        btn_scan = MDFillRoundFlatIconButton(
            icon="shield-search", text="فحص أمان النظام والشبكة",
            size_hint_x=1, on_release=self.system_scan
        )

        buttons_layout.add_widget(btn_radar)
        buttons_layout.add_widget(btn_ai)
        buttons_layout.add_widget(btn_scan)
        
        main_layout.add_widget(buttons_layout)
        screen.add_widget(main_layout)
        return screen

    # وظائف تجريبية للأزرار
    def start_radar(self, *args):
        self.status_label.text = "📡 الرادار يعمل الآن..\nيتم فحص القنوات..."
        
    def start_ai(self, *args):
        self.status_label.text = "🧠 تم تفعيل Ollama..\nأنا جاهز لتحليل البيانات"
        
    def system_scan(self, *args):
        self.status_label.text = "🔍 جاري فحص المنافذ والشبكة..\nبرجاء الانتظار"

if __name__ == "__main__":
    HeimaOS().run()
