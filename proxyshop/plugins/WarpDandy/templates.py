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

class FullartTrixTemplate (temp.NormalTemplate):
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
    def enable_frame_layers(self):

        # Easy reference
        docref = app.activeDocument

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature: psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land: pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        # background
        background = psd.getLayerSet(con.layers['BACKGROUND'])
        if self.layout.is_nyx: background = psd.getLayerSet(con.layers['NYX'])
        psd.getLayer(self.layout.background, background).visible = True

        # Content aware fill
        docref.activeLayer = self.art_layer
        psd.content_fill_empty_area()   


class MirrorTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Mirror"
    
    def template_suffix (self):
        return "Mirror"
    
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
     * Automates nickname
     * "Cardname (Artist) [SET] {Nickname}.gif/jpg" for art file
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
     * Automates nickname
     * "Cardname (Artist) [SET] {Nickname}.gif/jpg" for art file
    """
    def template_file_name (self):
        return "WarpDandy/NicknameMedium"

    def template_suffix (self):
        return "Ikoria M"
    
            
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
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
       
class GoldenAge2Template (temp.NormalTemplate):
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
        
class zneExpeditionTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/zneExpedition"
    
    def template_suffix (self):
        return "Original Expedition"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class SkyscraperTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Skyscraper"
    
    def template_suffix (self):
        return "Skyscraper"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class GoldenAgeV2Template (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAgeV2"
    
    def template_suffix (self):
        return "Golden Age V2"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class ArtDecoTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/ArtDeco"
    
    def template_suffix (self):
        return "Art Deco"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class UniversesBeyondTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/UniversesBeyond"
    
    def template_suffix (self):
        return "Universes Beyond"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class ClassicBorderlessShortTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/ClassicBorderlessShort"
    
    def template_suffix (self):
        return "Classic Borderless Short"
    
    # OPTIONAL
    def __init__(self, layout):
        # strip out reminder text for extended cards
        cfg.remove_reminder = True
        super().__init__(layout)
        # art
        self.art_reference = psd.getLayer(con.layers['ART_FRAME'])

    def enable_frame_layers(self):

        # Easy reference
        docref = app.activeDocument

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature: psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land: pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        # background
        background = psd.getLayerSet(con.layers['BACKGROUND'])
        if self.layout.is_nyx: background = psd.getLayerSet(con.layers['NYX'])
        psd.getLayer(self.layout.background, background).visible = True

        if self.is_legendary:
            # legendary crown
            crown = psd.getLayerSet(con.layers['LEGENDARY_CROWN'])
            psd.getLayer(self.layout.pinlines, crown).visible = True
            psd.getLayer(con.layers['NORMAL_BORDER'], con.layers['BORDER']).visible = False
            psd.getLayer(con.layers['LEGENDARY_BORDER'], con.layers['BORDER']).visible = True

            # Mask the top border sides
            docref.activeLayer = background
            psd.enable_active_layer_mask()

            # enable companion texture
            if self.is_companion: psd.getLayer(self.layout.pinlines, con.layers['COMPANION']).visible = True

            # Hollow crown
            if self.layout.is_nyx or self.is_companion:
                # Enable the hollow crown shadow and layer mask on crown, pinlines, and shadows
                super().enable_hollow_crown(crown, pinlines)
                docref.activeLayer = psd.getLayer("Shadows Light", "Shadows")
                psd.enable_active_layer_mask()

        # Content aware fill
        docref.activeLayer = self.art_layer
        psd.content_fill_empty_area()
        
class EighthTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Eighth"
    
    def template_suffix (self):
        return "Eighth"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
         
class EtchedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Etched"
    
    def template_suffix (self):
        return "Etched"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers() 
        
class DestinyTemplate (temp.NormalTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/Destiny"
    
    def template_suffix (self):
        return "Destiny"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class PinlinesExtNeonTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/PinlinesExtNeon"
    
    def template_suffix (self):
        return "Neon Extended"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers(self):

        # Easy reference
        docref = app.activeDocument

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature: psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land: pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        # background
        background = psd.getLayerSet(con.layers['BACKGROUND'])
        if self.layout.is_nyx: background = psd.getLayerSet(con.layers['NYX'])
        psd.getLayer(self.layout.background, background).visible = True

        # Content aware fill
        docref.activeLayer = self.art_layer
        psd.content_fill_empty_area()
        
class MysticalArchiveTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/MysticalArchive"
    
    def template_suffix (self):
        return "Mystical Archive"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
        # full art
        self.art_reference = psd.getLayer(con.layers['ART_FRAME']) 
        
    # OPTIONAL
    def enable_frame_layers(self):

        # Easy reference
        docref = app.activeDocument

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature: psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land: pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        # background
        background = psd.getLayerSet(con.layers['BACKGROUND'])
        if self.layout.is_nyx: background = psd.getLayerSet(con.layers['NYX'])
        psd.getLayer(self.layout.background, background).visible = True

        # Content aware fill
        docref.activeLayer = self.art_layer
        psd.content_fill_empty_area() 
        
class FangExtendedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/FangExtended"
    
    def template_suffix (self):
        return "Fang Extended"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers(self):

        # Easy reference
        docref = app.activeDocument

        # twins and pt box
        psd.getLayer(self.layout.twins, con.layers['TWINS']).visible = True
        if self.is_creature: psd.getLayer(self.layout.twins, con.layers['PT_BOX']).visible = True

        # pinlines
        pinlines = psd.getLayerSet(con.layers['PINLINES_TEXTBOX'])
        if self.is_land: pinlines = psd.getLayerSet(con.layers['LAND_PINLINES_TEXTBOX'])
        psd.getLayer(self.layout.pinlines, pinlines).visible = True

        # background
        background = psd.getLayerSet(con.layers['BACKGROUND'])
        if self.layout.is_nyx: background = psd.getLayerSet(con.layers['NYX'])
        psd.getLayer(self.layout.background, background).visible = True

        # Content aware fill
        docref.activeLayer = self.art_layer
        psd.content_fill_empty_area()
        
        if self.is_legendary:
            # legendary crown
            psd.getLayer(self.layout.pinlines, con.layers['LEGENDARY_CROWN']).visible = True
            border = psd.getLayerSet(con.layers['BORDER'])
            psd.getLayer(con.layers['NORMAL_BORDER'], border).visible = False
            psd.getLayer(con.layers['LEGENDARY_BORDER'], border).visible = True
        
class GoldenAgeFullArtTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/GoldenAgeFullArt"
    
    def template_suffix (self):
        return "Golden Age Full Art"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class TallArtClassicTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    def template_file_name (self):
        return "WarpDandy/TallArtClassic"
    
    def template_suffix (self):
        return "Tall Art Classic"
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()
        
class SilvanMDFCBackTemplate (temp.MDFCBackTemplate):
    """
    Silvan Full template modified for MDFC
    """
    template_file_name = "WarpDandy/full-mdfc-back"
    dfc_layer_group = con.layers['MDFC_BACK']
    template_suffix = "Full"

    def __init__(self, layout):
        cfg.remove_reminder = True
        super().__init__(layout)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


class SilvanMDFCFrontTemplate (SilvanMDFCBackTemplate):
    """
    Silvan Full template modified for MDFC
    """
    template_file_name = "WarpDandy/full-mdfc-front"
    dfc_layer_group = con.layers['MDFC_FRONT']
    template_suffix = "Full"

        
"""
Planeswalker templates
"""
class ClassicPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    def template_file_name (self):
        return "WarpDandy/ClassicPW"

    def __init__ (self, layout):
        self.exit_early = True
        super().__init__(layout)

        if self.layout.is_colorless: self.art_reference = psd.getLayer(con.layers['FULL_ART_FRAME'])
        else: self.art_reference = psd.getLayer(con.layers['PLANESWALKER_ART_FRAME'])

        ability_array = self.layout.oracle_text.split("\n")
        num_abilities = 3
        if len(ability_array) > 3: num_abilities = 4

        # docref for everything but legal and art reference is based on number of abilities
        self.docref = psd.getLayerSet("pw-"+str(num_abilities))
        self.docref.visible = True

        # Basic text layers
        self.basic_text_layers(psd.getLayerSet(con.layers['TEXT_AND_ICONS'], self.docref))

        # planeswalker ability layers
        group_names = [con.layers['FIRST_ABILITY'], con.layers['SECOND_ABILITY'], con.layers['THIRD_ABILITY'], con.layers['FOURTH_ABILITY']]
        loyalty_group = psd.getLayerSet(con.layers['LOYALTY_GRAPHICS'], self.docref)

        for i, ability in enumerate(ability_array):
            if i == 4: break
            ability_group = psd.getLayerSet(group_names[i], loyalty_group)
            static_text_layer = psd.getLayer(con.layers['STATIC_TEXT'], ability_group)
            ability_text_layer = psd.getLayer(con.layers['ABILITY_TEXT'], ability_group)
            ability_layer = ability_text_layer
            colon_index = ability.find(": ")

            # determine if this is a static or activated ability by the presence of ":" in the start of the ability
            if colon_index > 0 < 5:
                # activated ability

                # determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayerSet(ability[0], ability_group)
                loyalty_graphic.visible = True
                self.tx_layers.append(
                    txt_layers.TextField(
                        layer = psd.getLayer(con.layers['COST'], loyalty_graphic),
                        text_contents = ability[0:int(colon_index)],
                        text_color = psd.rgb_black(),
                    )
                )
                ability = ability[int(colon_index)+2:]

            else:
                # static ability
                ability_layer = static_text_layer
                ability_text_layer.visible = False
                static_text_layer.visible = True
                psd.getLayer("Colon", ability_group).visible = False

            self.tx_layers.append(
                txt_layers.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.tx_layers.append(
            txt_layers.TextField(
                layer = psd.getLayer(con.layers['TEXT'], psd.getLayerSet(con.layers['STARTING_LOYALTY'], loyalty_group)),
                text_contents = self.layout.scryfall['loyalty'],
                text_color = psd.rgb_white(),
            )
        )

        # paste scryfall scan
        app.activeDocument.activeLayer = psd.getLayerSet(con.layers['TEXTBOX'], self.docref)
        self.paste_scryfall_scan(psd.getLayer(con.layers['SCRYFALL_SCAN_FRAME']))

    def enable_frame_layers (self):
        # Twins, pinlines, background
        psd.getLayer(self.layout.twins, psd.getLayerSet(con.layers['TWINS'], self.docref)).visible = True
        psd.getLayer(self.layout.pinlines, psd.getLayerSet(con.layers['PINLINES'], self.docref)).visible = True
        self.enable_background()

    def enable_background (self):
        """
        Enable card background
        """
        psd.getLayer(self.layout.background, psd.getLayerSet(con.layers['BACKGROUND'], self.docref)).visible = True
        
    def template_suffix (self):
        return "Classic PW"
        
class ArtDecoPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    def template_file_name (self):
        return "WarpDandy/ArtDecoPW"

    def __init__ (self, layout):
        self.exit_early = True
        super().__init__(layout)

        if self.layout.is_colorless: self.art_reference = psd.getLayer(con.layers['FULL_ART_FRAME'])
        else: self.art_reference = psd.getLayer(con.layers['PLANESWALKER_ART_FRAME'])

        ability_array = self.layout.oracle_text.split("\n")
        num_abilities = 3
        if len(ability_array) > 3: num_abilities = 4

        # docref for everything but legal and art reference is based on number of abilities
        self.docref = psd.getLayerSet("pw-"+str(num_abilities))
        self.docref.visible = True

        # Basic text layers
        self.basic_text_layers(psd.getLayerSet(con.layers['TEXT_AND_ICONS'], self.docref))

        # planeswalker ability layers
        group_names = [con.layers['FIRST_ABILITY'], con.layers['SECOND_ABILITY'], con.layers['THIRD_ABILITY'], con.layers['FOURTH_ABILITY']]
        loyalty_group = psd.getLayerSet(con.layers['LOYALTY_GRAPHICS'], self.docref)

        for i, ability in enumerate(ability_array):
            if i == 4: break
            ability_group = psd.getLayerSet(group_names[i], loyalty_group)
            static_text_layer = psd.getLayer(con.layers['STATIC_TEXT'], ability_group)
            ability_text_layer = psd.getLayer(con.layers['ABILITY_TEXT'], ability_group)
            ability_layer = ability_text_layer
            colon_index = ability.find(": ")

            # determine if this is a static or activated ability by the presence of ":" in the start of the ability
            if colon_index > 0 < 5:
                # activated ability

                # determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayerSet(ability[0], ability_group)
                loyalty_graphic.visible = True
                self.tx_layers.append(
                    txt_layers.TextField(
                        layer = psd.getLayer(con.layers['COST'], loyalty_graphic),
                        text_contents = ability[0:int(colon_index)],
                        text_color = psd.rgb_white(),
                    )
                )
                ability = ability[int(colon_index)+2:]

            else:
                # static ability
                ability_layer = static_text_layer
                ability_text_layer.visible = False
                static_text_layer.visible = True
                psd.getLayer("Colon", ability_group).visible = False

            self.tx_layers.append(
                txt_layers.BasicFormattedTextField(
                    layer = ability_layer,
                    text_contents = ability,
                    text_color = psd.get_text_layer_color(ability_layer),
                )
            )

        # starting loyalty
        self.tx_layers.append(
            txt_layers.TextField(
                layer = psd.getLayer(con.layers['TEXT'], psd.getLayerSet(con.layers['STARTING_LOYALTY'], loyalty_group)),
                text_contents = self.layout.scryfall['loyalty'],
                text_color = psd.rgb_white(),
            )
        )

        # paste scryfall scan
        app.activeDocument.activeLayer = psd.getLayerSet(con.layers['TEXTBOX'], self.docref)
        self.paste_scryfall_scan(psd.getLayer(con.layers['SCRYFALL_SCAN_FRAME']))

    def enable_frame_layers (self):
        # Twins, pinlines, background
        psd.getLayer(self.layout.twins, psd.getLayerSet(con.layers['TWINS'], self.docref)).visible = True
        psd.getLayer(self.layout.pinlines, psd.getLayerSet(con.layers['PINLINES'], self.docref)).visible = True
        self.enable_background()

    def enable_background (self):
        """
        Enable card background
        """
        psd.getLayer(self.layout.background, psd.getLayerSet(con.layers['BACKGROUND'], self.docref)).visible = True
        
    def template_suffix (self):
        return "Art Deco PW"
