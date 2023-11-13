
# code points for the 5 skin tones
light, medium_light, medium, medium_dark, dark = range(0x1F3FB,0x1F400)
for skin_tone in light, medium_light, medium, medium_dark, dark:
    face = "\U0001F469"
    hand = "\U0001F91A"
    skin_tone_char = chr(skin_tone)  # use Unicode value to create character
    print(f"{face}{skin_tone_char}{hand}{skin_tone_char}")

