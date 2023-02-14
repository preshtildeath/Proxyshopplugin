"""
WARPDANDY TEMPLATES
"""
from functools import cached_property
from typing import Optional

from photoshop.api._layerSet import LayerSet

import proxyshop.format_text as ft
import proxyshop.text_layers as text_classes
import proxyshop.templates as temp
import proxyshop.helpers as psd
from proxyshop.constants import con
from proxyshop.settings import cfg

from photoshop.api._artlayer import ArtLayer
import photoshop.api as ps
app = ps.Application()


class SamuraiTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Samurai"
    template_suffix = "Samurai"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
        

class NinjaTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Ninja"
    template_suffix = "Ninja"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return
 
 
class NinjaGlitchTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/NinjaGlitch"
    template_suffix = "Glitch Ninja"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill for extended art
        psd.content_fill_empty_area(self.art_layer)


class MirroredTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Mirror"
    template_suffix = "Mirrored"

    def basic_text_layers(self):
        # Flip scaling on text layers
        self.text.extend([
            text_classes.FormattedTextField(
                layer=self.text_layer_mana,
                contents=self.layout.mana_cost
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_name,
                contents=self.layout.name,
                reference=self.text_layer_mana,
                flip_scale=True
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_type,
                contents=self.layout.type_line,
                reference=self.expansion_symbol,
                flip_scale=True
            )
        ])

    @property
    def expansion_symbol_anchor(self) -> ps.AnchorPosition:
        return ps.AnchorPosition.MiddleLeft

    def load_artwork(self):
        super().load_artwork()
        self.active_layer.resize(-100, 100, ps.AnchorPosition.MiddleCenter)
         
 
class ClassicWhiteBorderTemplate (temp.NormalClassicTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/ClassicWhiteBorder"
    template_suffix = "Classic WB"


class NicknameSmallTemplate (temp.NormalTemplate):
    """
     * Requires manually adding the nickname
    """
    template_file_name = "WarpDandy/NicknameSmall"
    template_suffix = "Nickname S"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def art_reference_layer(self) -> Optional[ArtLayer]:
        return psd.getLayer(con.layers.ART_FRAME)

    @cached_property
    def text_layer_nickname(self) -> ArtLayer:
        return psd.getLayer("Manual Nickname", self.text_layers)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill for extended art
        psd.content_fill_empty_area(self.art_layer)

    def basic_text_layers(self) -> None:

        if "{" in self.layout.filename:
            start = self.layout.filename.find("{") + 1
            end = self.layout.filename.find("}")
            nickname = self.layout.filename[start:end]
            self.text.append(
                text_classes.ScaledTextField(
                    layer=self.text_layer_nickname,
                    contents=nickname,
                    reference = self.text_layer_mana,
                )
            )
        else:
            cfg.exit_early = True

        self.text.extend([
            text_classes.FormattedTextField(
                layer = self.text_layer_mana,
                contents = self.layout.mana_cost,
            ),
            text_classes.TextField(
                layer = self.text_layer_name,
                contents = self.layout.name,
            ),
            text_classes.ScaledTextField(
                layer = self.text_layer_type,
                contents = self.layout.type_line,
                reference = self.expansion_symbol,
            )
        ])

           

class NicknameMediumTemplate (NicknameSmallTemplate):
    """
     * Requires manually adding the nickname
    """
    template_file_name = "WarpDandy/NicknameMedium"
    template_suffix = "Nickname M"


class GoldenAgeTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/GoldenAge"
    template_suffix = "Golden Age"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class zneExpeditionTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/zneExpedition"
    template_suffix = "Original Expedition"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class SkyscraperTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Skyscraper"
    template_suffix = "Skyscraper"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class GoldenAgeV2Template (temp.NormalTemplate):
    """
     * Created by MrOppsokopolis
    """
    template_file_name = "WarpDandy/GoldenAgeV2"
    template_suffix = "Golden Age V2"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class ArtDecoTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/ArtDeco"
    template_suffix = "Art Deco"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class UniversesBeyondTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/UniversesBeyond"
    template_suffix = "Universes Beyond"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class EtchedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/Etched"
    template_suffix = "Etched"

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


class DestinyTemplate (temp.NormalTemplate):
    """
     * Created by Meeple, ported to Proxyshop by WarpDandy
    """
    template_file_name = "WarpDandy/Destiny"
    template_suffix = "Destiny"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

        
class PinlinesExtNeonTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/PinlinesExtNeon"
    template_suffix = "Neon Extended"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def color_indicator_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class MysticalArchiveTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/MysticalArchive"
    template_suffix = "Mystical Archive"

    @property
    def is_legendary(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class FangExtendedTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/FangExtended"
    template_suffix = "Fang Extended"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    def load_artwork(self):
        # Content aware fill
        super().load_artwork()
        psd.content_fill_empty_area(self.art_layer)


class GoldenAgeFullArtTemplate (temp.NormalTemplate):
    """
     * Created by WarpDandy
    """
    template_file_name = "WarpDandy/GoldenAgeFullArt"
    template_suffix = "Golden Age Full Art"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return


"""
Planeswalker templates
"""


class ClassicPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    template_file_name = "WarpDandy/ClassicPW"
    template_suffix = "Classic PW"

    def __init__(self, layout):
        cfg.real_collector = False
        super().__init__(layout)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    @cached_property
    def group(self) -> LayerSet:
        return psd.getLayerSet("Planeswalker")

    @cached_property
    def ability_divider(self) -> Optional[ArtLayer]:
        div = cfg.get_setting(section="TEXT", key="Ability.Divider", default="Modern", is_bool=False)
        if div == "Modern":
            return psd.getLayer("Divider", self.loyalty_group)
        if div == "Classic":
            return psd.getLayer("Divider Block", self.loyalty_group)
        return

    def basic_text_layers(self):

        # Iterate through abilities to add text layers
        for i, ability in enumerate(self.abilities):

            # Get the colon index, determine if this is static or activated ability
            colon_index = ability.find(": ")
            if 5 > colon_index > 0:

                # Determine which loyalty group to enable, and set the loyalty symbol's text
                loyalty_graphic = psd.getLayer(con.layers.COST, self.loyalty_group).duplicate()
                loyalty_graphic.textItem.contents = ability[:int(colon_index)]
                if colon_index > 2:
                    loyalty_graphic.textItem.size = (
                            psd.get_text_scale_factor(loyalty_graphic) * loyalty_graphic.textItem.size
                    ) - 1
                    loyalty_graphic.translate(0, -4)
                ability_layer = psd.getLayer(con.layers.ABILITY_TEXT, self.loyalty_group).duplicate()

                # Add text layer, shields, and colons to list
                self.ability_layers.append(ability_layer)
                self.shields.append(loyalty_graphic)
                self.colons.append(psd.getLayer(con.layers.COLON, self.loyalty_group).duplicate())
                ability = ability[colon_index + 2:]

            else:

                # Hide default ability, switch to static
                ability_layer = psd.getLayer(con.layers.STATIC_TEXT, self.loyalty_group).duplicate()
                self.ability_layers.append(ability_layer)
                self.shields.append(None)
                self.colons.append(None)

                # Is this a double line ability?
                if "\n" in ability:
                    self.active_layer = ability_layer
                    ft.space_after_paragraph(2)

            # Add ability text
            self.text.append(
                text_classes.FormattedTextField(
                    layer=ability_layer,
                    contents=ability
                )
            )

        # Starting loyalty
        psd.getLayer(
            con.layers.TEXT, [self.loyalty_group, con.layers.STARTING_LOYALTY]
        ).textItem.contents = self.layout.loyalty

        # Add text layers.
        self.text.extend([
            text_classes.FormattedTextField(
                layer=self.text_layer_mana,
                contents=self.layout.mana_cost
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_name,
                contents=self.layout.name,
                reference=self.text_layer_mana
            ),
            text_classes.ScaledTextField(
                layer=self.text_layer_type,
                contents=self.layout.type_line,
                reference=self.expansion_symbol
            )
        ])

    def pw_ability_mask(self):
        # Position a divider between each ability layer
        if self.ability_divider:
            for i in range(len(self.ability_layers) - 1):
                divider = self.ability_divider.duplicate()
                psd.position_between_layers(divider, self.ability_layers[i], self.ability_layers[i+1])
                if self.ability_divider.name != "Divider Block":
                    divider.translate(0, -6)


class ArtDecoPWTemplate (temp.PlaneswalkerTemplate):
    """
     * Planeswalker template - 3 or 4 loyalty abilities.
    """
    template_file_name = "WarpDandy/ArtDecoPW"
    template_suffix = "Art Deco PW"
