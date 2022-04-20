russ = """
<ReportUrlScreen>:
    name:'report'
    FitImage:
        source:"themes\classic_theme\Rating.png"
    
    MDToolbar:
        title:"Report URL" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    MDLabel:
        text:'This is report url screen'

"""
rus = """
# ScreenManager:
#     ReportUrlScreen:   
<ReportUrlScreen>:
    name:'report'
    MDToolbar:
        title:"Report URL"
        pos_hint:{'top':1.0}  
        #left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10

    MDTextField:
        id: Rurl
        pos_hint: {"center_y": .6}
        hint_text: 'User:'
        normal_color: app.theme_cls.accent_color
        required: True

    BoxLayout:
        pos_hint: {"center_y": .5}
        size_hint_y: None
        height: '5dp'
        MDSlider:
            id: slide
            min: 0.0
            max: 10.0
            value: 5.0
            right_icon: 'android'

    MDRoundFlatButton:
        text:"Submit" 
        text_color: 0, 1, 0, 1
        pos_hint:{'center_x': 0.8, 'center_y': 0.4}
        size_hint:(0.045, 0.05)
        disabled:True if Rurl.text== '' else False
        on_press: app.input_rate()

    # MDLabel:
    #     text:'This is report url screen'

    # MDCard:
    #     size_hint:.8,.75
    #     pos_hint:{'center_x': 0.5, 'center_y': 0.45}
    #     elevation:40
    #     MDFloatLayout:    
    #         MDTextField:
    #             id:mail
    #             icon_right:'email'
    #             hint_text:"E-mail"
    #             helper_text:"example@gmail.com"
    #             helper_text_mode:"on_focus"
    #             pos_hint:{'center_x': 0.5, 'center_y': 0.80}
    #             #size_hint_x:None
    #             #width:250
    #             color_mode:'accent'
    #             required:True
"""