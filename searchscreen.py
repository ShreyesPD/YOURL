shs = """
<SearchScreen>:
    name:'search'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Database Scan/ User Rating" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1
    
    BoxLayout:
        orientation:'vertical'
        
        MDLabel:
            id:label1
            text:'URL'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        
        MDLabel:
            id:label2
            text:'STATUS'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        
        BoxLayout:
            MDLabel:
                id:label7
                text:'User Rating: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 
            MDLabel:
                id:label6
                text:'User Rating'
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 
        
        MDRectangleFlatButton:
            text:"Next" 
            pos_hint:{'center_x': 0.87, 'center_y': 0.04}
            #disabled:True if root.f== 0 else False      
            on_press:
                root.manager.current='search2'

        # MDLabel:
        #     id:label4
        #     text:'Domain Info'
        #     #pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        
                                
        # BoxLayout:
        #     orientation:'vertical'
        #     canvas.before:
        #         BorderImage:
        #             source:"themes\classic_theme\search.png"
        #             size:self.size
        #             #size_hint_x:1
        #             #size_hint_y:1
        #             #width:self.parent.width
        #             #height:self.parent.heightS
"""
shs2 = """
<SearchScreen2>:
    name:'search2'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"API Scan" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1
    MDBoxLayout:
        MDLabel:
            id:label15
            text:'VIRUSTOTAL API: '
            #pos_hint:{'center_x': 0.5, 'center_y': 0.5} 
        
        MDLabel:
            id:label3
            text:'STATUS'
            #pos_hint:{'center_x': 0.7, 'center_y': 0.7} 
        
    MDRectangleFlatButton:
        text:"Previous" 
        pos_hint:{'center_x': 0.13, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search'
    
    MDRectangleFlatButton:
        text:"Next" 
        pos_hint:{'center_x': 0.87, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search3'
        
"""

shs3 = """
<SearchScreen3>:
    name:'search3'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title:"Domain Info" 
            pos_hint:{'top':1.0}  
            left_action_items:[["home", lambda x:app.go_back('home')]]
            elevation:10
            #size_hint_x:1

        ScrollView:
            Label:
                id:label4
                # size_hint_x: 1.0
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width,None
                text:'Domain Info'
                align: 'left'

            #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

        MDBoxLayout:
            size_hint_y: None
            height: self.minimum_height
            
            MDRectangleFlatButton:
                text:"Previous" 
                #pos_hint:{'center_x': 0.13, 'center_y': 0.5}
                #disabled:True if root.f== 0 else False      
                on_press:
                    root.manager.current='search2'
            
            MDBoxLayout:
                MDRectangleFlatButton:
                    text:"Download Info" 
                    #pos_hint:{'center_x': 270.4, 'center_y': 0.5}
                    #disabled:True if root.f== 0 else False      
                    on_press:
                        app.downld_dinfo()
                
            MDRectangleFlatButton:
                text:"Next" 
                #pos_hint:{'center_x': 270.4, 'center_y': 0.5}
                #disabled:True if root.f== 0 else False      
                on_press:
                    root.manager.current='search4'

"""


shs4 = """
<SearchScreen4>:
    name:'search4'
    FitImage:
        source:'themes\classic_theme\search.png'

    
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title:"SSL / TLS Certificate Info" 
            pos_hint:{'top':1.0}  
            left_action_items:[["home", lambda x:app.go_back('home')]]
            elevation:10
            #size_hint_x:1
        
        MDLabel:
            id:label4
            text:'Issued to:'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 
        
        MDBoxLayout:
            MDLabel:
                id:label5
                text:'Common Name(CA): '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
            
            MDLabel:
                id:label51
                text:'Common Name(CA): '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        
        MDLabel:
            id:label3
            text:'Issued by:'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        
        MDBoxLayout:
            MDLabel:
                id:label6
                text:'Common Name(CA): '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
            
            MDLabel:
                id:label61
                text:'Common Name(CA): '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        
        
        MDBoxLayout:   
            MDLabel:
                id:label7
                text:'Organisation Name: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}          
            
            MDLabel:
                id:label71
                text:'Organisation Name: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}          

        MDBoxLayout:
            MDLabel:
                id:label8
                text:'Country: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

            MDLabel:
                id:label81
                text:'Country: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

        MDBoxLayout:
            MDLabel:
                id:label9
                text:'Issued on: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
            
            MDLabel:
                id:label91
                text:'Issued on: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        
        MDBoxLayout:
            MDLabel:
                id:label10
                text:'Expires on: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
            
            MDLabel:
                id:label101
                text:'Expires on: '
                #pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        

        MDBoxLayout:
            MDRectangleFlatButton:
                text:"Previous" 
                #pos_hint:{'center_x': 0.13, 'center_y': 0.04}
                #disabled:True if root.f== 0 else False      
                on_press:
                    root.manager.current='search3'
            MDRectangleFlatButton:
            MDRectangleFlatButton:
            MDRectangleFlatButton:
                text:"Next" 
                #pos_hint:{'center_x': 0.9, 'center_y': 0}
                #disabled:True if root.f== 0 else False      
                on_press:
                    #root.img=app.update_path()
                    root.manager.current='search5'

"""

shs5 = """
<SearchScreen5>:
    name:'search5'
    FitImage:
        source:'themes\classic_theme\search.png'
    
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:"Visual Preview" 
            pos_hint:{'top':1.0}  
            left_action_items:[["home", lambda x:app.go_back('home')]]
            elevation:10
            size_hint_x:1
           
        #MDFloatLayout:
        # pos_hint: {"center_y": 1}
        # size_hint_y: None
        #height: '5dp'
        FitImage:
            id:ss
            source:'screen_shot.png'
            #pos_hint: {"center_y": 0.5}
            #size_hint_y:0.5 
            #size_hint_x:1
            
        MDRectangleFlatButton:
            text:"Previous" 
            pos_hint:{'center_x': 0.13, 'center_y': 0.04}
            #disabled:True if root.f== 0 else False      
            on_press:
                root.manager.current='search4'

"""
