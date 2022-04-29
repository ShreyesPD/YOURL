
rus = """ 
<ReportUrlScreen>:
    name:'report'
    FitImage:
        source:"themes\classic_theme\Rating.png"
        
    MDToolbar:
        title:"Ratings"
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10

    MDTextField:
        id: rurl
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        hint_text: 'Enter URL'
        helper_text:"Slide the slider to rate the url"
        helper_text_mode:"on_focus"
        line_color_normal:app.theme_cls.accent_color
        size_hint_x:0.7
        size_hint_y:0.1
        color_mode:'accent'
        required: True

    BoxLayout:
        pos_hint: {"center_y": .45}
        size_hint_y: None
        #height: '5dp'
        MDSlider:
            id: slide
            min: 0.0
            max: 10.0
            value: 5.0
            #right_icon: 'android'
            color:[1,0,0,0.7] if slide.value<5.0 else [0,1,0,0.7]
            
    MDRoundFlatButton:
        text:"Rate it" 
        text_color:app.theme_cls.accent_color
        pos_hint:{'center_x': 0.8, 'center_y': 0.25}
        size_hint:(0.045, 0.05)
        disabled:True if rurl.text== '' else False
        on_press:app.rating_input()   
"""