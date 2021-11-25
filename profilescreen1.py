ps1 = """
<ProfileScreen1>:
    name:'profile1'
    MDToolbar:
        title:"Profile" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    
    MDCard:
        size_hint:.7,.7
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}
        elevation:25
        MDFloatLayout:    
            MDTextField:
                id:mail
                icon_right:'email'
                hint_text:"E-mail"
                helper_text:"example@gmail.com"
                helper_text_mode:"on_focus"
                pos_hint:{'center_x': 0.5, 'center_y': 0.80}
                #size_hint_x:None
                #width:250
                color_mode:'accent'
                required:True
            
            MDFillRoundFlatButton:
                text:"Get OTP"
                pos_hint:{'center_x': 0.5, 'center_y': 0.70}
                #disabled:True if mail.text== '' else False
                md_bg_color:0,0.5,0,1
                on_press:
                    app.toast_text(0)
    
                on_release:
                    root.no=app.get_mail()
                    print(root.no)

            MDTextField:
                id:otp
                icon_right:'lock'
                hint_text:"OTP"
                helper_text:"Enter the OTP you received"
                helper_text_mode:"on_focus"
                pos_hint:{'center_x': 0.5, 'center_y': 0.55}
                #size_hint_x:None
                #width:250
                color_mode:'accent'
                required:True
            
            MDFillRoundFlatButton:
                text:"Submit"
                pos_hint:{'center_x': 0.5, 'center_y': 0.45}
                md_bg_color:.0,0.5,0,1
                #disabled:True if otp.text== '' else False
                on_press:
                    app.validate_otp(root.no)
                                             
            MDTextField:
                id:name
                icon_right:'email'
                hint_text:"Name"
                helper_text:"Enter your legal name "
                helper_text_mode:"on_focus"
                pos_hint:{'center_x': 0.5, 'center_y': 0.90}
                #size_hint_x:None
                #width:250
                color_mode:'accent'
                required:True
                    
            MDFillRoundFlatButton:
                text:"Register"
                pos_hint:{'center_x': 0.5, 'center_y': 0.20}
                md_bg_color:.5,0,0,1
                on_press:
                    app.register()
                    #root.manager.current='profile2'
                    

"""
