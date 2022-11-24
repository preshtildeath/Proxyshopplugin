"""
WARPDANDY TEMPLATES
"""
import os
import proxyshop.frame_logic as frame_logic
import proxyshop.format_text as format_text
import proxyshop.text_layers as txt_layers
import proxyshop.templates as temp
import proxyshop.constants as con
import proxyshop.settings as cfg
import proxyshop.helpers as psd
import photoshop.api as ps
app = ps.Application()

class FullartTrixTemplate (temp.NormalFullartTemplate):
    """
     * Port of TrixAreForScoot Proximity Template
     * Created by WarpDandy & TrixAreForScoot
    """
    def template_file_name (self):
        return "WarpDandy/FullartTrix"
    
    def template_suffix (self):
        return "FullartTrix"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()

 
class LegendsTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Legends"
    
    def template_suffix (self):
        return "Legends"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
 
class SamuraiTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Samurai"
    
    def template_suffix (self):
        return "Samurai"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        

class NinjaTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Ninja"
    
    def template_suffix (self):
        return "Ninja"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
 
class NinjaGlitchTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/NinjaGlitch"
    
    def template_suffix (self):
        return "Glitch Ninja"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()   


class MirrorTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Mirror"
    
    def template_suffix (self):
        return "Left-Handed"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
         
 
class ClassicWhiteBorderTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/ClassicWhiteBorder"
    
    def template_suffix (self):
        return "Classic WB"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
 
class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameSmall"

    def template_suffix (self):
        return "Ikoria S"

    def __init__ (self, layout):
        # strip out reminder text for fullart
        super().__init__(layout)

    def basic_text_layers(self, text_and_icons):
        super().basic_text_layers(text_and_icons)

        nickname_layer = psd.getLayer("Manual Nickname", text_and_icons)
        n = self.layout.file
        nickname_text = n[n.rfind("{")+1:n.rfind("}")]
        if n == "": return None
        self.tx_layers.append(
            txt_layers.ScaledTextField(
                layer=nickname_layer,
                contents=nickname_text,
                reference=psd.getLayer("Mana Cost", text_and_icons),
            )
        )

    def enable_frame_layers (self):

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature:
            psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land:
            pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        if self.is_legendary:
            # legendary crown
            psd.getLayer(self.layout.pinlines, con.layers['LEGENDARY_CROWN']).visible = True
            app.activeDocument.activeLayer = pinlines
            psd.enable_active_layer_mask()
        
    def post_text_layers(self):
        super().post_text_layers()
        psd.content_fill_empty_area(self.art_layer)
           
    


class NicknameMediumTemplate (NicknameSmallTemplate):
    """
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameMedium"

    def template_suffix (self):
        return "Ikoria M"
            
   
class NicknameLargeTemplate (NicknameSmallTemplate):
    """
     * Requires manually adding the nickname
    """
    def template_file_name (self):
        return "WarpDandy/NicknameLarge"

    def template_suffix (self):
        return "Ikoria L"
            
class GoldenAgeTemplate (temp.NormalFullartTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAge"
    
    def template_suffix (self):
        return "Golden Age"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
        self.art_reference = psd.getLayer("Full Art Frame")
    
    # OPTIONAL
    def enable_frame_layers (self):

        # Add blurry background image
        # self.art_layer.duplicate()
        # app.activeDocument.activeLayer = self.art_layer
        # art_bounds = self.art_layer.bounds
        # width, height = art_bounds[2]-art_bounds[0], art_bounds[3]-art_bounds[1]
        # scale = 100 * max(app.activeDocument.width/width, app.activeDocument.height/height)
        # self.art_layer.resize(scale, scale)
        # app.activeDocument.selection.selectAll()
        # psd.align_horizontal()
        # psd.align_vertical()
        # psd.clear_selection()
        # self.art_layer.applyMinimum(3)
        # self.art_layer.applyGaussianBlur(30)

        super().enable_frame_layers()
       
class GoldenAge2Template (temp.NormalFullartTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAge2"
    
    def template_suffix (self):
        return "Golden Age 2"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
