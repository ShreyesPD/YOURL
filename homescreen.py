hs = """
<HomeScreen>:    
    name:'home'    
    MDFloatLayout:
        FitImage:
            id:home_image
            source:"themes\classic_theme\home.png"
            #allow_stretch:True
            #keep_ratio:True
            #size_hint:(1,1)
            #pos_hint:{"center_x":.5,"center_y":.5}
            #size_hint_x:None
            #size_hint_y:None
            #width:self.parent.width
            #height:self.parent.height
            
        MDTextField:
            id:link
            hint_text:"ENTER URL"
            helper_text:"Or click on the + button to rate an url"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.6}
            size_hint_x:0.7
            size_hint_y:0.1
            #width:250
            color_mode:'accent'
            required:True
            #mode:"rectangle"
            line_color_normal:app.theme_cls.accent_color
            
        MDRectangleFlatButton:
            text:"Search"
            text_color:app.theme_cls.accent_color 
            pos_hint:{'center_x': 0.8, 'center_y': 0.5}
            size_hint:(0.045, 0.05)
            disabled:True if link.text== '' else False
            on_press:
                root.manager.current='search' 
                app.get_url()
                app.rating_output()
                app.get_api()
                app.get_domain_info()
                app.image_preview()
                app.ssl()
                
                
        MDFloatingActionButton:
            icon:"plus"
            icon_color:app.theme_cls.accent_color 
            pos_hint:{'center_x': 0.9, 'center_y': 0.1}
            on_press:
                app.float()
            
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    MDToolbar:
                        title:"YOURL" 
                        pos_hint:{'top':1.0}  
                        left_action_items:[["menu", lambda x: nav_drawer.set_state('toggle')]]
                        elevation:10

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation:'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:'Settings'
                                #text_color:app.theme_cls.accent_color
                                on_press:
                                    root.manager.current = 'settings'
                                    nav_drawer.set_state('toggle')
                                IconLeftWidget:
                                    icon:'tools'
                                    on_press:
                                        root.manager.current = 'settings'
                                        nav_drawer.set_state('toggle')
                            OneLineIconListItem:
                                text:'FAQs'
                                #text_color:app.theme_cls.accent_color
                                on_press:
                                    root.manager.current = 'faqs'
                                    nav_drawer.set_state('toggle')
                                IconLeftWidget:
                                    icon:'puzzle'                   
                                    on_press:
                                        root.manager.current = 'faqs'     
                                        nav_drawer.set_state('toggle')
                            OneLineIconListItem:
                                text:'Feedback'
                                text_color:app.theme_cls.accent_color
                                on_press:
                                    app.feed()
                                    nav_drawer.set_state('toggle')
                                IconLeftWidget:
                                    icon:'pencil'
                                    on_press:
                                        app.feed()
                                        nav_drawer.set_state('toggle')
                            OneLineIconListItem:
                                text:'Profile'
                                color:app.theme_cls.accent_color
                                on_press:
                                    #root.manager.current = 'profile1'
                                    app.profile_status(0)
                                    nav_drawer.set_state('toggle')
                                IconLeftWidget:
                                    icon:'account'
                                    color:app.theme_cls.accent_color
                                    on_press:
                                        #root.manager.current = 'profile1'
                                        app.profile_status(0)
                                        nav_drawer.set_state('toggle')
    """

bs = """
<BootScreen>:
    name:'boot'
    Image:
        source:'themes\Animation\one.gif'    
"""
